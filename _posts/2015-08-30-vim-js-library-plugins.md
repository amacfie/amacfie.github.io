---
layout: post
title: Managing vim plugins for multiple JS libraries
---

Say you're working on two JS projects with vim: one using BackboneJS and
one using AngularJS.
For each framework, there are plugins, such as [vim-backbone](https://github.com/mklabs/vim-backbone)
and [angular-vim-snippets](https://github.com/matthewsimo/angular-vim-snippets)
that provide editing helpers such as snippets, but how do you prevent the
AngularJS plugins from loading when you're working on the BackboneJS project
and vice versa?

My solution is using [vim-localvimrc](https://github.com/embear/vim-localvimrc)
and [NeoBundle](https://github.com/Shougo/neobundle.vim).

Configuring which plugins load for which filetypes can be done in the main
`.vimrc` but JS frameworks are more specific than filetypes, so we use
vim-localvimrc to define vim configuration for a certain project (or any
directory).
In general, this will work as follows.
My main `.vimrc` file contains

    NeoBundleLazy 'matthewsimo/angular-vim-snippets'

This line registers `angular-vim-snippets` but doesn't load it.
Then in an AngularJS project's root directory, I have a `.lvimrc` file with

    NeoBundleSource angular-vim-snippets

This actually loads the plugin, so it's available when I'm editing a JS file
in that project.
As long as I don't edit an AngularJS project and a BackboneJS project in the
same vim session, this is a very nice solution.

