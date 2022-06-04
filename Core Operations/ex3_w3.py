class Exp:
    pass
class BinExp(Exp):
    def __init__(self,o1,op,o2):
        self.left = o1
        self.op = op
        self.right = o2
class UnExp(Exp): 
    def __init__(self,op,o1):
        self.op = op
        self.operand = o1
class IntLit(Exp):
    def __init__(self,v):
        self.value = v
class FloatLit(Exp):
    def __init__(self,v):
        self.value = v

class Eval:
    def visit(self, ex):
        if isinstance(ex, IntLit) or isinstance(ex, FloatLit):
            return ex.value
        elif isinstance(ex, UnExp):
            if ex.op == '-': return self.visit(ex.operand) * (-1)
            elif ex.op == '+': return self.visit(ex.operand)
            else:
                raise('Not registered operator')
        elif isinstance(ex, BinExp):
            if ex.op == '+': return self.visit(ex.left) + self.visit(ex.right)
            elif ex.op == '-': return self.visit(ex.left) - self.visit(ex.right)
            elif ex.op == '*': return self.visit(ex.left) * self.visit(ex.right)
            elif ex.op == '/': return self.visit(ex.left) / self.visit(ex.right)
            else:
                raise('Not registered operator')

class PrintPrefix:
    def visit(self, ex):
        if isinstance(ex, IntLit) or isinstance(ex, FloatLit):
            return str(ex.value)
        elif isinstance(ex, UnExp):
            return ex.op + '. ' + self.visit(ex.operand)
        elif isinstance(ex, BinExp):
            return ex.op + ' ' + self.visit(ex.left) + ' ' + self.visit(ex.right)

class PrintPostfix:
    def visit(self, ex):
        if isinstance(ex, IntLit) or isinstance(ex, FloatLit):
            return str(ex.value)
        elif isinstance(ex, UnExp):
            return  self.visit(ex.operand) + ' ' + ex.op + '.'
        elif isinstance(ex, BinExp):
            return self.visit(ex.left) + ' ' + self.visit(ex.right) + ' ' + ex.op

x1 = IntLit(1)
x2 = FloatLit(2.0)
x3 = BinExp(x1,"+",x1)
x4 = UnExp("-",x1)
x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))

v1  = Eval()
print(v1.visit(x5))
v2 = PrintPrefix()
print(v2.visit(x5))
v3 = PrintPostfix()
print(v3.visit(x5))