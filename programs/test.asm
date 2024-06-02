start:
        LD      a
        JMP     skip
        HLT
skip:
        ADD     b
        ST      c
        HLT
a:      WORD    0xF4F3F2F1
b:      WORD    3
c:      WORD    3
