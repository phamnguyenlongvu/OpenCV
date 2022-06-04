from abc import ABC, abstractmethod


class Exp(ABC):
    @abstractmethod
    def accept(self): pass


class BinExp(Exp):
    def __init__(self, o1, op, o2):
        self.left = o1
        self.op = op
        self.right = o2

    def accept(self, v):
        return v.visitBinExp(self)


class UnExp(Exp):
    def __init__(self, op, o1):
        self.op = op
        self.operand = o1

    def accept(self, v):
        return v.visitUnExp(self)


class IntLit(Exp):
    def __init__(self, v):
        self.value = v

    def accept(self, v):
        return v.visitIntLit(self)


class FloatLit(Exp):
    def __init__(self, v):
        self.value = v

    def accept(self, v):
        return v.visitFloatLit(self)


class Visitor(ABC):  # interface
    def visitBinExp(self, binexp): pass

    def visitUnExp(self, unexp): pass

    def visitFloatLit(self, floatlit): pass

    def visitIntLit(self, intlit): pass


class Eval(Visitor):
    def visit(self, x):
        return x.accept(self)

    def visitBinExp(self, x):
        e1 = self.visit(x.left)
        e2 = self.visit(x.right)
        if x.op == '+':
            return e1 + e2
        elif x.op == '-':
            return e1 - e2
        elif x.op == '*':
            return e1 * e2
        elif x.op == '/':
            return e1 / e2

    def visitUnExp(self, x):
        e = self.visit(x.operand)
        if x.op == '-':
            return -e
        else:
            return e

    def visitIntLit(self, x):
        return x.value

    def visitFloatLit(self, x):
        return x.value

class PrintPrefix(Visitor):
    def visit(self, x):
        return x.accept(self)

    def visitBinExp(self, x):
        e1 = self.visit(x.left)
        e2 = self.visit(x.right)
        return f"{x.op} {e1} {e2}"

    def visitUnExp(self, x):
        e = self.visit(x.operand)
        return f"{x.op}. {e}"

    def visitIntLit(self, x):
        return f"{x.value}"

    def visitFloatLit(self, x):
        return f"{x.value}"


class PrintPostfix(Visitor):
    def visit(self, x):
        return x.accept(self)

    def visitBinExp(self, x):
        e1 = self.visit(x.left)
        e2 = self.visit(x.right)
        return f"{e1} {e2} {x.op}"

    def visitUnExp(self, x):
        e = self.visit(x.operand)
        return f"{e} {x.op}."

    def visitIntLit(self, x):
        return f"{x.value}"

    def visitFloatLit(self, x):
        return f"{x.value}"

x1 = IntLit(1)
x2 = FloatLit(2.0)
x3 = BinExp(x1,"+",x1)
x4 = UnExp("-",x1)
x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))

v1 = Eval()
v2 = PrintPrefix()
v3 = PrintPostfix()

exps = [x1, x2, x3, x4, x5]
for exp in exps:
    print(v1.visit(exp))
    print(v2.visit(exp))
    print(v3.visit(exp))