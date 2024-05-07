a:      WORD    1
b:      WORD    1
buff:   WORD    0
i:      WORD    0
n:      WORD    20
term:   WORD    0
ascii0: WORD    0x30
start:
loop:
        LD      a
        ADD     ascii0
        OUT     1
        LD      a
        ADD     b
        ST      buff
        LD      b
        ST      a
        LD      buff
        ST      b
        LD      i
        INC
        ST      i
        CMP     n
        JGE     end
        JMP     loop
end:
        OUT     2
