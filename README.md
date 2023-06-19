# Py in the sky

This is a generalization of the brilliant fzf-iter project.
I've generalized it to work with a lot of shell commands.
You can spin up a number of wrappers pretty quickly and intuitively.
Make a gum wrapper, fd wrapper, htmlq wrapper, rg wrapper, etc.
Awesome.

## Complications
There are some tools, like `fd`, for which the wrapper implementation is ugly using the base `CLITool` class.
This is why.
Under the hood, we're starting a subprocess like so.
`my_process = subprocess.popen(f'{command} {subcommand} {options}', stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding="utf-8")`
We can then very easily send iterables into the subprocess with a pipe.
This is genius for the `fzf` wrapper, and makes commands like `gum filter` `gum choose` ridiculously pleasant to use.
But who sends stdin to `fd`? I certainly don't.
I think `fd` is the excepton, and not the rule; we're usually wanting to pipe the `.__repr__()` of python objects into the command.
Therefore, it *should* raise errors, or complain when nothing is being sent in.
The workaround is putting all of our switches in the subcommand, like `-tf -e pdf -x pdftotext{}`. 
We'll see the base, naive `Fd` class as an example.

```
from cli import CLITool


class Fd(CLITool):
    def __init__(self):
        super().__init__(
                executable_path="fd",
                default_options="--search-path=/ab/so/lute/ly",
                pyclass_name="PY_FD"
                )

    def files(self, query):
        return self.execute("", subcommand=f'-t f {query}')

    def dirs(self, query):
        return self.execute("", subcommand=f'-t d {query}')


```

It's pretty damn simple.
