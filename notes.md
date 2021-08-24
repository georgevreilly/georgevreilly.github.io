# Building and Running the blog

To create a fresh virtualenv.

```bash
python3 -m venv ./venv
```

Use the version of Acrylamid in `~/src/acrylamid`.

First `pip install wheel`, then `pip install -r requirements.txt`

To create a new blog post in `~/stuff/Writing/blog/gvr` aka `./gvrblog`:

```bash
pushd ./gvrblog/drafts/
cp 0.rst foo-bar.rst  # or 0book.rst or 0movie.rst
vim foo-bar.rst
# Fix template fields and _permalink
mv foo-bar.rst ..
```

To liveview a draft in `./gvrblog` at http://localhost:8080/
(misses a lot of Acrylamid niceties):

```bash
./blogview ./gvrblog/drafts/blackbox-paperkey.rst
```

To copy the latest blog posts from `./gvrblog` into `./content`:

```bash
./migrate_gvr_blog.py
```

To view with Acrylamid at http://localhost:8000/blog/:

```bash
acrylamid autocompile
```

To deploy a new blog post to https://www.georgevreilly.com/blog/:

```bash
./migrate_gvr_blog.py
# Compile to ./output
acrylamid compile
# Publish ./output to GitHub Pages
acrylamid deploy
```
