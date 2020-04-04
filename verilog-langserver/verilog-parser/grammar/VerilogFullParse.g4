parser grammar VerilogFullParse;
/*
    This is a grammar for feature complete parsing
*/
options { tokenVocab=VerilogLexer; }

// source_text : ( timeunits_declaration )? ( description )* ;
source_text : ( description )* ;

description :
    module_declaration;

            //  | udp_declaration
            //  | interface_declaration
            //  | program_declaration
            //  | package_declaration
            //  | ( attribute_instance )* package_item
            //  | ( attribute_instance )* bind_directive
            //  | config_declaration
            //  | timescale_compiler_directive
            //  | include_compiler_directive ;

module_declaration          : Module .*? Endmodule;
udp_declaration             : ;
interface_declaration       : ;
program_declaration         : ;
package_declaration         : ;
attribute_instance          : ;
config_declaration          : ;
timescale_compiler_directive: ;
include_compiler_directive  : ;

