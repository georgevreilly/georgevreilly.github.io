To create a fresh virtualenv. (Python 3 doesn't work yet):

    virtualenv -p python2.7 ~/.virtualenvs/gvrblog

To view a draft:

    ./blogview gvrblog/drafts/blackbox-paperkey.rst

To copy the latest blog posts from `~/stuff/Writing/blog/gvr`:

    ./migrate_gvr_blog.py

To view:

    acrylamid autocompile

To create a new file: 

    pushd ~/gvrblog/drafts/
    cp 0.rst foo-bar.rst  # or 0book.rst or 0movie.rst
    vim foo-bar.rst
    # Fix template fields and _permalink
    cp foo-bar.rst ..
