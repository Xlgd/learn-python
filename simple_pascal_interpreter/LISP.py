from spi import Lexer, Parser, NodeVisitor

class Translator(NodeVisitor):
    def __init__(self, tree):
        self.tree = tree
    
    def visit_BinOp(self, node):
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)
        return '({op} {left} {right})'.format(
            op = node.op.value,
            left = left_val,
            right = right_val,
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