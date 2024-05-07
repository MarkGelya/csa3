start:

value: WORD    2024
    LD    0x10

ADD     *value
; this is comment
ST      *0x10
HLT ; and this
; ADD 0x10
test:
ADD 0x10
end:
