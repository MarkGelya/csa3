        JMP     start
buff:   BYTE    0xFF
start:
loop:
        IN      1
        OUT     1
        JEOF    end
        JMP     loop
end:
        HLT
