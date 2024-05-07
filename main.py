from antlr4 import *
from translator.antlr4.MyAssemblerLexer import MyAssemblerLexer
from translator.antlr4.MyAssemblerParser import MyAssemblerParser

from translator.VisitorInterp import VisitorInterp
from translator.Code import Code

def main():
    input_stream = FileStream('tests/main2.asm')
    lexer = MyAssemblerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyAssemblerParser(stream)
    tree = parser.program()
    code = Code()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = VisitorInterp(code)
        vinterp.visit(tree)
    code.eof()
    code.print()

if __name__ == '__main__':
    main()
