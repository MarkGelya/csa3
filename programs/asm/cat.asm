        JMP     start
start:
loop:
        IN      1
        JEOF    end
        OUT     1
        JMP     loop
end:
        HLT
