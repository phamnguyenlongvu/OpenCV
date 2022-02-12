
class exp:
    def __init__(self, op, left, right) -> None:
        self.op=op
        self.left=left
        self.right=right
    def __add__(self, left, right):
        return left+right

x= exp('+', 3, 4)
print(x)