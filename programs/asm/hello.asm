        JMP     start
hello:  BYTES   "Hello, world!"
ptr0:   SHORT   hello
ptr:    SHORT   hello
i:      SHORT   0
start:
loop:
        LD      *ptr    b8
        OUT     0
        LD      ptr     b16
        INC
        ST      ptr     b16
        LD      i       b16
        CMP     *ptr0   b8
        JG      end
        INC
        ST      i       b16
        JMP     loop
end:
        HLT
