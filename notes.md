# Building and Running the blog

To create a fresh virtualenv. (Acrylamid doesn't work on Python 3 yet):

```bash
virtualenv -p python2.7 ~/.virtualenvs/gvrblog
```

To create a new blog post in `~/stuff/Writing/blog/gvr` aka `./gvrblog`:

```bash
pushd ./gvrblog/drafts/
cp 0.rst foo-bar.rst  # or 0book.rst or 0movie.rst
vim foo-bar.rst
# Fix template fields and _permalink
cp foo-bar.rst ..
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
