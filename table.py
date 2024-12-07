class Table:
        def __init__(self, headers, contents):
            self.headers = headers
            self.contents = contents
            self.key_width = max([len(headers[0]), *[len(str(key)) for key in contents.keys()]])
            self.value_width = max([len(headers[1]), *[len(str(value)) for value in contents.values()]])
        def display_line(self, symbols):
            start, line, middle, end = symbols
            print(start + line * (self.key_width + 2) + middle + line * (self.value_width + 2) + end)
        def display_header(self):
            print(f'│ {str(self.headers[0]):^{self.key_width}} │ {str(self.headers[1]):^{self.value_width}} │')
        def display_content(self, key, value):
            print(f'│ {str(key):<{self.key_width}} │ {str(value):<{self.value_width}} │')
        def display(self):
            self.display_line('┌─┬┐')
            self.display_header()
            self.display_line('╞═╪╡')
            for i, (key, value) in enumerate(self.contents.items()):
                self.display_content(key, value)
                if i + 1 != len(self.contents):
                    self.display_line('├─┼┤')
            self.display_line('└─┴┘')
