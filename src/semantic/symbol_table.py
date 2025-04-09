class Symbol:
    def __init__(self, name, type_, decl=None):
        self.name = name
        self.type_ = type_
        self.decl = decl

    def __repr__(self):
        return f"Symbol(name={self.name}, type_={self.type_})"


class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def define(self, name, type_, decl=None):
        self.symbols[name] = Symbol(name, type_, decl)

    def lookup(self, name):

        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.lookup(name)
        else:
            return None

    def lookup_local(self, name):

        return self.symbols.get(name)
