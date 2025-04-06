import tokenize
from io import BytesIO
import ast
code = "x = y + 2"

tokens = tokenize.tokenize(BytesIO(code.encode('utf-8')).readline)

for token in tokens:
    print(token)
def generate_assembly(node):
    if isinstance(node, ast.Assign):
        target = node.targets[0].id
        value = node.value
        if isinstance(value, ast.BinOp):
            left = value.left.id
            right = value.right.n
            return [
                f"MOV R1, {left}",   # load y
                f"ADD R1, {right}",  # add 2
                f"MOV {target}, R1"  # store in x
            ]
    return []

code = "x = y + 2"
tree = ast.parse(code)
instructions = generate_assembly(tree.body[0])

for instr in instructions:
    print(instr)
