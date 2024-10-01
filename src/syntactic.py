import sys

class SyntacticException(Exception):
    def __init__(self, text:str, command:str):
        self.text = text
        self.command = command
    def __str__(self):
        return f"Ошибка синтаксиса: {self.text} ({self.command})"

class HouseLang:
    def __init__(self):
        self.variables = {}

    def eval(self, cmd):
        command = cmd.split(";")[0]
        tokens = command.split(maxsplit=4)
        if not tokens: return
        
        if tokens[0] == "let":
            if len(tokens) != 4 or tokens[2] != "=":
                raise SyntacticException("Неверные аргументы", command)
                return
            self._set_variable(tokens[1], tokens[3])
        elif tokens[0] == "print":
            try:
                if len(tokens) == 2:
                    raise SyntacticException("Неверные аргументы", command)
                print(self._get_variable(tokens[1]))
            except NameError as e: print(e)
        elif tokens[0] == "exit": sys.exit(0)
        else: raise SyntacticException("Неизвестная команда", command)

    def _set_variable(self, var_name, value):
        if value.startswith('"') and value.endswith('"'):
            self.variables[var_name] = value[1:-1].replace("&_", "_").replace("_", " ")
        elif value.isdigit():
            self.variables[var_name] = int(value)
        else:
            self.variables[var_name] = self._get_variable(value)

    def _get_variable(self, var_name):
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise SyntacticException("Переменная не определена", var_name)