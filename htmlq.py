from cli import CLITool


class Htmlq(CLITool):

    def __init__(self):
        super().__init__(
                executable_path="htmlq",
                default_options="",
                pyclass_name="pyhtmlq"
                )

    def css(self, query):
        return self.execute("", subcommand=f'{query}')
