grammar DocumentSymbols;

import LexerRules;

source : (declaration | .+?)* EOF;

declaration:
    module_declaration
    | interface_declaration
    | program_declaration
    | package_declaration
    | config_declaration
    | udp_declaration
    | item
    ;
    //  | ( attribute_instance )* bind_directive
    //  | timescale_compiler_directive # Ignored in lexer rules!
    //  | include_compiler_directive   # Ignored in lexer rules!


module_declaration   : 'module' identifier parameter_list? item*? 'endmodule' label?;
interface_declaration: 'interface' identifier parameter_list? item*? 'endinterface' label?;
program_declaration  : 'program' life_time? identifier item*? 'endprogram' label?;
package_declaration  : 'package' identifier item*? 'endpackage' label?;
config_declaration   : 'config' identifier item*? 'endconfig' label?;
udp_declaration      : 'primitive' identifier item*? 'endprimitive' label?;
class_declaration    : 'virtual'? 'class' life_time? identifier
    ('extends' type_identifier .*?)?
    ('implements' type_identifier parameter_list? (',' type_identifier parameter_list?)*)?
    ';' item*? 'endclass' label?;

item:
    task_declaration
    | function_declaration
    | class_declaration
    | type_declaration
    | instantiation
    | .+?
    ;

task_declaration    : 'task' identifier .*? 'endtask' label?;
function_declaration: 'function' return_val identifier '(' .*? 'endfunction' label?;
type_declaration    : 'typedef' .*? identifier ';';

parameter_list : '#(' .*? ')';
port_list:  '(' .*? ')' ;
return_val: 'void' | .*? ;
life_time: 'static' | 'automatic';
attribute: '(' '*' .*? ')';

instantiation:
    type_identifier parameter_list?
    identifier ( '[' .*? ']' )* port_list?
    ( ',' identifier ( '[' .*? ']' )* port_list? )* ';'
    | .+?
    ;

type_identifier: ( Word '::' )? Word ('[' .*? ']')*;
identifier: Word;
label: Colon identifier;
hierarchical_identifier : ( '$root' '.' )? ( Word constant_bit_select '.' )* identifier ;
constant_bit_select : ( '[' Word ']' )* ;