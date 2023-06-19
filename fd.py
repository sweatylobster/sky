from cli import CLITool


class Fd(CLITool):
    def __init__(self):
        super().__init__(
                executable_path="fd",
                default_options="--search-path=C:/Users/maxde/code/interpreting/aguila",
                pyclass_name="PY_FD"
                )

    def files(self, query):
        return self.execute("", subcommand=f'-t f {query}')

    def dirs(self, query):
        return self.execute("", subcommand=f'-t d {query}')

    def fd(self, subcommand):
        """
        Simply run `fd` without any prepending or defaults.
        Useful for processing through other CLI commands with fd -x.
        """
        return self.execute("", subcommand=subcommand)
