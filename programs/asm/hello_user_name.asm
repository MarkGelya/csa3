        JMP     start

str1:   BYTES   "What is your name?"
str3:   BYTES   "Hello,"
str2:   BYTES   256
space:  BYTE    0x20
symbol: BYTE    0x21

ptr1:   SHORT   str1
ptr2:   SHORT   str2
ptr3:   SHORT   str3

ptr:    SHORT   0
i:      BYTE    0
zero:   WORD    0

start:
        ; init variables for print
        LD      ptr1    b16
        ST      ptr     b16
        LD      zero
        ST      i
loop1:
        ; print1
        LD      *ptr    b8
        OUT     0
        LD      ptr     b16
        INC
        ST      ptr     b16
        LD      i       b8
        CMP     *ptr1   b8
        JGE     input
        INC
        ST      i       b8
        JMP     loop1
input:
        IN      0
        ST      str2    b8
        LD      zero
        ST      i       b8
        LD      ptr2    b16
        ST      ptr     b16
loop2:
        LD      ptr     b16
        INC
        ST      ptr     b16
        LD      i       b8
        CMP     *ptr2   b8
        JGE     print2
        INC
        ST      i       b8
        IN      0
        ST      *ptr    b8
        JMP     loop2
print2:
        ; format string
        LD      str2    b8
        ADD     str3    b8
        INC
        INC
        ST      str3    b8
        ADD     ptr3    b16
        ST      ptr     b16
        LD      symbol  b8
        ST      *ptr    b8
        LD      space   b8
        ST      str2    b8

        ; init variables for print
        LD      ptr3    b16
        ST      ptr     b16
        LD      zero
        ST      i

loop3:
        LD      *ptr    b8
        OUT     0
        LD      ptr     b16
        INC
        ST      ptr     b16
        LD      i       b8
        CMP     *ptr3   b8
        JG     end
        INC
        ST      i       b8
        JMP     loop3
end:
        HLT
