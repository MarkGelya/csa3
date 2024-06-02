import sys

from antlr4 import *
from translator.asm.antlr4.MyAssemblerLexer import MyAssemblerLexer
from translator.asm.antlr4.MyAssemblerParser import MyAssemblerParser
from translator.asm.VisitorInterp import VisitorInterp
from translator.asm.Code import Code

# from translator.alg.antlr4.MyAlgLexer import MyAlgLexer
# from translator.alg.antlr4.MyAlgParser import MyAlgParser
# from translator.alg.antlr4.MyAlgVisitor import MyAlgVisitor
# from translator.alg.Code import Code


def main(input_filename: str, output_filename: str):
    # asm
    input_stream = FileStream(input_filename)
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
    code.compile(output_filename)
    if '-p' in sys.argv:
        code.print()

    # # alg
    # input_stream = FileStream(sys.argv[1])
    # lexer = MyAlgLexer(input_stream)
    # stream = CommonTokenStream(lexer)
    # parser = MyAlgParser(stream)
    # tree = parser.program()
    # # code = Code()
    # if parser.getNumberOfSyntaxErrors() > 0:
    #     print("syntax errors")
    # else:
    #     vinterp = MyAlgVisitor()
    #     vinterp.visit(tree)
    # # code.eof()
    # # code.compile(sys.argv[2] if sys.argv[2] else sys.argv[1] + '.bin')
    # # if '-p' in sys.argv:
    # #     code.print()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
