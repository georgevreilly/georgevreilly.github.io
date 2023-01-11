---
title: "Serializing a NameValueCollection"
date: "2007-07-20"
permalink: "/blog/2007/07/20/SerializingANameValueCollection.html"
tags: [c-sharp, til]
---



.. image:: /content/binary/serialize-nvc.jpg
    :alt: Serializing a NameValueCollection

I had a NameValueCollection embedded inside a larger object.
I needed to serialize the larger object into XML and back.
Unfortunately, NameValueCollection is not XML serializable.
Why I do not know.

A blog comment from `Tim Erwin`_ got me started in the right direction.
Implement ``IXmlSerializable`` and do the work by hand in
``ReadXml`` and ``WriteXml``.

.. _Tim Erwin:
    http://nayyeri.net/archive/2006/08/11/Serialize-NameValueCollection.aspx#72442

Tim's implementation turned out to be overly simple.
It didn't handle an empty collection well,
nor did it leave the ``XmlReader`` in a good state.

I used `SGen`_ to examine the deserialization of a
``List<String>`` to figure out what else needed to be done.

.. _SGen:
    http://msdn2.microsoft.com/en-us/library/bk3w6240(vs.80).aspx

The following ``ReadXml`` seems to work.
If I expected to receive XML from untrusted sources,
I would make this more robust.


.. code:: csharp

    public void ReadXml(XmlReader reader)
    {
        if (reader.IsEmptyElement)
            return;

        while (reader.Read()
            && reader.NodeType != XmlNodeType.EndElement
            && reader.NodeType != XmlNodeType.None)
        {
            if (reader.NodeType == XmlNodeType.Element && reader.LocalName == "Header")
            {
                reader.MoveToAttribute("name");
                string name = reader.Value;
                reader.MoveToAttribute("value");
                string value = reader.Value;
                Add(name, value);
            }
        }
        reader.ReadEndElement();
    }

    public void WriteXml(XmlWriter writer)
    {
       foreach (string name in nvc.Keys)
       {
           writer.WriteStartElement("Header");
           string value = nvc[name];
           writer.WriteAttributeString("name",  name);
           writer.WriteAttributeString("value", value);
           writer.WriteEndElement();
       }
    }

    public XmlSchema GetSchema( )
    {
       return null;
    }

I also found that I needed to implement custom ``Equals``
and ``GetHashCode``, as the ``NameValueCollection``
implementations didn't seem to do what I wanted.

.. code:: csharp

    // Have to override GetHashCode() as two apparently identical NameValueCollections
    // will have different hash codes.
    public override int GetHashCode()
    {
        int hash = nvc.Count;

        foreach (string name in nvc)
        {
            hash = 757 * hash  +  101 * nvc[name].GetHashCode()  +  name.GetHashCode();
        }

        return hash;
    }

    public bool Equals(HeadersCollection that)
    {
        if (ReferenceEquals(that, null))
            return false;

        if (ReferenceEquals(this, that))
            return true;

        // Have to explicitly compare the contents of the collections
        // as NameValueCollection.Equals doesn't seem to do what we want.
        // Note: this is independent of order.
        if (nvc.Count != that.nvc.Count)
            return false;

        foreach (string name in nvc)
        {
            if (nvc[name] != that.nvc.Get(name))
                return false;
        }

        return true;
    }

    public static bool Equals(HeadersCollection headersA, HeadersCollection headersB)
    {
        if (headersA == null)
            return (headersB == null);

        if (ReferenceEquals(headersA, headersB))
            return true;

        return headersA.Equals(headersB);
    }

    public override bool Equals(object obj)
    {
        if (obj is HeadersCollection)
            return Equals((HeadersCollection) obj);

        return false;
    }

.. _permalink:
    /blog/2007/07/20/SerializingANameValueCollection.html
