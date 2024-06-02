grammar MyAlg;

program : statement+ EOF
    ;

type
    : type_basic
    | type_basic ID '[' INTVAL ']'
    ;

type_basic
    : INT
    | SHORT
    | BYTE
    ;

statements
    : (statement)*
    ;

statement
    : newVar ';'
    | assignSt ';'
    | whileSt
    | forSt
    | ifElseSt
    | function ';'
    | label ';'
    | gotoSt ';'
    ;

ifElseSt
    :  ifSt elseSt?
    ;

ifSt
    : IF expr '{' statements '}'
    ;

forSt
    : FOR '(' assignSt ';' expr ';' assignSt ')' '{' statements '}'
    ;

whileSt
    : WHILE expr '{' statements '}'
    ;

elseSt
    : ELSE '{' statements '}'
    ;

gotoSt
    : GOTO ID
    ;

function
    : ID '(' (args)? ')'
    ;

args
    : arg (',' arg)*
    ;

arg
    : ID
    ;

assignSt: left_expr ASSIGN expr;

newVar
    : type assignSt
    ;

label
    : ID COLON
    ;


left_expr
    : ident
    | array_access
    ;

expr
    : (NOT | PLUS | MINUS) expr
    | '(' expr ')'
    | expr (PLUS | MINUS) expr
    | expr (EQUAL | NOTEQUAL | LESS | LESSEQ | BIGGER | BIGGEREQ) expr
    | expr (AND | OR) expr
    | CHARVAL
    | INTVAL
    | BOOLVAL
    | pointer
    | ident
    | array_access
    | ident '(' ((expr) (',' expr)*)? ')'
    ;

ident
    : ID
    ;

pointer
    : STAR ID
    ;

array_access
    : ident '[' expr ']'
    ;

ASSIGN    : '=' ;
EQUAL     : '==' ;
NOTEQUAL  : '!=' ;
LESS      : '<';
LESSEQ    : '<=';
BIGGER    : '>';
BIGGEREQ  : '>=';
PLUS      : '+' ;
MINUS     : '-';
INT       : 'int';
SHORT     : 'short';
BYTE      : 'byte';
VOID      : 'void';
STRING    : 'string';
NOT       : '~';
AND       : '&';
OR        : '|';
IF        : 'if' ;
ELSE      : 'else';
WHILE     : 'while';
FOR       : 'for';
GOTO      : 'goto';
ARRAY     : 'array';
CHARVAL      : '\'' ( ESC_SEQ | ~('\\'|'"') ) '\'';
ID        : ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;
COLON     : ':';
BOOLVAL   : 'true' | 'false';
STAR      : '*';

INTVAL
    : DEC_INTEGER
    | HEX_INTEGER
    | OCT_INTEGER
    | BIN_INTEGER
    ;

DEC_INTEGER: [0-9]+;
OCT_INTEGER: '0' [qo][0-7]+;
HEX_INTEGER: '0' [xh][0-9A-F]+;
BIN_INTEGER: '0' [b][01]+;

STRINGVAL: '"' ( ESC_SEQ | ~('\\'|'"') )* '"' ;

ESC_SEQ: '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\') ;
COMMENT: '//' ~('\n'|'\r')* '\r'? '\n' -> skip ;
WHITESPACE: (' '|'\t'|'\r'|'\n')+ -> skip ;
