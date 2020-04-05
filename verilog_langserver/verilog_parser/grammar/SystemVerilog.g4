grammar SystemVerilog;

import LexRules;

source : declaration* EOF;

declaration:
    module_declaration
    | interface_declaration
    | program_declaration
    | package_declaration
    | package_item
    | config_declaration
    ;
    //  | udp_declaration
    //  | ( attribute_instance )* bind_directive
    //  | timescale_compiler_directive
    //  | include_compiler_directive


module_declaration   : 'module' identifier parameter_port_list? .*? 'endmodule';
interface_declaration: 'interface' identifier parameter_port_list? .*? 'endinterface';
program_declaration  : 'program' .*? 'endprogram';
package_declaration  : 'package' (package_item | .*?) 'endpackage';
config_declaration   : 'config' .*? 'endconfig';
class_declaration   : 'virtual'? 'class' identifier .*? 'endclass' label? ;

package_item: task_declaration | function_declaration | class_declaration;

task_declaration    : 'task' identifier .*? 'endtask';
function_declaration: 'function' return_val identifier '(' .*? 'endfunction';

parameter_port_list : '#(' .*? ')';
port_list:  '(' .*? ')' ;
return_val: 'void' | .*? ;

label: COLON identifier;
identifier: WORD;
hierarchical_identifier : ( '$root' '.' )? ( identifier constant_bit_select '.' )* identifier ;
constant_bit_select : ( '[' WORD ']' )* ;