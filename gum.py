from cli import CLITool, wraps


class GumPrompt(CLITool):

    def __init__(self):
        super().__init__(
                executable_path="gum",
                # default options don't usually make sense, like placeholder
                # but maybe --style works
                default_options="",
                pyclass_name="GumPrompt")

    def choose(self, choices, *args, **kwargs):
        return self.execute(choices, subcommand='choose', *args, **kwargs)

    def confirm(self):
        pass

    def filter(self, choices, *args, **kwargs):
        return self.execute(choices, subcommand='filter', *args, **kwargs)

    def file(self):
        pass

    def format(self):
        pass

    def input(self):
        pass

    def join(self):
        pass

    def pager(self):
        pass

    def spin(self):
        pass

    def style(self):
        pass

    def table(self):
        pass

    def write(self):
        pass


gum = GumPrompt()
# print(gum)
numbers = [x for x in range(1, 11)]
choice = gum.filter(numbers, "no-limit", header="CHOOSE A NUMBER FOOL")
print(type(choice))
print(choice.__repr__())
print(choice)

if choice == "5":
    print("2+2 got you here, didn't it?")
