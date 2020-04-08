# Generated from C:\Users\eirik\Desktop\verilog-langserver\verilog_langserver\verilog_parser/grammar/WorkspaceSymbol.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u00fc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\7\2,\n\2\f\2\16\2/\13\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\6\3:\n\3\r\3\16\3;\5\3")
        buf.write(">\n\3\3\4\3\4\3\4\5\4C\n\4\3\4\7\4F\n\4\f\4\16\4I\13\4")
        buf.write("\3\4\3\4\5\4M\n\4\3\5\3\5\3\5\5\5R\n\5\3\5\7\5U\n\5\f")
        buf.write("\5\16\5X\13\5\3\5\3\5\5\5\\\n\5\3\6\3\6\5\6`\n\6\3\6\3")
        buf.write("\6\7\6d\n\6\f\6\16\6g\13\6\3\6\3\6\5\6k\n\6\3\7\3\7\3")
        buf.write("\7\7\7p\n\7\f\7\16\7s\13\7\5\7u\n\7\3\7\3\7\5\7y\n\7\3")
        buf.write("\b\3\b\3\b\7\b~\n\b\f\b\16\b\u0081\13\b\3\b\3\b\5\b\u0085")
        buf.write("\n\b\3\t\5\t\u0088\n\t\3\t\3\t\5\t\u008c\n\t\3\t\3\t\7")
        buf.write("\t\u0090\n\t\f\t\16\t\u0093\13\t\3\t\3\t\5\t\u0097\n\t")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u009d\n\n\3\13\3\13\3\13\7\13\u00a2")
        buf.write("\n\13\f\13\16\13\u00a5\13\13\3\13\3\13\5\13\u00a9\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\7\f\u00b0\n\f\f\f\16\f\u00b3\13\f")
        buf.write("\3\f\3\f\5\f\u00b7\n\f\3\r\3\r\7\r\u00bb\n\r\f\r\16\r")
        buf.write("\u00be\13\r\3\r\3\r\3\r\3\16\3\16\7\16\u00c5\n\16\f\16")
        buf.write("\16\16\u00c8\13\16\3\16\3\16\3\17\3\17\7\17\u00ce\n\17")
        buf.write("\f\17\16\17\u00d1\13\17\3\17\3\17\3\20\3\20\7\20\u00d7")
        buf.write("\n\20\f\20\16\20\u00da\13\20\5\20\u00dc\n\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\5\24\u00e7\n\24\3")
        buf.write("\24\3\24\3\24\3\24\7\24\u00ed\n\24\f\24\16\24\u00f0\13")
        buf.write("\24\3\24\3\24\3\25\3\25\3\25\7\25\u00f7\n\25\f\25\16\25")
        buf.write("\u00fa\13\25\3\25\17;GVeq\177\u0091\u00a3\u00b1\u00bc")
        buf.write("\u00c6\u00cf\u00d8\2\26\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(\2\3\3\2\27\30\2\u0110\2-\3\2\2\2\4=\3")
        buf.write("\2\2\2\6?\3\2\2\2\bN\3\2\2\2\n]\3\2\2\2\fl\3\2\2\2\16")
        buf.write("z\3\2\2\2\20\u0087\3\2\2\2\22\u009c\3\2\2\2\24\u009e\3")
        buf.write("\2\2\2\26\u00aa\3\2\2\2\30\u00b8\3\2\2\2\32\u00c2\3\2")
        buf.write("\2\2\34\u00cb\3\2\2\2\36\u00db\3\2\2\2 \u00dd\3\2\2\2")
        buf.write("\"\u00df\3\2\2\2$\u00e1\3\2\2\2&\u00e6\3\2\2\2(\u00f8")
        buf.write("\3\2\2\2*,\5\4\3\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2")
        buf.write("\2\2.\60\3\2\2\2/-\3\2\2\2\60\61\7\2\2\3\61\3\3\2\2\2")
        buf.write("\62>\5\6\4\2\63>\5\b\5\2\64>\5\n\6\2\65>\5\f\7\2\66>\5")
        buf.write("\22\n\2\67>\5\16\b\28:\13\2\2\298\3\2\2\2:;\3\2\2\2;<")
        buf.write("\3\2\2\2;9\3\2\2\2<>\3\2\2\2=\62\3\2\2\2=\63\3\2\2\2=")
        buf.write("\64\3\2\2\2=\65\3\2\2\2=\66\3\2\2\2=\67\3\2\2\2=9\3\2")
        buf.write("\2\2>\5\3\2\2\2?@\7\3\2\2@B\5\"\22\2AC\5\32\16\2BA\3\2")
        buf.write("\2\2BC\3\2\2\2CG\3\2\2\2DF\13\2\2\2ED\3\2\2\2FI\3\2\2")
        buf.write("\2GH\3\2\2\2GE\3\2\2\2HJ\3\2\2\2IG\3\2\2\2JL\7\4\2\2K")
        buf.write("M\5$\23\2LK\3\2\2\2LM\3\2\2\2M\7\3\2\2\2NO\7\5\2\2OQ\5")
        buf.write("\"\22\2PR\5\32\16\2QP\3\2\2\2QR\3\2\2\2RV\3\2\2\2SU\13")
        buf.write("\2\2\2TS\3\2\2\2UX\3\2\2\2VW\3\2\2\2VT\3\2\2\2WY\3\2\2")
        buf.write("\2XV\3\2\2\2Y[\7\6\2\2Z\\\5$\23\2[Z\3\2\2\2[\\\3\2\2\2")
        buf.write("\\\t\3\2\2\2]_\7\7\2\2^`\5 \21\2_^\3\2\2\2_`\3\2\2\2`")
        buf.write("a\3\2\2\2ae\5\"\22\2bd\13\2\2\2cb\3\2\2\2dg\3\2\2\2ef")
        buf.write("\3\2\2\2ec\3\2\2\2fh\3\2\2\2ge\3\2\2\2hj\7\b\2\2ik\5$")
        buf.write("\23\2ji\3\2\2\2jk\3\2\2\2k\13\3\2\2\2lt\7\t\2\2mu\5\22")
        buf.write("\n\2np\13\2\2\2on\3\2\2\2ps\3\2\2\2qr\3\2\2\2qo\3\2\2")
        buf.write("\2ru\3\2\2\2sq\3\2\2\2tm\3\2\2\2tq\3\2\2\2uv\3\2\2\2v")
        buf.write("x\7\n\2\2wy\5$\23\2xw\3\2\2\2xy\3\2\2\2y\r\3\2\2\2z{\7")
        buf.write("\13\2\2{\177\5\"\22\2|~\13\2\2\2}|\3\2\2\2~\u0081\3\2")
        buf.write("\2\2\177\u0080\3\2\2\2\177}\3\2\2\2\u0080\u0082\3\2\2")
        buf.write("\2\u0081\177\3\2\2\2\u0082\u0084\7\f\2\2\u0083\u0085\5")
        buf.write("$\23\2\u0084\u0083\3\2\2\2\u0084\u0085\3\2\2\2\u0085\17")
        buf.write("\3\2\2\2\u0086\u0088\7\r\2\2\u0087\u0086\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\7\16\2")
        buf.write("\2\u008a\u008c\5 \21\2\u008b\u008a\3\2\2\2\u008b\u008c")
        buf.write("\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u0091\5\"\22\2\u008e")
        buf.write("\u0090\13\2\2\2\u008f\u008e\3\2\2\2\u0090\u0093\3\2\2")
        buf.write("\2\u0091\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0094")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0096\7\17\2\2\u0095")
        buf.write("\u0097\5$\23\2\u0096\u0095\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\21\3\2\2\2\u0098\u009d\5\24\13\2\u0099\u009d\5")
        buf.write("\26\f\2\u009a\u009d\5\20\t\2\u009b\u009d\5\30\r\2\u009c")
        buf.write("\u0098\3\2\2\2\u009c\u0099\3\2\2\2\u009c\u009a\3\2\2\2")
        buf.write("\u009c\u009b\3\2\2\2\u009d\23\3\2\2\2\u009e\u009f\7\20")
        buf.write("\2\2\u009f\u00a3\5\"\22\2\u00a0\u00a2\13\2\2\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a6\u00a8\7\21\2\2\u00a7\u00a9\5$\23\2\u00a8\u00a7")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\25\3\2\2\2\u00aa\u00ab")
        buf.write("\7\22\2\2\u00ab\u00ac\5\36\20\2\u00ac\u00ad\5\"\22\2\u00ad")
        buf.write("\u00b1\7#\2\2\u00ae\u00b0\13\2\2\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b3\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b1\u00af\3")
        buf.write("\2\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b6")
        buf.write("\7\23\2\2\u00b5\u00b7\5$\23\2\u00b6\u00b5\3\2\2\2\u00b6")
        buf.write("\u00b7\3\2\2\2\u00b7\27\3\2\2\2\u00b8\u00bc\7\24\2\2\u00b9")
        buf.write("\u00bb\13\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2")
        buf.write("\2\u00bc\u00bd\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00bf")
        buf.write("\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\5\"\22\2\u00c0")
        buf.write("\u00c1\7\'\2\2\u00c1\31\3\2\2\2\u00c2\u00c6\7\25\2\2\u00c3")
        buf.write("\u00c5\13\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2")
        buf.write("\2\u00c6\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c9")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\7$\2\2\u00ca")
        buf.write("\33\3\2\2\2\u00cb\u00cf\7#\2\2\u00cc\u00ce\13\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00d0\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3")
        buf.write("\2\2\2\u00d2\u00d3\7$\2\2\u00d3\35\3\2\2\2\u00d4\u00dc")
        buf.write("\7\26\2\2\u00d5\u00d7\13\2\2\2\u00d6\u00d5\3\2\2\2\u00d7")
        buf.write("\u00da\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d8\u00d6\3\2\2\2")
        buf.write("\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00d4\3")
        buf.write("\2\2\2\u00db\u00d8\3\2\2\2\u00dc\37\3\2\2\2\u00dd\u00de")
        buf.write("\t\2\2\2\u00de!\3\2\2\2\u00df\u00e0\78\2\2\u00e0#\3\2")
        buf.write("\2\2\u00e1\u00e2\7(\2\2\u00e2\u00e3\5\"\22\2\u00e3%\3")
        buf.write("\2\2\2\u00e4\u00e5\7\31\2\2\u00e5\u00e7\7,\2\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00ee\3\2\2\2\u00e8")
        buf.write("\u00e9\78\2\2\u00e9\u00ea\5(\25\2\u00ea\u00eb\7,\2\2\u00eb")
        buf.write("\u00ed\3\2\2\2\u00ec\u00e8\3\2\2\2\u00ed\u00f0\3\2\2\2")
        buf.write("\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f1\3")
        buf.write("\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f2\5\"\22\2\u00f2")
        buf.write("\'\3\2\2\2\u00f3\u00f4\7!\2\2\u00f4\u00f5\78\2\2\u00f5")
        buf.write("\u00f7\7\"\2\2\u00f6\u00f3\3\2\2\2\u00f7\u00fa\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9)\3\2\2")
        buf.write("\2\u00fa\u00f8\3\2\2\2$-;=BGLQV[_ejqtx\177\u0084\u0087")
        buf.write("\u008b\u0091\u0096\u009c\u00a3\u00a8\u00b1\u00b6\u00bc")
        buf.write("\u00c6\u00cf\u00d8\u00db\u00e6\u00ee\u00f8")
        return buf.getvalue()


