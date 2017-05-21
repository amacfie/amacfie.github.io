---
layout: post
title: "Building a shell with JavaScript"
---

[ShellJS](https://github.com/shelljs/shelljs) is a JS library that provides
functions like `cd()` and `ls()` which you can use to write Node scripts
instead of bash scripts.
That's great for scripts, but what about an interactive shell?
Well, we could just run the Node repl and import ShellJS:

    $ node
    > require('shelljs/global');
    {}
    > pwd()
    { [String: '/tmp']
      stdout: '/tmp',
      stderr: null,
      code: 0,
      cat: [Function: bound ],
      exec: [Function: bound ],
      grep: [Function: bound ],
      head: [Function: bound ],
      sed: [Function: bound ],
      sort: [Function: bound ],
      tail: [Function: bound ],
      to: [Function: bound ],
      toEnd: [Function: bound ],
      uniq: [Function: bound ] }

Hmm, that's a little verbose, and we might want to avoid manually importing
ShellJS.
We also might want more features than the Node repl offers, such as vi
keybindings.

We can get vi keybindings with rlwrap, but then tab completion goes away.
The solution is given in [this SO answer](http://stackoverflow.com/a/43677273/371334).
First we need to install an rlwrap filter that negotiates tab-completion with a
Node repl.
The filter file can be found at that link, where it's called `node_complete`.
Put `node_complete` in `$RLWRAP_FILTERDIR`, which should be the folder on your
system containing the `RlwrapFilter.pm` Perl module.
For me it's `/usr/share/rlwrap/filters`.

Now rlwrap is ready to negotiate tab completion, but the Node repl isn't.
We'll have to actually write our own Node repl, which is easy because the
`repl` module gives us all the tools we need.
We'll create a file called, say, `myrepl.js`, the contents of which are also
given in [the SO answer](http://stackoverflow.com/a/43677273/371334), only 9
lines.
This script starts a repl with a hook to negotiate tab completion with rlwrap.
If `myrepl.js` is in `~/bin`, now we can run

    $ rlwrap -z node_complete -e '' -c ~/bin/myrepl.js

and have both JS tab completion and rlwrap features, such as vi keybindings
if that's what we've [configured](https://unix.stackexchange.com/q/22740/15513).
Let's create a file called `mysh` with the following contents:

    #!/usr/bin/env bash
    rlwrap -z node_complete -e '' -c ~/bin/myrepl.js

Assuming `~/bin` is in our path variable, we can put `mysh` there and launch
our shell anywhere by just running `mysh`.
So far so good but we wanted to automatically import ShellJS.
In `myrepl.sj`, add the following:

    var shell = require('shelljs');
    Object.assign(myrepl.context, shell);

Those two lines add all the ShellJS functions to the JS global object inside
the repl.
We have:

    $ mysh
    > pwd()
    { [String: '/tmp']
      stdout: '/tmp',
      stderr: null,
      code: 0,
      cat: [Function: bound ],
      exec: [Function: bound ],
      grep: [Function: bound ],
      head: [Function: bound ],
      sed: [Function: bound ],
      sort: [Function: bound ],
      tail: [Function: bound ],
      to: [Function: bound ],
      toEnd: [Function: bound ],
      uniq: [Function: bound ] }

Progress.
Now, how do we clean up this output?
The `repl` module allows us to define a custom `writer`.
This is a function which takes the
output of a line of JS and returns a string to represent the output in the
repl.
What we need to do is intercept objects like the one returned by `pwd()` above
and only show the `stderr` and `stdout` properties.
Add the following near the beginning of `myrepl.js`:

    var util = require('util');

    var myWriter = function(output) {
      var isSS = (
          output &&
          output.hasOwnProperty('stdout') &&
          output.hasOwnProperty('stderr'));
      if (isSS) {
        var stderrPart = output.stderr || '';
        var stdoutPart = output.stdout || '';
        return stderrPart + stdoutPart;
      } else {
        return util.inspect(output, null, null, true);
      }
    };

And load this writer by changing

    var myrepl = require("repl").start({terminal:false});

to

    var myrepl = require("repl").start({
      terminal: false,
      writer: myWriter});

Now we get

    $ mysh
    > pwd()
    \tmp

Much better.
However, since the `echo` function prints its argument to the console _and_
returns an object with it in the `stdout` property, we get this:


    $ mysh
    > echo('hi')
    hi
    hi

I haven't solved this issue quite yet although I'd be surprised if there isn't
a reasonable solution out there.
You can add to `mysh` and `myrepl.js` to get more features, such as colors,
custom evaluation, custom pretty printing, other pre-loaded libraries, et
cetera.
The sky is the limit.
I added an `inspect` function which allows us to see the full ShellJS output
of a command if we really want it.
My complete `myrepl.js` file is:

    #!/usr/bin/env node

    var util = require('util');
    var colors = require('colors/safe');

    var inspect = function(obj) {
      if (obj && typeof obj === 'object') {
        obj['__inspect'] = true;
      }
      return obj;
    };

    var myWriter = function(output) {
      var isSS = (
          output &&
          output.hasOwnProperty('stdout') &&
          output.hasOwnProperty('stderr') &&
          !output.hasOwnProperty('__inspect'));
      if (isSS) {
        var stderrPart = output.stderr || '';
        var stdoutPart = output.stdout || '';
        return colors.cyan(stderrPart + stdoutPart);
      } else {
        if (typeof output === 'object') {
          delete output['__inspect'];
        }
        return util.inspect(output, null, null, true);
      }
    };

    // terminal:false disables readline (just like env NODE_NO_READLINE=1):
    var myrepl = require("repl").start({
      terminal: false,
      prompt: colors.green('% '),
      ignoreUndefined: true,
      useColors: true,
      writer: myWriter});

    var shell = require('shelljs');
    Object.assign(myrepl.context, shell);
    myrepl.context['inspect'] = inspect;

    // add REPL command rlwrap_complete(prefix) that prints a simple list
    //   of completions of prefix
    myrepl.context['rlwrap_complete'] =  function(prefix) {
      myrepl.complete(prefix, function(err,data) {
        for (x of data[0]) {console.log(x);}
      });
    };

So this is basically what we wanted.
We have a JS repl with convenient ShellJS commands.
We also have vi keybindings, and tab completion for JS and filenames.
It's very rough around the edges, but it was really simple to make.
GitHub user `streamich` built a [more advanced form](https://github.com/streamich/jssh)
of this, called `jssh` which adds many features but lacks some too.
The bottom line is, if you know JS, you might be surprised at what you can
build.

