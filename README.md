# Py in the sky

to make a CLI tool.
I just repurposed the fzf-iter project to generalize it for any shell command.
Gum wrapper, fd wrapper, htmlq wrapper, rg wrapper, etc.
Awesome.

Fd is hacky af.
Have to put things in the subcommand.
f'{command} {subcommand} {options}'.
It parses options and reads input in a way convenient to fzf.
This aspect needs to totally be repurposed.
After all, it's just a wrapper.
