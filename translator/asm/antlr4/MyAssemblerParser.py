# Generated from translator/asm/MyAssembler.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,103,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        3,1,42,8,1,1,1,3,1,45,8,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,5,
        4,56,8,4,10,4,12,4,59,9,4,1,5,1,5,1,5,1,5,3,5,65,8,5,1,6,1,6,1,7,
        1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,81,8,10,1,
        11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,5,
        15,96,8,15,10,15,12,15,99,9,15,1,15,1,15,1,15,0,0,16,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,0,6,1,0,2,5,1,0,6,24,1,0,25,26,1,0,
        27,30,2,0,39,39,42,44,1,0,31,32,100,0,35,1,0,0,0,2,41,1,0,0,0,4,
        48,1,0,0,0,6,51,1,0,0,0,8,53,1,0,0,0,10,64,1,0,0,0,12,66,1,0,0,0,
        14,68,1,0,0,0,16,70,1,0,0,0,18,72,1,0,0,0,20,80,1,0,0,0,22,82,1,
        0,0,0,24,85,1,0,0,0,26,88,1,0,0,0,28,90,1,0,0,0,30,92,1,0,0,0,32,
        34,3,2,1,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,
        0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,0,0,1,39,1,1,0,0,0,40,42,3,
        4,2,0,41,40,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,45,3,8,4,0,44,
        43,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,47,5,36,0,0,47,3,1,0,0,
        0,48,49,3,6,3,0,49,50,5,33,0,0,50,5,1,0,0,0,51,52,5,34,0,0,52,7,
        1,0,0,0,53,57,3,10,5,0,54,56,3,20,10,0,55,54,1,0,0,0,56,59,1,0,0,
        0,57,55,1,0,0,0,57,58,1,0,0,0,58,9,1,0,0,0,59,57,1,0,0,0,60,65,3,
        12,6,0,61,65,3,14,7,0,62,65,3,16,8,0,63,65,3,18,9,0,64,60,1,0,0,
        0,64,61,1,0,0,0,64,62,1,0,0,0,64,63,1,0,0,0,65,11,1,0,0,0,66,67,
        5,1,0,0,67,13,1,0,0,0,68,69,7,0,0,0,69,15,1,0,0,0,70,71,7,1,0,0,
        71,17,1,0,0,0,72,73,7,2,0,0,73,19,1,0,0,0,74,81,3,28,14,0,75,81,
        3,6,3,0,76,81,3,22,11,0,77,81,3,24,12,0,78,81,3,26,13,0,79,81,3,
        30,15,0,80,74,1,0,0,0,80,75,1,0,0,0,80,76,1,0,0,0,80,77,1,0,0,0,
        80,78,1,0,0,0,80,79,1,0,0,0,81,21,1,0,0,0,82,83,5,41,0,0,83,84,3,
        28,14,0,84,23,1,0,0,0,85,86,5,41,0,0,86,87,3,6,3,0,87,25,1,0,0,0,
        88,89,7,3,0,0,89,27,1,0,0,0,90,91,7,4,0,0,91,29,1,0,0,0,92,97,5,
        31,0,0,93,96,5,38,0,0,94,96,8,5,0,0,95,93,1,0,0,0,95,94,1,0,0,0,
        96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,
        0,0,0,100,101,5,31,0,0,101,31,1,0,0,0,8,35,41,44,57,64,80,95,97
    ]

