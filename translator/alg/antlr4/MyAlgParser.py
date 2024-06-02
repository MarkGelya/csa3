# Generated from translator/alg/MyAlg.g4 by ANTLR 4.13.0
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
        4,1,45,209,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,4,0,46,8,0,11,0,12,0,47,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,59,8,1,1,2,1,2,1,3,5,3,64,8,3,10,3,12,3,67,9,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,3,4,87,8,4,1,5,1,5,3,5,91,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,3,11,128,
        8,11,1,11,1,11,1,12,1,12,1,12,5,12,135,8,12,10,12,12,12,138,9,12,
        1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,17,
        1,17,3,17,154,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,174,8,18,10,18,
        12,18,177,9,18,3,18,179,8,18,1,18,1,18,3,18,183,8,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,194,8,18,10,18,12,18,197,9,
        18,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,0,1,36,
        22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        0,5,1,0,18,20,2,0,16,17,23,23,1,0,16,17,1,0,10,15,1,0,24,25,213,
        0,45,1,0,0,0,2,58,1,0,0,0,4,60,1,0,0,0,6,65,1,0,0,0,8,86,1,0,0,0,
        10,88,1,0,0,0,12,92,1,0,0,0,14,98,1,0,0,0,16,110,1,0,0,0,18,116,
        1,0,0,0,20,121,1,0,0,0,22,124,1,0,0,0,24,131,1,0,0,0,26,139,1,0,
        0,0,28,141,1,0,0,0,30,145,1,0,0,0,32,148,1,0,0,0,34,153,1,0,0,0,
        36,182,1,0,0,0,38,198,1,0,0,0,40,200,1,0,0,0,42,203,1,0,0,0,44,46,
        3,8,4,0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,
        48,49,1,0,0,0,49,50,5,0,0,1,50,1,1,0,0,0,51,59,3,4,2,0,52,53,3,4,
        2,0,53,54,5,33,0,0,54,55,5,1,0,0,55,56,5,37,0,0,56,57,5,2,0,0,57,
        59,1,0,0,0,58,51,1,0,0,0,58,52,1,0,0,0,59,3,1,0,0,0,60,61,7,0,0,
        0,61,5,1,0,0,0,62,64,3,8,4,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,
        0,0,0,65,66,1,0,0,0,66,7,1,0,0,0,67,65,1,0,0,0,68,69,3,30,15,0,69,
        70,5,3,0,0,70,87,1,0,0,0,71,72,3,28,14,0,72,73,5,3,0,0,73,87,1,0,
        0,0,74,87,3,16,8,0,75,87,3,14,7,0,76,87,3,10,5,0,77,78,3,22,11,0,
        78,79,5,3,0,0,79,87,1,0,0,0,80,81,3,32,16,0,81,82,5,3,0,0,82,87,
        1,0,0,0,83,84,3,20,10,0,84,85,5,3,0,0,85,87,1,0,0,0,86,68,1,0,0,
        0,86,71,1,0,0,0,86,74,1,0,0,0,86,75,1,0,0,0,86,76,1,0,0,0,86,77,
        1,0,0,0,86,80,1,0,0,0,86,83,1,0,0,0,87,9,1,0,0,0,88,90,3,12,6,0,
        89,91,3,18,9,0,90,89,1,0,0,0,90,91,1,0,0,0,91,11,1,0,0,0,92,93,5,
        26,0,0,93,94,3,36,18,0,94,95,5,4,0,0,95,96,3,6,3,0,96,97,5,5,0,0,
        97,13,1,0,0,0,98,99,5,29,0,0,99,100,5,6,0,0,100,101,3,28,14,0,101,
        102,5,3,0,0,102,103,3,36,18,0,103,104,5,3,0,0,104,105,3,28,14,0,
        105,106,5,7,0,0,106,107,5,4,0,0,107,108,3,6,3,0,108,109,5,5,0,0,
        109,15,1,0,0,0,110,111,5,28,0,0,111,112,3,36,18,0,112,113,5,4,0,
        0,113,114,3,6,3,0,114,115,5,5,0,0,115,17,1,0,0,0,116,117,5,27,0,
        0,117,118,5,4,0,0,118,119,3,6,3,0,119,120,5,5,0,0,120,19,1,0,0,0,
        121,122,5,30,0,0,122,123,5,33,0,0,123,21,1,0,0,0,124,125,5,33,0,
        0,125,127,5,6,0,0,126,128,3,24,12,0,127,126,1,0,0,0,127,128,1,0,
        0,0,128,129,1,0,0,0,129,130,5,7,0,0,130,23,1,0,0,0,131,136,3,26,
        13,0,132,133,5,8,0,0,133,135,3,26,13,0,134,132,1,0,0,0,135,138,1,
        0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,25,1,0,0,0,138,136,1,0,
        0,0,139,140,5,33,0,0,140,27,1,0,0,0,141,142,3,34,17,0,142,143,5,
        9,0,0,143,144,3,36,18,0,144,29,1,0,0,0,145,146,3,2,1,0,146,147,3,
        28,14,0,147,31,1,0,0,0,148,149,5,33,0,0,149,150,5,34,0,0,150,33,
        1,0,0,0,151,154,3,38,19,0,152,154,3,42,21,0,153,151,1,0,0,0,153,
        152,1,0,0,0,154,35,1,0,0,0,155,156,6,18,-1,0,156,157,7,1,0,0,157,
        183,3,36,18,12,158,159,5,6,0,0,159,160,3,36,18,0,160,161,5,7,0,0,
        161,183,1,0,0,0,162,183,5,32,0,0,163,183,5,37,0,0,164,183,5,35,0,
        0,165,183,3,40,20,0,166,183,3,38,19,0,167,183,3,42,21,0,168,169,
        3,38,19,0,169,178,5,6,0,0,170,175,3,36,18,0,171,172,5,8,0,0,172,
        174,3,36,18,0,173,171,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,
        176,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,178,170,1,0,0,0,178,
        179,1,0,0,0,179,180,1,0,0,0,180,181,5,7,0,0,181,183,1,0,0,0,182,
        155,1,0,0,0,182,158,1,0,0,0,182,162,1,0,0,0,182,163,1,0,0,0,182,
        164,1,0,0,0,182,165,1,0,0,0,182,166,1,0,0,0,182,167,1,0,0,0,182,
        168,1,0,0,0,183,195,1,0,0,0,184,185,10,10,0,0,185,186,7,2,0,0,186,
        194,3,36,18,11,187,188,10,9,0,0,188,189,7,3,0,0,189,194,3,36,18,
        10,190,191,10,8,0,0,191,192,7,4,0,0,192,194,3,36,18,9,193,184,1,
        0,0,0,193,187,1,0,0,0,193,190,1,0,0,0,194,197,1,0,0,0,195,193,1,
        0,0,0,195,196,1,0,0,0,196,37,1,0,0,0,197,195,1,0,0,0,198,199,5,33,
        0,0,199,39,1,0,0,0,200,201,5,36,0,0,201,202,5,33,0,0,202,41,1,0,
        0,0,203,204,3,38,19,0,204,205,5,1,0,0,205,206,3,36,18,0,206,207,
        5,2,0,0,207,43,1,0,0,0,13,47,58,65,86,90,127,136,153,175,178,182,
        193,195
    ]

