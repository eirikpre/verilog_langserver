lexer grammar LexRules;

// channels { ERROR, PREPROCESS }

// Configuration
SINGLELINE_COMMENT: '//' (~[\n])* '\n' -> skip;
MULTILINE_COMMENT : '/*' .*? '*/'      -> skip;

SPACE  : ' '        -> skip;
TAB    : '\t'       -> skip;
NEWLINE: '\r'? '\n' -> skip;

STRING: '"' (~["] | '\\"')* '"' ;

COMPILER_DIRECTIVE: GRAVE WORD .*? ~[\\] EOL -> skip;


COLON       : ':';
SEMICOLON   : ';';
PAR_OPEN    : '(';
PAR_CLOSE   : ')';
SQUARE_OPEN : '[';
SQUARE_CLOSE: ']';
CURLY_OPEN  : '{';
CURLY_CLOSE : '}';
COMMA       : ',';
WORD        : (CHAR | UNDERSCORE)+;


OPERATORS: '+'|'-'|'*'|'<'|'>'|'='|'%'|'!'|'~'|'@'|'$';

// Numbers
// C_IDENTIFIER : [a-zA-Z_] ( [a-zA-Z0-9_] )* ;
// SIMPLE_IDENTIFIER : [a-zA-Z_] ( [a-zA-Z0-9_$] )* ;
// SYSTEM_TF_IDENTIFIER : '$' [a-zA-Z0-9_$] ( [a-zA-Z0-9_$] )* ;

// ====================
//       Numbers
// ====================
NUMBER         : INTEGRAL_NUMBER | REAL_NUMBER;
INTEGRAL_NUMBER: DECIMAL_NUMBER | OCTAL_NUMBER | BINARY_NUMBER | HEX_NUMBER | UNSIGNED_NUMBER;
REAL_NUMBER    : UNSIGNED_NUMBER DOT UNSIGNED_NUMBER | UNSIGNED_NUMBER DOT UNSIGNED_NUMBER [eE] SIGN UNSIGNED_NUMBER;
DECIMAL_NUMBER : SIZE DECIMAL_BASE DECIMAL_DIGIT*;
BINARY_NUMBER  : SIZE BINARY_BASE BINARY_VALUE;
OCTAL_NUMBER   : SIZE OCTAL_BASE OCTAL_VALUE;
HEX_NUMBER     : SIZE HEX_BASE HEX_VALUE;
SIZE           : NON_ZERO_NUMBER;
NON_ZERO_NUMBER: NON_ZERO_DIGIT  ( UNDERSCORE | DIGIT )*;
UNSIGNED_NUMBER: DIGIT           ( UNDERSCORE | DIGIT )*;
DECIMAL_VALUE  : DECIMAL_DIGIT   ( UNDERSCORE | DECIMAL_DIGIT )*;
BINARY_VALUE   : BINARY_DIGIT    ( UNDERSCORE | BINARY_DIGIT  )*;
OCTAL_VALUE    : OCTAL_DIGIT     ( UNDERSCORE | OCTAL_DIGIT   )*;
HEX_VALUE      : HEX_DIGIT       ( UNDERSCORE | HEX_DIGIT     )*;

UNBASED_UNSIZED_LITERAL: APOSTROPHE (X | Z | [01]);


// Fragments
fragment GRAVE     : [`];
fragment APOSTROPHE: ['];
fragment UNDERSCORE: [_];
fragment DOT       : [.];
fragment EOL       : '\n' '\r'?;


fragment SIGN      : [+-];
fragment TIME_UNIT : ([munpf])?[s];
fragment X         : [xX];
fragment Z         : [zZ?];
fragment CHAR      : [0-9A-Za-z];
fragment DIGIT     : [0-9];

fragment NON_ZERO_DIGIT: [1-9];
fragment DECIMAL_DIGIT : [0-9]       | X | Z;
fragment BINARY_DIGIT  : [01]        | X | Z;
fragment OCTAL_DIGIT   : [0-7]       | X | Z;
fragment HEX_DIGIT     : [0-9a-fA-F] | X | Z;

fragment DECIMAL_BASE: APOSTROPHE [dD];
fragment BINARY_BASE : APOSTROPHE [bB];
fragment OCTAL_BASE  : APOSTROPHE [oO];
fragment HEX_BASE    : APOSTROPHE [hH];