class MyAssemblerParser ( Parser ):

    grammarFileName = "MyAssembler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'HLT'", "'WORD'", "'SHORT'", "'BYTE'", 
                     "'BYTES'", "'LD'", "'ST'", "'ADD'", "'SUB'", "'INC'", 
                     "'DEC'", "'OR'", "'AND'", "'XOR'", "'CMP'", "'JMP'", 
                     "'JE'", "'JZ'", "'JNE'", "'JNZ'", "'JG'", "'JGE'", 
                     "'JL'", "'JLE'", "'IN'", "'OUT'", "'b8'", "'b16'", 
                     "'b24'", "'b32'", "'\"'", "'\\'", "':'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COLON", "NAME", "COMMENT", "EOL", "WHITESPACE", 
                      "ESCAPED_CHAR", "DEC_INTEGER", "SIGN", "STAR", "OCT_INTEGER", 
                      "HEX_INTEGER", "BIN_INTEGER" ]

    RULE_program = 0
    RULE_line = 1
    RULE_label = 2
    RULE_name = 3
    RULE_instruction = 4
    RULE_op = 5
    RULE_op0 = 6
    RULE_op1 = 7
    RULE_op2 = 8
    RULE_op3 = 9
    RULE_operand = 10
    RULE_final_addr = 11
    RULE_final_addr_label = 12
    RULE_bit_depth = 13
    RULE_integer = 14
    RULE_string = 15

    ruleNames =  [ "program", "line", "label", "name", "instruction", "op", 
                   "op0", "op1", "op2", "op3", "operand", "final_addr", 
                   "final_addr_label", "bit_depth", "integer", "string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    COLON=33
    NAME=34
    COMMENT=35
    EOL=36
    WHITESPACE=37
    ESCAPED_CHAR=38
    DEC_INTEGER=39
    SIGN=40
    STAR=41
    OCT_INTEGER=42
    HEX_INTEGER=43
    BIN_INTEGER=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MyAssemblerParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyAssemblerParser.LineContext)
            else:
                return self.getTypedRuleContext(MyAssemblerParser.LineContext,i)


        def getRuleIndex(self):
            return MyAssemblerParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MyAssemblerParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 86033563646) != 0):
                self.state = 32
                self.line()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(MyAssemblerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOL(self):
            return self.getToken(MyAssemblerParser.EOL, 0)

        def label(self):
            return self.getTypedRuleContext(MyAssemblerParser.LabelContext,0)


        def instruction(self):
            return self.getTypedRuleContext(MyAssemblerParser.InstructionContext,0)


        def getRuleIndex(self):
            return MyAssemblerParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = MyAssemblerParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 40
                self.label()


            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 134217726) != 0):
                self.state = 43
                self.instruction()


            self.state = 46
            self.match(MyAssemblerParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(MyAssemblerParser.NameContext,0)


        def COLON(self):
            return self.getToken(MyAssemblerParser.COLON, 0)

        def getRuleIndex(self):
            return MyAssemblerParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = MyAssemblerParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.name()
            self.state = 49
            self.match(MyAssemblerParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(MyAssemblerParser.NAME, 0)

        def getRuleIndex(self):
            return MyAssemblerParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = MyAssemblerParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MyAssemblerParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self):
            return self.getTypedRuleContext(MyAssemblerParser.OpContext,0)


        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyAssemblerParser.OperandContext)
            else:
                return self.getTypedRuleContext(MyAssemblerParser.OperandContext,i)


        def getRuleIndex(self):
            return MyAssemblerParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = MyAssemblerParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.op()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33556445265920) != 0):
                self.state = 54
                self.operand()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op0(self):
            return self.getTypedRuleContext(MyAssemblerParser.Op0Context,0)


        def op1(self):
            return self.getTypedRuleContext(MyAssemblerParser.Op1Context,0)


        def op2(self):
            return self.getTypedRuleContext(MyAssemblerParser.Op2Context,0)


        def op3(self):
            return self.getTypedRuleContext(MyAssemblerParser.Op3Context,0)


        def getRuleIndex(self):
            return MyAssemblerParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = MyAssemblerParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_op)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.op0()
                pass
            elif token in [2, 3, 4, 5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.op1()
                pass
            elif token in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.op2()
                pass
            elif token in [25, 26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.op3()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyAssemblerParser.RULE_op0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp0" ):
                listener.enterOp0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp0" ):
                listener.exitOp0(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp0" ):
                return visitor.visitOp0(self)
            else:
                return visitor.visitChildren(self)




    def op0(self):

        localctx = MyAssemblerParser.Op0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_op0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(MyAssemblerParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyAssemblerParser.RULE_op1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp1" ):
                listener.enterOp1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp1" ):
                listener.exitOp1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp1" ):
                return visitor.visitOp1(self)
            else:
                return visitor.visitChildren(self)




    def op1(self):

        localctx = MyAssemblerParser.Op1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_op1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyAssemblerParser.RULE_op2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp2" ):
                listener.enterOp2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp2" ):
                listener.exitOp2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp2" ):
                return visitor.visitOp2(self)
            else:
                return visitor.visitChildren(self)




    def op2(self):

        localctx = MyAssemblerParser.Op2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_op2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33554368) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyAssemblerParser.RULE_op3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp3" ):
                listener.enterOp3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp3" ):
                listener.exitOp3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp3" ):
                return visitor.visitOp3(self)
            else:
                return visitor.visitChildren(self)




    def op3(self):

        localctx = MyAssemblerParser.Op3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_op3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not(_la==25 or _la==26):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer(self):
            return self.getTypedRuleContext(MyAssemblerParser.IntegerContext,0)


        def name(self):
            return self.getTypedRuleContext(MyAssemblerParser.NameContext,0)


        def final_addr(self):
            return self.getTypedRuleContext(MyAssemblerParser.Final_addrContext,0)


        def final_addr_label(self):
            return self.getTypedRuleContext(MyAssemblerParser.Final_addr_labelContext,0)


        def bit_depth(self):
            return self.getTypedRuleContext(MyAssemblerParser.Bit_depthContext,0)


        def string(self):
            return self.getTypedRuleContext(MyAssemblerParser.StringContext,0)


        def getRuleIndex(self):
            return MyAssemblerParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MyAssemblerParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operand)
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.integer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.name()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.final_addr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.final_addr_label()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.bit_depth()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.string()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Final_addrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(MyAssemblerParser.STAR, 0)

        def integer(self):
            return self.getTypedRuleContext(MyAssemblerParser.IntegerContext,0)


        def getRuleIndex(self):
            return MyAssemblerParser.RULE_final_addr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinal_addr" ):
                listener.enterFinal_addr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinal_addr" ):
                listener.exitFinal_addr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinal_addr" ):
                return visitor.visitFinal_addr(self)
            else:
                return visitor.visitChildren(self)




    def final_addr(self):

        localctx = MyAssemblerParser.Final_addrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_final_addr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MyAssemblerParser.STAR)
            self.state = 83
            self.integer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Final_addr_labelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(MyAssemblerParser.STAR, 0)

        def name(self):
            return self.getTypedRuleContext(MyAssemblerParser.NameContext,0)


        def getRuleIndex(self):
            return MyAssemblerParser.RULE_final_addr_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinal_addr_label" ):
                listener.enterFinal_addr_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinal_addr_label" ):
                listener.exitFinal_addr_label(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinal_addr_label" ):
                return visitor.visitFinal_addr_label(self)
            else:
                return visitor.visitChildren(self)




    def final_addr_label(self):

        localctx = MyAssemblerParser.Final_addr_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_final_addr_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(MyAssemblerParser.STAR)
            self.state = 86
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bit_depthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyAssemblerParser.RULE_bit_depth

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBit_depth" ):
                listener.enterBit_depth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBit_depth" ):
                listener.exitBit_depth(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBit_depth" ):
                return visitor.visitBit_depth(self)
            else:
                return visitor.visitChildren(self)




    def bit_depth(self):

        localctx = MyAssemblerParser.Bit_depthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_bit_depth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2013265920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC_INTEGER(self):
            return self.getToken(MyAssemblerParser.DEC_INTEGER, 0)

        def HEX_INTEGER(self):
            return self.getToken(MyAssemblerParser.HEX_INTEGER, 0)

        def OCT_INTEGER(self):
            return self.getToken(MyAssemblerParser.OCT_INTEGER, 0)

        def BIN_INTEGER(self):
            return self.getToken(MyAssemblerParser.BIN_INTEGER, 0)

        def getRuleIndex(self):
            return MyAssemblerParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = MyAssemblerParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31336081391616) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCAPED_CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(MyAssemblerParser.ESCAPED_CHAR)
            else:
                return self.getToken(MyAssemblerParser.ESCAPED_CHAR, i)

        def getRuleIndex(self):
            return MyAssemblerParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = MyAssemblerParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(MyAssemblerParser.T__30)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35177929637886) != 0):
                self.state = 95
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 93
                    self.match(MyAssemblerParser.ESCAPED_CHAR)
                    pass

                elif la_ == 2:
                    self.state = 94
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==31 or _la==32:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass


                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(MyAssemblerParser.T__30)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





