        JMP     start
        BYTE    0xFF
hello:  BYTES   "hello"
data:   WORD    0xF1F2F3F4
str:    BYTES   256
ptr:    SHORT   str
ptr0:   SHORT   str
i:      SHORT   0
up:     BYTE    0x20
one:    BYTE    1
start:
loop:
        IN      0x0
        ST      *ptr    b8
        LD      ptr     b16
        INC
        ST      ptr     b16
        LD      i       b8
        INC
        ST      i       b8
        CMP     str     b8
        JGE     end
        JMP     loop
end:
        LD      one     b8
        OUT     0x0
        LD      ptr0    b16
        INC
        ST      ptr     b16
        LD      *ptr    b8
        SUB     up      b8
        OUT     0x0
        HLT
