class Exp:
    pass
class IntLit(Exp):
    def __init__(self, value):
        self.value = value
    def eval(self):
        return self.value
    def printPrefix(self):
        return str(self.value)    

class FloatLit(Exp):
    def __init__(self, value):
        self.value = value
    def eval(self):
        return self.value
    def printPrefix(self):
        return str(self.value)

class BinExp(Exp):
    def __init__(self, first_operand, operator, second_operand):
        self.first_operand = first_operand
        self.operator = operator
        self.second_operand = second_operand
    def eval(self):
        if self.operator == '+':
            x = self.first_operand.eval() + self.second_operand.eval()
        elif self.operator == '-':
            x = self.first_operand.eval() - self.second_operand.eval()
        elif self.operator == '*':
            x = self.first_operand.eval() * self.second_operand.eval()
        elif self.operator == '/':
            x = self.first_operand.eval() / self.second_operand.eval()
        else:
            raise('Not registered operator')
        return x
    def printPrefix(self):
        return self.operator + ' ' + self.first_operand.printPrefix() + ' ' + self.second_operand.printPrefix()

class UnExp(Exp):
    def __init__(self, operator, first_operand):
        self.operator = operator
        self.first_operand = first_operand
    def eval(self):
        if self.operator == '+':
            x = self.first_operand.eval()
        elif self.operator == '-':
            x = self.first_operand.eval() * (-1)
        else:
            raise('Not registered operator')
        return x
    def printPrefix(self):
        return self.operator + '. ' + self.first_operand.printPrefix()


x1 = IntLit(1)

x2 = FloatLit(2.0)

x3 = BinExp(x1,"+",x1)

x4 = UnExp("-",x1)

x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))

print(x5.printPrefix())