class WorkspaceSymbolParser ( Parser ):

    grammarFileName = "WorkspaceSymbol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'module'", "'endmodule'", "'interface'", 
                     "'endinterface'", "'program'", "'endprogram'", "'package'", 
                     "'endpackage'", "'config'", "'endconfig'", "'virtual'", 
                     "'class'", "'endclass'", "'task'", "'endtask'", "'function'", 
                     "'endfunction'", "'typedef'", "'#('", "'void'", "'static'", 
                     "'automatic'", "'$root'", "<INVALID>", "<INVALID>", 
                     "' '", "'\t'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "':'", 
                     "','", "'='", "'?'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SINGLELINE_COMMENT", "MULTILINE_COMMENT", "SPACE", 
                      "TAB", "NEWLINE", "String", "COMPILER_DIRECTIVE", 
                      "OpenBracket", "CloseBracket", "OpenParen", "CloseParen", 
                      "OpenBrace", "CloseBrace", "SemiColon", "Colon", "Comma", 
                      "Assign", "QuestionMark", "Dot", "Operators", "Number", 
                      "IntegralNumber", "RealNumber", "UnsignedNumber", 
                      "DecimalNumber", "BinaryNumber", "OctalNumber", "HexNumber", 
                      "UnbasedUnsizedLiteral", "Time", "Word" ]

    RULE_source = 0
    RULE_declaration = 1
    RULE_module_declaration = 2
    RULE_interface_declaration = 3
    RULE_program_declaration = 4
    RULE_package_declaration = 5
    RULE_config_declaration = 6
    RULE_class_declaration = 7
    RULE_package_item = 8
    RULE_task_declaration = 9
    RULE_function_declaration = 10
    RULE_type_declaration = 11
    RULE_parameter_port_list = 12
    RULE_port_list = 13
    RULE_return_val = 14
    RULE_life_time = 15
    RULE_identifier = 16
    RULE_label = 17
    RULE_hierarchical_identifier = 18
    RULE_constant_bit_select = 19

    ruleNames =  [ "source", "declaration", "module_declaration", "interface_declaration", 
                   "program_declaration", "package_declaration", "config_declaration", 
                   "class_declaration", "package_item", "task_declaration", 
                   "function_declaration", "type_declaration", "parameter_port_list", 
                   "port_list", "return_val", "life_time", "identifier", 
                   "label", "hierarchical_identifier", "constant_bit_select" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    SINGLELINE_COMMENT=24
    MULTILINE_COMMENT=25
    SPACE=26
    TAB=27
    NEWLINE=28
    String=29
    COMPILER_DIRECTIVE=30
    OpenBracket=31
    CloseBracket=32
    OpenParen=33
    CloseParen=34
    OpenBrace=35
    CloseBrace=36
    SemiColon=37
    Colon=38
    Comma=39
    Assign=40
    QuestionMark=41
    Dot=42
    Operators=43
    Number=44
    IntegralNumber=45
    RealNumber=46
    UnsignedNumber=47
    DecimalNumber=48
    BinaryNumber=49
    OctalNumber=50
    HexNumber=51
    UnbasedUnsizedLiteral=52
    Time=53
    Word=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SourceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(WorkspaceSymbolParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkspaceSymbolParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(WorkspaceSymbolParser.DeclarationContext,i)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_source

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSource" ):
                listener.enterSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSource" ):
                listener.exitSource(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSource" ):
                return visitor.visitSource(self)
            else:
                return visitor.visitChildren(self)




    def source(self):

        localctx = WorkspaceSymbolParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_source)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << WorkspaceSymbolParser.T__0) | (1 << WorkspaceSymbolParser.T__1) | (1 << WorkspaceSymbolParser.T__2) | (1 << WorkspaceSymbolParser.T__3) | (1 << WorkspaceSymbolParser.T__4) | (1 << WorkspaceSymbolParser.T__5) | (1 << WorkspaceSymbolParser.T__6) | (1 << WorkspaceSymbolParser.T__7) | (1 << WorkspaceSymbolParser.T__8) | (1 << WorkspaceSymbolParser.T__9) | (1 << WorkspaceSymbolParser.T__10) | (1 << WorkspaceSymbolParser.T__11) | (1 << WorkspaceSymbolParser.T__12) | (1 << WorkspaceSymbolParser.T__13) | (1 << WorkspaceSymbolParser.T__14) | (1 << WorkspaceSymbolParser.T__15) | (1 << WorkspaceSymbolParser.T__16) | (1 << WorkspaceSymbolParser.T__17) | (1 << WorkspaceSymbolParser.T__18) | (1 << WorkspaceSymbolParser.T__19) | (1 << WorkspaceSymbolParser.T__20) | (1 << WorkspaceSymbolParser.T__21) | (1 << WorkspaceSymbolParser.T__22) | (1 << WorkspaceSymbolParser.SINGLELINE_COMMENT) | (1 << WorkspaceSymbolParser.MULTILINE_COMMENT) | (1 << WorkspaceSymbolParser.SPACE) | (1 << WorkspaceSymbolParser.TAB) | (1 << WorkspaceSymbolParser.NEWLINE) | (1 << WorkspaceSymbolParser.String) | (1 << WorkspaceSymbolParser.COMPILER_DIRECTIVE) | (1 << WorkspaceSymbolParser.OpenBracket) | (1 << WorkspaceSymbolParser.CloseBracket) | (1 << WorkspaceSymbolParser.OpenParen) | (1 << WorkspaceSymbolParser.CloseParen) | (1 << WorkspaceSymbolParser.OpenBrace) | (1 << WorkspaceSymbolParser.CloseBrace) | (1 << WorkspaceSymbolParser.SemiColon) | (1 << WorkspaceSymbolParser.Colon) | (1 << WorkspaceSymbolParser.Comma) | (1 << WorkspaceSymbolParser.Assign) | (1 << WorkspaceSymbolParser.QuestionMark) | (1 << WorkspaceSymbolParser.Dot) | (1 << WorkspaceSymbolParser.Operators) | (1 << WorkspaceSymbolParser.Number) | (1 << WorkspaceSymbolParser.IntegralNumber) | (1 << WorkspaceSymbolParser.RealNumber) | (1 << WorkspaceSymbolParser.UnsignedNumber) | (1 << WorkspaceSymbolParser.DecimalNumber) | (1 << WorkspaceSymbolParser.BinaryNumber) | (1 << WorkspaceSymbolParser.OctalNumber) | (1 << WorkspaceSymbolParser.HexNumber) | (1 << WorkspaceSymbolParser.UnbasedUnsizedLiteral) | (1 << WorkspaceSymbolParser.Time) | (1 << WorkspaceSymbolParser.Word))) != 0):
                self.state = 40
                self.declaration()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(WorkspaceSymbolParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def module_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Module_declarationContext,0)


        def interface_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Interface_declarationContext,0)


        def program_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Program_declarationContext,0)


        def package_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Package_declarationContext,0)


        def package_item(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Package_itemContext,0)


        def config_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Config_declarationContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = WorkspaceSymbolParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.module_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.interface_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.program_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.package_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.package_item()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 53
                self.config_declaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 55 
                self._errHandler.sync(self)
                _alt = 1+1
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1+1:
                        self.state = 54
                        self.matchWildcard()

                    else:
                        raise NoViableAltException(self)
                    self.state = 57 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Module_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def parameter_port_list(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Parameter_port_listContext,0)


        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_module_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule_declaration" ):
                listener.enterModule_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule_declaration" ):
                listener.exitModule_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule_declaration" ):
                return visitor.visitModule_declaration(self)
            else:
                return visitor.visitChildren(self)




    def module_declaration(self):

        localctx = WorkspaceSymbolParser.Module_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_module_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(WorkspaceSymbolParser.T__0)
            self.state = 62
            self.identifier()
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 63
                self.parameter_port_list()


            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 66
                    self.matchWildcard() 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 72
            self.match(WorkspaceSymbolParser.T__1)
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 73
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def parameter_port_list(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Parameter_port_listContext,0)


        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_interface_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_declaration" ):
                listener.enterInterface_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_declaration" ):
                listener.exitInterface_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declaration" ):
                return visitor.visitInterface_declaration(self)
            else:
                return visitor.visitChildren(self)




    def interface_declaration(self):

        localctx = WorkspaceSymbolParser.Interface_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_interface_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(WorkspaceSymbolParser.T__2)
            self.state = 77
            self.identifier()
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 78
                self.parameter_port_list()


            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 81
                    self.matchWildcard() 
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 87
            self.match(WorkspaceSymbolParser.T__3)
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 88
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def life_time(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Life_timeContext,0)


        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_program_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram_declaration" ):
                listener.enterProgram_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram_declaration" ):
                listener.exitProgram_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_declaration" ):
                return visitor.visitProgram_declaration(self)
            else:
                return visitor.visitChildren(self)




    def program_declaration(self):

        localctx = WorkspaceSymbolParser.Program_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_program_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(WorkspaceSymbolParser.T__4)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.T__20 or _la==WorkspaceSymbolParser.T__21:
                self.state = 92
                self.life_time()


            self.state = 95
            self.identifier()
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 96
                    self.matchWildcard() 
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 102
            self.match(WorkspaceSymbolParser.T__5)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 103
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Package_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def package_item(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Package_itemContext,0)


        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_package_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackage_declaration" ):
                listener.enterPackage_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackage_declaration" ):
                listener.exitPackage_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackage_declaration" ):
                return visitor.visitPackage_declaration(self)
            else:
                return visitor.visitChildren(self)




    def package_declaration(self):

        localctx = WorkspaceSymbolParser.Package_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_package_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(WorkspaceSymbolParser.T__6)
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 107
                self.package_item()
                pass

            elif la_ == 2:
                self.state = 111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 108
                        self.matchWildcard() 
                    self.state = 113
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass


            self.state = 116
            self.match(WorkspaceSymbolParser.T__7)
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 117
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Config_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_config_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfig_declaration" ):
                listener.enterConfig_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfig_declaration" ):
                listener.exitConfig_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfig_declaration" ):
                return visitor.visitConfig_declaration(self)
            else:
                return visitor.visitChildren(self)




    def config_declaration(self):

        localctx = WorkspaceSymbolParser.Config_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_config_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(WorkspaceSymbolParser.T__8)
            self.state = 121
            self.identifier()
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 122
                    self.matchWildcard() 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 128
            self.match(WorkspaceSymbolParser.T__9)
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 129
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def life_time(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Life_timeContext,0)


        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_class_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_declaration" ):
                listener.enterClass_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_declaration" ):
                listener.exitClass_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = WorkspaceSymbolParser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.T__10:
                self.state = 132
                self.match(WorkspaceSymbolParser.T__10)


            self.state = 135
            self.match(WorkspaceSymbolParser.T__11)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.T__20 or _la==WorkspaceSymbolParser.T__21:
                self.state = 136
                self.life_time()


            self.state = 139
            self.identifier()
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 140
                    self.matchWildcard() 
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 146
            self.match(WorkspaceSymbolParser.T__12)
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 147
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Package_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def task_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Task_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Function_declarationContext,0)


        def class_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Class_declarationContext,0)


        def type_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Type_declarationContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_package_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackage_item" ):
                listener.enterPackage_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackage_item" ):
                listener.exitPackage_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackage_item" ):
                return visitor.visitPackage_item(self)
            else:
                return visitor.visitChildren(self)




    def package_item(self):

        localctx = WorkspaceSymbolParser.Package_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_package_item)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WorkspaceSymbolParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.task_declaration()
                pass
            elif token in [WorkspaceSymbolParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.function_declaration()
                pass
            elif token in [WorkspaceSymbolParser.T__10, WorkspaceSymbolParser.T__11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.class_declaration()
                pass
            elif token in [WorkspaceSymbolParser.T__17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
                self.type_declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Task_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_task_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTask_declaration" ):
                listener.enterTask_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTask_declaration" ):
                listener.exitTask_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTask_declaration" ):
                return visitor.visitTask_declaration(self)
            else:
                return visitor.visitChildren(self)




    def task_declaration(self):

        localctx = WorkspaceSymbolParser.Task_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_task_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(WorkspaceSymbolParser.T__13)
            self.state = 157
            self.identifier()
            self.state = 161
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 158
                    self.matchWildcard() 
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 164
            self.match(WorkspaceSymbolParser.T__14)
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 165
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_val(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Return_valContext,0)


        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def OpenParen(self):
            return self.getToken(WorkspaceSymbolParser.OpenParen, 0)

        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = WorkspaceSymbolParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(WorkspaceSymbolParser.T__15)
            self.state = 169
            self.return_val()
            self.state = 170
            self.identifier()
            self.state = 171
            self.match(WorkspaceSymbolParser.OpenParen)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 172
                    self.matchWildcard() 
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 178
            self.match(WorkspaceSymbolParser.T__16)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 179
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def SemiColon(self):
            return self.getToken(WorkspaceSymbolParser.SemiColon, 0)

        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_type_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_declaration" ):
                listener.enterType_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_declaration" ):
                listener.exitType_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_declaration" ):
                return visitor.visitType_declaration(self)
            else:
                return visitor.visitChildren(self)




    def type_declaration(self):

        localctx = WorkspaceSymbolParser.Type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(WorkspaceSymbolParser.T__17)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 183
                    self.matchWildcard() 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 189
            self.identifier()
            self.state = 190
            self.match(WorkspaceSymbolParser.SemiColon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_port_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CloseParen(self):
            return self.getToken(WorkspaceSymbolParser.CloseParen, 0)

        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_parameter_port_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_port_list" ):
                listener.enterParameter_port_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_port_list" ):
                listener.exitParameter_port_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_port_list" ):
                return visitor.visitParameter_port_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_port_list(self):

        localctx = WorkspaceSymbolParser.Parameter_port_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter_port_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(WorkspaceSymbolParser.T__18)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 193
                    self.matchWildcard() 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 199
            self.match(WorkspaceSymbolParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Port_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenParen(self):
            return self.getToken(WorkspaceSymbolParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(WorkspaceSymbolParser.CloseParen, 0)

        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_port_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPort_list" ):
                listener.enterPort_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPort_list" ):
                listener.exitPort_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPort_list" ):
                return visitor.visitPort_list(self)
            else:
                return visitor.visitChildren(self)




    def port_list(self):

        localctx = WorkspaceSymbolParser.Port_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_port_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(WorkspaceSymbolParser.OpenParen)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 202
                    self.matchWildcard() 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 208
            self.match(WorkspaceSymbolParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_return_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_val" ):
                listener.enterReturn_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_val" ):
                listener.exitReturn_val(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_val" ):
                return visitor.visitReturn_val(self)
            else:
                return visitor.visitChildren(self)




    def return_val(self):

        localctx = WorkspaceSymbolParser.Return_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_return_val)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(WorkspaceSymbolParser.T__19)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 211
                        self.matchWildcard() 
                    self.state = 216
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Life_timeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_life_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLife_time" ):
                listener.enterLife_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLife_time" ):
                listener.exitLife_time(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLife_time" ):
                return visitor.visitLife_time(self)
            else:
                return visitor.visitChildren(self)




    def life_time(self):

        localctx = WorkspaceSymbolParser.Life_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_life_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==WorkspaceSymbolParser.T__20 or _la==WorkspaceSymbolParser.T__21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Word(self):
            return self.getToken(WorkspaceSymbolParser.Word, 0)

        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = WorkspaceSymbolParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(WorkspaceSymbolParser.Word)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Colon(self):
            return self.getToken(WorkspaceSymbolParser.Colon, 0)

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = WorkspaceSymbolParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(WorkspaceSymbolParser.Colon)
            self.state = 224
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hierarchical_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(WorkspaceSymbolParser.Dot)
            else:
                return self.getToken(WorkspaceSymbolParser.Dot, i)

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(WorkspaceSymbolParser.Word)
            else:
                return self.getToken(WorkspaceSymbolParser.Word, i)

        def constant_bit_select(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkspaceSymbolParser.Constant_bit_selectContext)
            else:
                return self.getTypedRuleContext(WorkspaceSymbolParser.Constant_bit_selectContext,i)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_hierarchical_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHierarchical_identifier" ):
                listener.enterHierarchical_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHierarchical_identifier" ):
                listener.exitHierarchical_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHierarchical_identifier" ):
                return visitor.visitHierarchical_identifier(self)
            else:
                return visitor.visitChildren(self)




    def hierarchical_identifier(self):

        localctx = WorkspaceSymbolParser.Hierarchical_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_hierarchical_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.T__22:
                self.state = 226
                self.match(WorkspaceSymbolParser.T__22)
                self.state = 227
                self.match(WorkspaceSymbolParser.Dot)


            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 230
                    self.match(WorkspaceSymbolParser.Word)
                    self.state = 231
                    self.constant_bit_select()
                    self.state = 232
                    self.match(WorkspaceSymbolParser.Dot) 
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 239
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_bit_selectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenBracket(self, i:int=None):
            if i is None:
                return self.getTokens(WorkspaceSymbolParser.OpenBracket)
            else:
                return self.getToken(WorkspaceSymbolParser.OpenBracket, i)

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(WorkspaceSymbolParser.Word)
            else:
                return self.getToken(WorkspaceSymbolParser.Word, i)

        def CloseBracket(self, i:int=None):
            if i is None:
                return self.getTokens(WorkspaceSymbolParser.CloseBracket)
            else:
                return self.getToken(WorkspaceSymbolParser.CloseBracket, i)

        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_constant_bit_select

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant_bit_select" ):
                listener.enterConstant_bit_select(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant_bit_select" ):
                listener.exitConstant_bit_select(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant_bit_select" ):
                return visitor.visitConstant_bit_select(self)
            else:
                return visitor.visitChildren(self)




    def constant_bit_select(self):

        localctx = WorkspaceSymbolParser.Constant_bit_selectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_constant_bit_select)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==WorkspaceSymbolParser.OpenBracket:
                self.state = 241
                self.match(WorkspaceSymbolParser.OpenBracket)
                self.state = 242
                self.match(WorkspaceSymbolParser.Word)
                self.state = 243
                self.match(WorkspaceSymbolParser.CloseBracket)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





