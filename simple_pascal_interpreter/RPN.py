from spi import Lexer, Parser, NodeVisitor

class Translator(NodeVisitor):
    def __init__(self, tree):
        self.tree = tree

    def visit_BinOp(self, node):
        left_val = self.visit(node.left)
        right_vla = self.visit(node.right)
        return '{left} {right} {op}'.format(
            left = left_val,
            right = right_vla,
            op = node.op.value,
        )

    def visit_Num(self, node):
        return node.value

    def translate(self):
        return self.visit(tree)

text = input('> ')
lexer = Lexer(text)
parser = Parser(lexer)

tree = parser.parse()
translator = Translator(tree)
print(translator.translate())