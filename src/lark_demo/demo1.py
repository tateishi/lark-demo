from functools import reduce

from fire import Fire
from lark import Lark, Transformer


class CalcTransformer(Transformer):
    def expr(self, tree):
        print(f"expr={tree}")
        if tree[1]:
            return reduce(lambda x, y: x + y, tree)
        else:
            return tree[0]

    def term(self, tree):
        print(f"term={tree}")
        if tree[1]:
            return reduce(lambda x, y: x * y, tree)
        else:
            return tree[0]

    def factor(self, tree):
        print(f"factor={tree}")
        return tree[0]

    def number(self, tree):
        print(f'number={tree}')
        return int(tree[0])


def calc(text: str) -> None:
    from importlib.resources import files
    path = files("lark_demo") / "grammar/calc.lark"
    print(path)
    grammar = path.read_text(encoding="utf-8")
    print(grammar)
    print(text)

#    with open(path, encoding="utf-8") as grammar:
    parser = Lark(grammar, start="expr")
    print(parser)
    tree = parser.parse(text)
    print(tree)
    result = CalcTransformer().transform(tree)
    print(result)


def main():
    Fire(calc)
