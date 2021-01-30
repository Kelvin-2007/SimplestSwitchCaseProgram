_D = None
_d = False

def Switch(Data):
    global _D
    global _d
    _D = Data
    _d = False

def Case(Arguments, Function, FunctionArguments: tuple):
    global _D
    global _d
    if Arguments == _D and not _d:
        Function(*FunctionArguments)
        _d = True