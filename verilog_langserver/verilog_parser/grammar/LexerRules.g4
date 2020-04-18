lexer grammar LexerRules;

// channels { ERROR, PREPROCESS }

SINGLELINE_COMMENT: '//' (~[\n])* '\n'  -> skip;
MULTILINE_COMMENT : '/*' .*? '*/'       -> skip;
SPACE             : ' '                 -> skip;
TAB               : '\t'                -> skip;
NEWLINE           : '\r'? '\n'          -> skip;

String: '"' (~["] | '\\"')* '"' ;

COMPILER_DIRECTIVE: GRAVE Word .*? EOL -> skip;

OpenBracket : '[';
CloseBracket: ']';
OpenParen   : '(';
CloseParen  : ')';
OpenBrace   : '{';
CloseBrace  : '}';
SemiColon   : ';';
Colon       : ':';
Comma       : ',';
Assign      : '=';
QuestionMark: '?';
Dot         : '.';
Apostrophe  : APOSTROPHE;

Operators: '+'|'-'|'*'|'<'|'>'|'='|'%'|'!'|'~'|'@'|'$'|'#';
// ====================
//       Keywords
// ====================
Module      : 'module';
Endmodule   : 'endmodule';
Interface   : 'interface';
Endinterface: 'endinterface';
Class       : 'class';
Endclass    : 'endclass';
Config      : 'config';
Endconfig   : 'endconfig';
Primitive   : 'primitive';
Endprimitive: 'endprimitive';
Program     : 'program';
Endprogram  : 'endprogram';
Task        : 'task';
Endtask     : 'endtask';
Function    : 'function';
Endfunction : 'endfunction';
Package     : 'package';
Endpackage  : 'endpackage';

Input  : 'input';
Output : 'output';
Virtual: 'virtual';
Typedef: 'typedef';

// ====================
//       Numbers
// ====================
Number         : IntegralNumber | RealNumber;
IntegralNumber : DecimalNumber | OctalNumber | BinaryNumber | HexNumber | UnsignedNumber;
RealNumber
    : UnsignedNumber Dot UnsignedNumber
    | UnsignedNumber Dot UnsignedNumber [eE] SIGN UnsignedNumber;

UnsignedNumber: DIGIT           ( UNDERSCORE | DIGIT )*;

DecimalNumber: NON_ZERO_NUMBER? DECIMAL_BASE DECIMAL_VALUE;
BinaryNumber : NON_ZERO_NUMBER? BINARY_BASE BINARY_VALUE;
OctalNumber  : NON_ZERO_NUMBER? OCTAL_BASE OCTAL_VALUE;
HexNumber    : NON_ZERO_NUMBER? HEX_BASE HEX_VALUE;

UnbasedUnsizedLiteral: APOSTROPHE (X | Z | [01]);

Time: UnsignedNumber TIME_UNIT;
Word: (CHAR | UNDERSCORE)+;

// ====================
// Fragments
// ====================
fragment GRAVE     : [`];
fragment APOSTROPHE: ['];
fragment UNDERSCORE: [_];
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

fragment NON_ZERO_NUMBER: NON_ZERO_DIGIT  ( UNDERSCORE | DIGIT )*;

fragment DECIMAL_BASE : APOSTROPHE [dD];
fragment BINARY_BASE  : APOSTROPHE [bB];
fragment OCTAL_BASE   : APOSTROPHE [oO];
fragment HEX_BASE     : APOSTROPHE [hH];
fragment DECIMAL_VALUE: DECIMAL_DIGIT   ( UNDERSCORE | DECIMAL_DIGIT )*;
fragment BINARY_VALUE : BINARY_DIGIT    ( UNDERSCORE | BINARY_DIGIT  )*;
fragment OCTAL_VALUE  : OCTAL_DIGIT     ( UNDERSCORE | OCTAL_DIGIT   )*;
fragment HEX_VALUE    : HEX_DIGIT       ( UNDERSCORE | HEX_DIGIT     )*;
