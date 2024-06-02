grammar MyAssembler;

program
    : line* EOF
    ;

line
    : label? instruction? EOL
    ;

label
    : name COLON
    ;


name
    : NAME
    ;

instruction
    : op operand*
    ;

op
    : op0
    | op1
    | op2
    | op3
    ;
op0
    : 'HLT'
    ;
op1
    : 'WORD'
    | 'SHORT'
    | 'BYTE'
    | 'BYTES'
    ;
op2
    : 'LD'
    | 'ST'
    | 'ADD'
    | 'SUB'
    | 'INC'
    | 'DEC'
    | 'OR'
    | 'AND'
    | 'XOR'
    | 'CMP'
    | 'JMP'
    | 'JE'
    | 'JZ'
    | 'JNE'
    | 'JNZ'
    | 'JG'
    | 'JGE'
    | 'JL'
    | 'JLE'
    ;
op3
    : 'IN'
    | 'OUT'
    ;

COLON: ':';
NAME: [a-zA-Z][a-zA-Z0-9]*;
COMMENT: ';' ~[\r\n]* -> channel(HIDDEN);
EOL: [\r\n]+;
WHITESPACE: [ \t] -> channel(HIDDEN);

operand
    : integer
    | name
    | final_addr
    | final_addr_label
    | bit_depth
    | string
    ;

final_addr: STAR integer;
final_addr_label: STAR name;
bit_depth
    : 'b8'
    | 'b16'
    | 'b24'
    | 'b32'
    ;
integer
    : DEC_INTEGER
    | HEX_INTEGER
    | OCT_INTEGER
    | BIN_INTEGER
    ;
string: '"' ( ESCAPED_CHAR | ~('\\'|'"') )* '"';

ESCAPED_CHAR: '\\' ( 'n' | 'r' | 't' | '"' | '\\' );
DEC_INTEGER: [0-9]+;
SIGN: '+' | '-';
STAR: '*';
OCT_INTEGER: '0' [qo][0-7]+;
HEX_INTEGER: '0' [xh][0-9A-F]+;
BIN_INTEGER: '0' [b][01]+;