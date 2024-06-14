JMP     start
a:      WORD    0
b:      WORD    1
buff:   WORD    0
res:
res0:   BYTE    0
res1:   BYTE    0
res2:   BYTE    0
res3:   BYTE    0
mask:   WORD    0x1
max:    WORD    50

start:
loop:
        LD      a
        ADD     b
; a -> buff, b -> a, buff -> a
        ST      buff
        LD      b
        ST      a
        LD      buff
        ST      b

        CMP     max
        JGE     end

        AND     mask
        JNZ     loop

        ST      res
        LD      res0    b8
        OUT     10
        LD      res1    b8
        OUT     10
        LD      res2    b8
        OUT     10
        LD      res3    b8
        OUT     10

        LD      b
        ADD     res
        ST      res

        JMP     loop
end:
        LD      res0    b8
        OUT     10
        LD      res1    b8
        OUT     10
        LD      res2    b8
        OUT     10
        LD      res3    b8
        OUT     10
        HLT
