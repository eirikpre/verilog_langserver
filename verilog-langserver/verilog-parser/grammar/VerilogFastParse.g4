parser grammar VerilogFastParse;
/*
    This is a simple grammar to describe global objects
    for rough indexation
*/
options { tokenVocab=VerilogLexer; }

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

module_declaration   : Module .*? Endmodule;
interface_declaration: Interface .*? Endinterface;
program_declaration  : Program .*? Endprogram;
package_declaration  : Package (package_item | .*?) Endpackage;
config_declaration   : Config .*? Endconfig;

package_item:
    task_declaration
    | function_declaration
    | class_declaration
    | .*? SEMICOLON
    ;

task_declaration    : Task .*? Endtask;
function_declaration: Function .*? Endfunction;
class_declaration   : Virtual? Class Identifier .*? Endclass Label? ;



