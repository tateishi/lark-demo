from pathlib import Path

from fire import Fire
from lark import Lark

def hdparam(file: str) -> None:
    from importlib.resources import files

    syntax = files("lark_demo") / "grammar/hdparam.lark"
    grammar = syntax.read_text(encoding="utf-8")

    text = Path(file).read_text(encoding="utf-8")
#    print(text)

    parser = Lark(grammar, start="hdparam")
    tree = parser.parse(text)
    print(tree)


def main():
    Fire(hdparam)
