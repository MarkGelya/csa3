# Generated from translator/asm/MyAssembler.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,44,280,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,1,0,1,0,1,0,
        1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,
        1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,
        18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,
        22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,
        25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,
        29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,32,1,32,5,32,216,8,
        32,10,32,12,32,219,9,32,1,33,1,33,5,33,223,8,33,10,33,12,33,226,
        9,33,1,33,1,33,1,34,4,34,231,8,34,11,34,12,34,232,1,35,1,35,1,35,
        1,35,1,36,1,36,1,36,4,36,242,8,36,11,36,12,36,243,1,36,1,36,1,37,
        1,37,1,37,1,38,4,38,252,8,38,11,38,12,38,253,1,39,1,39,1,40,1,40,
        1,41,1,41,1,41,4,41,263,8,41,11,41,12,41,264,1,42,1,42,1,42,4,42,
        270,8,42,11,42,12,42,271,1,43,1,43,1,43,4,43,277,8,43,11,43,12,43,
        278,0,0,44,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,
        23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,
        34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,1,
        0,14,2,0,65,90,97,122,3,0,48,57,65,90,97,122,2,0,10,10,13,13,2,0,
        9,9,32,32,4,0,10,10,13,13,34,34,92,92,5,0,34,34,92,92,110,110,114,
        114,116,116,1,0,48,57,2,0,43,43,45,45,2,0,111,111,113,113,1,0,48,
        55,2,0,104,104,120,120,2,0,48,57,65,70,1,0,98,98,1,0,48,49,288,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,
        0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,
        0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,
        0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,
        0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,
        0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,
        0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,1,89,1,0,0,0,3,93,1,
        0,0,0,5,98,1,0,0,0,7,104,1,0,0,0,9,109,1,0,0,0,11,115,1,0,0,0,13,
        118,1,0,0,0,15,121,1,0,0,0,17,125,1,0,0,0,19,129,1,0,0,0,21,133,
        1,0,0,0,23,137,1,0,0,0,25,140,1,0,0,0,27,144,1,0,0,0,29,148,1,0,
        0,0,31,152,1,0,0,0,33,156,1,0,0,0,35,159,1,0,0,0,37,162,1,0,0,0,
        39,166,1,0,0,0,41,170,1,0,0,0,43,173,1,0,0,0,45,177,1,0,0,0,47,180,
        1,0,0,0,49,184,1,0,0,0,51,189,1,0,0,0,53,192,1,0,0,0,55,196,1,0,
        0,0,57,199,1,0,0,0,59,203,1,0,0,0,61,207,1,0,0,0,63,211,1,0,0,0,
        65,213,1,0,0,0,67,220,1,0,0,0,69,230,1,0,0,0,71,234,1,0,0,0,73,238,
        1,0,0,0,75,247,1,0,0,0,77,251,1,0,0,0,79,255,1,0,0,0,81,257,1,0,
        0,0,83,259,1,0,0,0,85,266,1,0,0,0,87,273,1,0,0,0,89,90,5,72,0,0,
        90,91,5,76,0,0,91,92,5,84,0,0,92,2,1,0,0,0,93,94,5,87,0,0,94,95,
        5,79,0,0,95,96,5,82,0,0,96,97,5,68,0,0,97,4,1,0,0,0,98,99,5,83,0,
        0,99,100,5,72,0,0,100,101,5,79,0,0,101,102,5,82,0,0,102,103,5,84,
        0,0,103,6,1,0,0,0,104,105,5,66,0,0,105,106,5,89,0,0,106,107,5,84,
        0,0,107,108,5,69,0,0,108,8,1,0,0,0,109,110,5,66,0,0,110,111,5,89,
        0,0,111,112,5,84,0,0,112,113,5,69,0,0,113,114,5,83,0,0,114,10,1,
        0,0,0,115,116,5,76,0,0,116,117,5,68,0,0,117,12,1,0,0,0,118,119,5,
        83,0,0,119,120,5,84,0,0,120,14,1,0,0,0,121,122,5,65,0,0,122,123,
        5,68,0,0,123,124,5,68,0,0,124,16,1,0,0,0,125,126,5,83,0,0,126,127,
        5,85,0,0,127,128,5,66,0,0,128,18,1,0,0,0,129,130,5,73,0,0,130,131,
        5,78,0,0,131,132,5,67,0,0,132,20,1,0,0,0,133,134,5,68,0,0,134,135,
        5,69,0,0,135,136,5,67,0,0,136,22,1,0,0,0,137,138,5,79,0,0,138,139,
        5,82,0,0,139,24,1,0,0,0,140,141,5,65,0,0,141,142,5,78,0,0,142,143,
        5,68,0,0,143,26,1,0,0,0,144,145,5,88,0,0,145,146,5,79,0,0,146,147,
        5,82,0,0,147,28,1,0,0,0,148,149,5,67,0,0,149,150,5,77,0,0,150,151,
        5,80,0,0,151,30,1,0,0,0,152,153,5,74,0,0,153,154,5,77,0,0,154,155,
        5,80,0,0,155,32,1,0,0,0,156,157,5,74,0,0,157,158,5,69,0,0,158,34,
        1,0,0,0,159,160,5,74,0,0,160,161,5,90,0,0,161,36,1,0,0,0,162,163,
        5,74,0,0,163,164,5,78,0,0,164,165,5,69,0,0,165,38,1,0,0,0,166,167,
        5,74,0,0,167,168,5,78,0,0,168,169,5,90,0,0,169,40,1,0,0,0,170,171,
        5,74,0,0,171,172,5,71,0,0,172,42,1,0,0,0,173,174,5,74,0,0,174,175,
        5,71,0,0,175,176,5,69,0,0,176,44,1,0,0,0,177,178,5,74,0,0,178,179,
        5,76,0,0,179,46,1,0,0,0,180,181,5,74,0,0,181,182,5,76,0,0,182,183,
        5,69,0,0,183,48,1,0,0,0,184,185,5,74,0,0,185,186,5,69,0,0,186,187,
        5,79,0,0,187,188,5,70,0,0,188,50,1,0,0,0,189,190,5,73,0,0,190,191,
        5,78,0,0,191,52,1,0,0,0,192,193,5,79,0,0,193,194,5,85,0,0,194,195,
        5,84,0,0,195,54,1,0,0,0,196,197,5,98,0,0,197,198,5,56,0,0,198,56,
        1,0,0,0,199,200,5,98,0,0,200,201,5,49,0,0,201,202,5,54,0,0,202,58,
        1,0,0,0,203,204,5,98,0,0,204,205,5,50,0,0,205,206,5,52,0,0,206,60,
        1,0,0,0,207,208,5,98,0,0,208,209,5,51,0,0,209,210,5,50,0,0,210,62,
        1,0,0,0,211,212,5,58,0,0,212,64,1,0,0,0,213,217,7,0,0,0,214,216,
        7,1,0,0,215,214,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,
        1,0,0,0,218,66,1,0,0,0,219,217,1,0,0,0,220,224,5,59,0,0,221,223,
        8,2,0,0,222,221,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,
        1,0,0,0,225,227,1,0,0,0,226,224,1,0,0,0,227,228,6,33,0,0,228,68,
        1,0,0,0,229,231,7,2,0,0,230,229,1,0,0,0,231,232,1,0,0,0,232,230,
        1,0,0,0,232,233,1,0,0,0,233,70,1,0,0,0,234,235,7,3,0,0,235,236,1,
        0,0,0,236,237,6,35,0,0,237,72,1,0,0,0,238,241,5,34,0,0,239,242,8,
        4,0,0,240,242,3,75,37,0,241,239,1,0,0,0,241,240,1,0,0,0,242,243,
        1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,245,1,0,0,0,245,246,
        5,34,0,0,246,74,1,0,0,0,247,248,5,92,0,0,248,249,7,5,0,0,249,76,
        1,0,0,0,250,252,7,6,0,0,251,250,1,0,0,0,252,253,1,0,0,0,253,251,
        1,0,0,0,253,254,1,0,0,0,254,78,1,0,0,0,255,256,7,7,0,0,256,80,1,
        0,0,0,257,258,5,42,0,0,258,82,1,0,0,0,259,260,5,48,0,0,260,262,7,
        8,0,0,261,263,7,9,0,0,262,261,1,0,0,0,263,264,1,0,0,0,264,262,1,
        0,0,0,264,265,1,0,0,0,265,84,1,0,0,0,266,267,5,48,0,0,267,269,7,
        10,0,0,268,270,7,11,0,0,269,268,1,0,0,0,270,271,1,0,0,0,271,269,
        1,0,0,0,271,272,1,0,0,0,272,86,1,0,0,0,273,274,5,48,0,0,274,276,
        7,12,0,0,275,277,7,13,0,0,276,275,1,0,0,0,277,278,1,0,0,0,278,276,
        1,0,0,0,278,279,1,0,0,0,279,88,1,0,0,0,10,0,217,224,232,241,243,
        253,264,271,278,1,0,1,0
    ]

class MyAssemblerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    COLON = 32
    NAME = 33
    COMMENT = 34
    EOL = 35
    WHITESPACE = 36
    StringVar = 37
    ESCAPED_CHAR = 38
    DEC_INTEGER = 39
    SIGN = 40
    STAR = 41
    OCT_INTEGER = 42
    HEX_INTEGER = 43
    BIN_INTEGER = 44

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'HLT'", "'WORD'", "'SHORT'", "'BYTE'", "'BYTES'", "'LD'", "'ST'", 
            "'ADD'", "'SUB'", "'INC'", "'DEC'", "'OR'", "'AND'", "'XOR'", 
            "'CMP'", "'JMP'", "'JE'", "'JZ'", "'JNE'", "'JNZ'", "'JG'", 
            "'JGE'", "'JL'", "'JLE'", "'JEOF'", "'IN'", "'OUT'", "'b8'", 
            "'b16'", "'b24'", "'b32'", "':'", "'*'" ]

    symbolicNames = [ "<INVALID>",
            "COLON", "NAME", "COMMENT", "EOL", "WHITESPACE", "StringVar", 
            "ESCAPED_CHAR", "DEC_INTEGER", "SIGN", "STAR", "OCT_INTEGER", 
            "HEX_INTEGER", "BIN_INTEGER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "COLON", 
                  "NAME", "COMMENT", "EOL", "WHITESPACE", "StringVar", "ESCAPED_CHAR", 
                  "DEC_INTEGER", "SIGN", "STAR", "OCT_INTEGER", "HEX_INTEGER", 
                  "BIN_INTEGER" ]

    grammarFileName = "MyAssembler.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


