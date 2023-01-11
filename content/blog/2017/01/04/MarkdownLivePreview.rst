---
title: "Markdown Live Preview"
date: "2017-01-04"
permalink: "/blog/2017/01/04/MarkdownLivePreview.html"
tags: [tech, writing, til]
---



It's very useful when creating Markdown__ to be able to preview it live.
For example, creating a complex pull request or a ``README.md``.
I usually use the built-in `Atom Markdown Preview`__ package in Atom__.
Just type ``⌃⇧M`` (aka ``Ctrl+Shift+M``) to see a live preview in an adjacent pane.
I use `vim-mode-plus`__ to edit in Atom,
which provides an acceptable emulation of Vim.

__ https://guides.github.com/features/mastering-markdown/
__ https://github.com/atom/markdown-preview
__ https://atom.io/
__ https://atom.io/packages/vim-mode-plus

I recently discovered `VS Code Markdown Preview`__ in `Visual Studio Code`__.
Type ``⌘K V`` (aka ``Ctrl+K V`` on Windows or Linux)
to invoke the side-by-side live preview.
I use `VSCodeVim`__ to meet my Vim needs.

__ https://code.visualstudio.com/Docs/languages/markdown
__ https://code.visualstudio.com/
__ https://github.com/VSCodeVim/Vim

Unfortunately, neither previewer gives identical results to GitHub's Markdown renderer.
GitHub itself seems to use different renderers for Pull Requests
than it does for ``README.md``\ s.

As an example of markdown that behaves differently in GitHub's ``README.md``
but looks fine in Atom, VSCode, and GitHub's own Pull Requests previewer for Markdown,
consider this nested list.
The *blank* lines before and after the indented “fenced code blocks”
(denoted by triple backticks, :literal:`\`\`\``,  a GitHub-Flavored Markdown extension)
are necessary for the indented code blocks to render properly everywhere.
The blank lines may be omitted in all but the GitHub ``README.md``,
without affecting the rendering.
However, without the blank lines,
the code block will collapse onto one line in the GitHub ``README.md``.

.. code-block:: markdown

	* The following has been tested with RabbitMQ 3.6.0 on macOS
	  (`brew install rabbitmq`):
		- `/usr/local/etc/rabbitmq/rabbitmq-env.conf`
		  should *not* have a localhost entry for `NODE_IP_ADDRESS`;
		  e.g.:

			```
			CONFIG_FILE=/usr/local/etc/rabbitmq/rabbitmq
			#NODE_IP_ADDRESS=127.0.0.1
			NODENAME=rabbit@localhost
			```

		- `/usr/local/etc/rabbitmq/rabbitmq.config`:

			```
			[{rabbit, [{loopback_users, []}]}].
			```

			(Yes, the trailing period is deliberate.)

Both Atom and VSCode are built on top of `Electron`__,
which seems to be an excellent way to built powerful cross-platform desktop apps
using HTML, CSS, and JavaScript on top of Chromium and Node.js.
Other `Electron-based apps`__ that I use include
Brave__, GitKraken__, `Cycligent Git Tool`__, Postman__, Slack__, and Kitematic__.

__ http://electron.atom.io/
__ http://electron.atom.io/apps/
__ https://brave.com/
__ https://www.gitkraken.com/
__ https://www.cycligent.com/git-tool
__ https://www.getpostman.com/
__ https://slack.com/
__ https://kitematic.com/

.. _permalink:
    /blog/2017/01/04/MarkdownLivePreview.html