class MyAlgParser ( Parser ):

    grammarFileName = "MyAlg.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "';'", "'{'", "'}'", "'('", 
                     "')'", "','", "'='", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'+'", "'-'", "'int'", "'short'", "'byte'", 
                     "'void'", "'string'", "'~'", "'&'", "'|'", "'if'", 
                     "'else'", "'while'", "'for'", "'goto'", "'array'", 
                     "<INVALID>", "<INVALID>", "':'", "<INVALID>", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ASSIGN", "EQUAL", "NOTEQUAL", "LESS", 
                      "LESSEQ", "BIGGER", "BIGGEREQ", "PLUS", "MINUS", "INT", 
                      "SHORT", "BYTE", "VOID", "STRING", "NOT", "AND", "OR", 
                      "IF", "ELSE", "WHILE", "FOR", "GOTO", "ARRAY", "CHARVAL", 
                      "ID", "COLON", "BOOLVAL", "STAR", "INTVAL", "DEC_INTEGER", 
                      "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "STRINGVAL", 
                      "ESC_SEQ", "COMMENT", "WHITESPACE" ]

    RULE_program = 0
    RULE_type = 1
    RULE_type_basic = 2
    RULE_statements = 3
    RULE_statement = 4
    RULE_ifElseSt = 5
    RULE_ifSt = 6
    RULE_forSt = 7
    RULE_whileSt = 8
    RULE_elseSt = 9
    RULE_gotoSt = 10
    RULE_function = 11
    RULE_args = 12
    RULE_arg = 13
    RULE_assignSt = 14
    RULE_newVar = 15
    RULE_label = 16
    RULE_left_expr = 17
    RULE_expr = 18
    RULE_ident = 19
    RULE_pointer = 20
    RULE_array_access = 21

    ruleNames =  [ "program", "type", "type_basic", "statements", "statement", 
                   "ifElseSt", "ifSt", "forSt", "whileSt", "elseSt", "gotoSt", 
                   "function", "args", "arg", "assignSt", "newVar", "label", 
                   "left_expr", "expr", "ident", "pointer", "array_access" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ASSIGN=9
    EQUAL=10
    NOTEQUAL=11
    LESS=12
    LESSEQ=13
    BIGGER=14
    BIGGEREQ=15
    PLUS=16
    MINUS=17
    INT=18
    SHORT=19
    BYTE=20
    VOID=21
    STRING=22
    NOT=23
    AND=24
    OR=25
    IF=26
    ELSE=27
    WHILE=28
    FOR=29
    GOTO=30
    ARRAY=31
    CHARVAL=32
    ID=33
    COLON=34
    BOOLVAL=35
    STAR=36
    INTVAL=37
    DEC_INTEGER=38
    OCT_INTEGER=39
    HEX_INTEGER=40
    BIN_INTEGER=41
    STRINGVAL=42
    ESC_SEQ=43
    COMMENT=44
    WHITESPACE=45

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
            return self.getToken(MyAlgParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyAlgParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyAlgParser.StatementContext,i)


        def getRuleIndex(self):
            return MyAlgParser.RULE_program

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

        localctx = MyAlgParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.statement()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 10537926656) != 0)):
                    break

            self.state = 49
            self.match(MyAlgParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_basic(self):
            return self.getTypedRuleContext(MyAlgParser.Type_basicContext,0)


        def ID(self):
            return self.getToken(MyAlgParser.ID, 0)

        def INTVAL(self):
            return self.getToken(MyAlgParser.INTVAL, 0)

        def getRuleIndex(self):
            return MyAlgParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MyAlgParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.type_basic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.type_basic()
                self.state = 53
                self.match(MyAlgParser.ID)
                self.state = 54
                self.match(MyAlgParser.T__0)
                self.state = 55
                self.match(MyAlgParser.INTVAL)
                self.state = 56
                self.match(MyAlgParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_basicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MyAlgParser.INT, 0)

        def SHORT(self):
            return self.getToken(MyAlgParser.SHORT, 0)

        def BYTE(self):
            return self.getToken(MyAlgParser.BYTE, 0)

        def getRuleIndex(self):
            return MyAlgParser.RULE_type_basic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_basic" ):
                listener.enterType_basic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_basic" ):
                listener.exitType_basic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_basic" ):
                return visitor.visitType_basic(self)
            else:
                return visitor.visitChildren(self)




    def type_basic(self):

        localctx = MyAlgParser.Type_basicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type_basic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
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


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyAlgParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyAlgParser.StatementContext,i)


        def getRuleIndex(self):
            return MyAlgParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = MyAlgParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10537926656) != 0):
                self.state = 62
                self.statement()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newVar(self):
            return self.getTypedRuleContext(MyAlgParser.NewVarContext,0)


        def assignSt(self):
            return self.getTypedRuleContext(MyAlgParser.AssignStContext,0)


        def whileSt(self):
            return self.getTypedRuleContext(MyAlgParser.WhileStContext,0)


        def forSt(self):
            return self.getTypedRuleContext(MyAlgParser.ForStContext,0)


        def ifElseSt(self):
            return self.getTypedRuleContext(MyAlgParser.IfElseStContext,0)


        def function(self):
            return self.getTypedRuleContext(MyAlgParser.FunctionContext,0)


        def label(self):
            return self.getTypedRuleContext(MyAlgParser.LabelContext,0)


        def gotoSt(self):
            return self.getTypedRuleContext(MyAlgParser.GotoStContext,0)


        def getRuleIndex(self):
            return MyAlgParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MyAlgParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.newVar()
                self.state = 69
                self.match(MyAlgParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.assignSt()
                self.state = 72
                self.match(MyAlgParser.T__2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.whileSt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.forSt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.ifElseSt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 77
                self.function()
                self.state = 78
                self.match(MyAlgParser.T__2)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.label()
                self.state = 81
                self.match(MyAlgParser.T__2)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 83
                self.gotoSt()
                self.state = 84
                self.match(MyAlgParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseStContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifSt(self):
            return self.getTypedRuleContext(MyAlgParser.IfStContext,0)


        def elseSt(self):
            return self.getTypedRuleContext(MyAlgParser.ElseStContext,0)


        def getRuleIndex(self):
            return MyAlgParser.RULE_ifElseSt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElseSt" ):
                listener.enterIfElseSt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElseSt" ):
                listener.exitIfElseSt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseSt" ):
                return visitor.visitIfElseSt(self)
            else:
                return visitor.visitChildren(self)




    def ifElseSt(self):

        localctx = MyAlgParser.IfElseStContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifElseSt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.ifSt()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 89
                self.elseSt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MyAlgParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(MyAlgParser.ExprContext,0)


        def statements(self):
            return self.getTypedRuleContext(MyAlgParser.StatementsContext,0)


        def getRuleIndex(self):
            return MyAlgParser.RULE_ifSt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfSt" ):
                listener.enterIfSt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfSt" ):
                listener.exitIfSt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfSt" ):
                return visitor.visitIfSt(self)
            else:
                return visitor.visitChildren(self)




    def ifSt(self):

        localctx = MyAlgParser.IfStContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifSt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(MyAlgParser.IF)
            self.state = 93
            self.expr(0)
            self.state = 94
            self.match(MyAlgParser.T__3)
            self.state = 95
            self.statements()
            self.state = 96
            self.match(MyAlgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MyAlgParser.FOR, 0)

        def assignSt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyAlgParser.AssignStContext)
            else:
                return self.getTypedRuleContext(MyAlgParser.AssignStContext,i)


        def expr(self):
            return self.getTypedRuleContext(MyAlgParser.ExprContext,0)


        def statements(self):
            return self.getTypedRuleContext(MyAlgParser.StatementsContext,0)


        def getRuleIndex(self):
            return MyAlgParser.RULE_forSt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForSt" ):
                listener.enterForSt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForSt" ):
                listener.exitForSt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForSt" ):
                return visitor.visitForSt(self)
            else:
                return visitor.visitChildren(self)




    def forSt(self):

        localctx = MyAlgParser.ForStContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forSt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(MyAlgParser.FOR)
            self.state = 99
            self.match(MyAlgParser.T__5)
            self.state = 100
            self.assignSt()
            self.state = 101
            self.match(MyAlgParser.T__2)
            self.state = 102
            self.expr(0)
            self.state = 103
            self.match(MyAlgParser.T__2)
            self.state = 104
            self.assignSt()
            self.state = 105
            self.match(MyAlgParser.T__6)
            self.state = 106
            self.match(MyAlgParser.T__3)
            self.state = 107
            self.statements()
            self.state = 108
            self.match(MyAlgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MyAlgParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(MyAlgParser.ExprContext,0)


        def statements(self):
            return self.getTypedRuleContext(MyAlgParser.StatementsContext,0)


        def getRuleIndex(self):
            return MyAlgParser.RULE_whileSt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileSt" ):
                listener.enterWhileSt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileSt" ):
                listener.exitWhileSt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileSt" ):
                return visitor.visitWhileSt(self)
            else:
                return visitor.visitChildren(self)




    def whileSt(self):

        localctx = MyAlgParser.WhileStContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileSt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(MyAlgParser.WHILE)
            self.state = 111
            self.expr(0)
            self.state = 112
            self.match(MyAlgParser.T__3)
            self.state = 113
            self.statements()
            self.state = 114
            self.match(MyAlgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MyAlgParser.ELSE, 0)

        def statements(self):
            return self.getTypedRuleContext(MyAlgParser.StatementsContext,0)


        def getRuleIndex(self):
            return MyAlgParser.RULE_elseSt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseSt" ):
                listener.enterElseSt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseSt" ):
                listener.exitElseSt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseSt" ):
                return visitor.visitElseSt(self)
            else:
                return visitor.visitChildren(self)




    def elseSt(self):

        localctx = MyAlgParser.ElseStContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_elseSt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(MyAlgParser.ELSE)
            self.state = 117
            self.match(MyAlgParser.T__3)
            self.state = 118
            self.statements()
            self.state = 119
            self.match(MyAlgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoStContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOTO(self):
            return self.getToken(MyAlgParser.GOTO, 0)

        def ID(self):
            return self.getToken(MyAlgParser.ID, 0)

        def getRuleIndex(self):
            return MyAlgParser.RULE_gotoSt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotoSt" ):
                listener.enterGotoSt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotoSt" ):
                listener.exitGotoSt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotoSt" ):
                return visitor.visitGotoSt(self)
            else:
                return visitor.visitChildren(self)




    def gotoSt(self):

        localctx = MyAlgParser.GotoStContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_gotoSt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(MyAlgParser.GOTO)
            self.state = 122
            self.match(MyAlgParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyAlgParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(MyAlgParser.ArgsContext,0)


        def getRuleIndex(self):
            return MyAlgParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = MyAlgParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(MyAlgParser.ID)
            self.state = 125
            self.match(MyAlgParser.T__5)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 126
                self.args()


            self.state = 129
            self.match(MyAlgParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyAlgParser.ArgContext)
            else:
                return self.getTypedRuleContext(MyAlgParser.ArgContext,i)


        def getRuleIndex(self):
            return MyAlgParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = MyAlgParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.arg()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 132
                self.match(MyAlgParser.T__7)
                self.state = 133
                self.arg()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyAlgParser.ID, 0)

        def getRuleIndex(self):
            return MyAlgParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = MyAlgParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(MyAlgParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_expr(self):
            return self.getTypedRuleContext(MyAlgParser.Left_exprContext,0)


        def ASSIGN(self):
            return self.getToken(MyAlgParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MyAlgParser.ExprContext,0)


        def getRuleIndex(self):
            return MyAlgParser.RULE_assignSt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignSt" ):
                listener.enterAssignSt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignSt" ):
                listener.exitAssignSt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignSt" ):
                return visitor.visitAssignSt(self)
            else:
                return visitor.visitChildren(self)




    def assignSt(self):

        localctx = MyAlgParser.AssignStContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignSt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.left_expr()
            self.state = 142
            self.match(MyAlgParser.ASSIGN)
            self.state = 143
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MyAlgParser.TypeContext,0)


        def assignSt(self):
            return self.getTypedRuleContext(MyAlgParser.AssignStContext,0)


        def getRuleIndex(self):
            return MyAlgParser.RULE_newVar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewVar" ):
                listener.enterNewVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewVar" ):
                listener.exitNewVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewVar" ):
                return visitor.visitNewVar(self)
            else:
                return visitor.visitChildren(self)




    def newVar(self):

        localctx = MyAlgParser.NewVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_newVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.type_()
            self.state = 146
            self.assignSt()
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

        def ID(self):
            return self.getToken(MyAlgParser.ID, 0)

        def COLON(self):
            return self.getToken(MyAlgParser.COLON, 0)

        def getRuleIndex(self):
            return MyAlgParser.RULE_label

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

        localctx = MyAlgParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(MyAlgParser.ID)
            self.state = 149
            self.match(MyAlgParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(MyAlgParser.IdentContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MyAlgParser.Array_accessContext,0)


        def getRuleIndex(self):
            return MyAlgParser.RULE_left_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeft_expr" ):
                listener.enterLeft_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeft_expr" ):
                listener.exitLeft_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_expr" ):
                return visitor.visitLeft_expr(self)
            else:
                return visitor.visitChildren(self)




    def left_expr(self):

        localctx = MyAlgParser.Left_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_left_expr)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.ident()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.array_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyAlgParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyAlgParser.ExprContext,i)


        def NOT(self):
            return self.getToken(MyAlgParser.NOT, 0)

        def PLUS(self):
            return self.getToken(MyAlgParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MyAlgParser.MINUS, 0)

        def CHARVAL(self):
            return self.getToken(MyAlgParser.CHARVAL, 0)

        def INTVAL(self):
            return self.getToken(MyAlgParser.INTVAL, 0)

        def BOOLVAL(self):
            return self.getToken(MyAlgParser.BOOLVAL, 0)

        def pointer(self):
            return self.getTypedRuleContext(MyAlgParser.PointerContext,0)


        def ident(self):
            return self.getTypedRuleContext(MyAlgParser.IdentContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MyAlgParser.Array_accessContext,0)


        def EQUAL(self):
            return self.getToken(MyAlgParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(MyAlgParser.NOTEQUAL, 0)

        def LESS(self):
            return self.getToken(MyAlgParser.LESS, 0)

        def LESSEQ(self):
            return self.getToken(MyAlgParser.LESSEQ, 0)

        def BIGGER(self):
            return self.getToken(MyAlgParser.BIGGER, 0)

        def BIGGEREQ(self):
            return self.getToken(MyAlgParser.BIGGEREQ, 0)

        def AND(self):
            return self.getToken(MyAlgParser.AND, 0)

        def OR(self):
            return self.getToken(MyAlgParser.OR, 0)

        def getRuleIndex(self):
            return MyAlgParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyAlgParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 156
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8585216) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 157
                self.expr(12)
                pass

            elif la_ == 2:
                self.state = 158
                self.match(MyAlgParser.T__5)
                self.state = 159
                self.expr(0)
                self.state = 160
                self.match(MyAlgParser.T__6)
                pass

            elif la_ == 3:
                self.state = 162
                self.match(MyAlgParser.CHARVAL)
                pass

            elif la_ == 4:
                self.state = 163
                self.match(MyAlgParser.INTVAL)
                pass

            elif la_ == 5:
                self.state = 164
                self.match(MyAlgParser.BOOLVAL)
                pass

            elif la_ == 6:
                self.state = 165
                self.pointer()
                pass

            elif la_ == 7:
                self.state = 166
                self.ident()
                pass

            elif la_ == 8:
                self.state = 167
                self.array_access()
                pass

            elif la_ == 9:
                self.state = 168
                self.ident()
                self.state = 169
                self.match(MyAlgParser.T__5)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 253411655744) != 0):
                    self.state = 170
                    self.expr(0)
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==8:
                        self.state = 171
                        self.match(MyAlgParser.T__7)
                        self.state = 172
                        self.expr(0)
                        self.state = 177
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 180
                self.match(MyAlgParser.T__6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 193
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = MyAlgParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 184
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 185
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 186
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = MyAlgParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 187
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 188
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 189
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = MyAlgParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 190
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 191
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 192
                        self.expr(9)
                        pass

             
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyAlgParser.ID, 0)

        def getRuleIndex(self):
            return MyAlgParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)




    def ident(self):

        localctx = MyAlgParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ident)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(MyAlgParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(MyAlgParser.STAR, 0)

        def ID(self):
            return self.getToken(MyAlgParser.ID, 0)

        def getRuleIndex(self):
            return MyAlgParser.RULE_pointer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointer" ):
                listener.enterPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointer" ):
                listener.exitPointer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointer" ):
                return visitor.visitPointer(self)
            else:
                return visitor.visitChildren(self)




    def pointer(self):

        localctx = MyAlgParser.PointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_pointer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MyAlgParser.STAR)
            self.state = 201
            self.match(MyAlgParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(MyAlgParser.IdentContext,0)


        def expr(self):
            return self.getTypedRuleContext(MyAlgParser.ExprContext,0)


        def getRuleIndex(self):
            return MyAlgParser.RULE_array_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_access" ):
                listener.enterArray_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_access" ):
                listener.exitArray_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




    def array_access(self):

        localctx = MyAlgParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.ident()
            self.state = 204
            self.match(MyAlgParser.T__0)
            self.state = 205
            self.expr(0)
            self.state = 206
            self.match(MyAlgParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         




