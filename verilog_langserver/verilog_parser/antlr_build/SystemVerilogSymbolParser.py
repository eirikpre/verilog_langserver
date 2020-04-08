# Generated from C:\Users\eirik\Desktop\verilog-langserver\verilog_langserver\verilog_parser/grammar/SystemVerilogSymbol.g4 by ANTLR 4.8
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
        buf.write("\u00e8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\7\2,\n\2\f\2\16\2/\13\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\5\39\n\3\3\4\3\4\3\4\5\4>\n")
        buf.write("\4\3\4\7\4A\n\4\f\4\16\4D\13\4\3\4\3\4\3\5\3\5\3\5\5\5")
        buf.write("K\n\5\3\5\7\5N\n\5\f\5\16\5Q\13\5\3\5\3\5\3\6\3\6\5\6")
        buf.write("W\n\6\3\6\3\6\7\6[\n\6\f\6\16\6^\13\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\7\7e\n\7\f\7\16\7h\13\7\5\7j\n\7\3\7\3\7\3\b\3\b")
        buf.write("\7\bp\n\b\f\b\16\bs\13\b\3\b\3\b\3\t\5\tx\n\t\3\t\3\t")
        buf.write("\5\t|\n\t\3\t\3\t\7\t\u0080\n\t\f\t\16\t\u0083\13\t\3")
        buf.write("\t\3\t\5\t\u0087\n\t\3\n\3\n\3\n\3\n\5\n\u008d\n\n\3\13")
        buf.write("\3\13\3\13\7\13\u0092\n\13\f\13\16\13\u0095\13\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\7\f\u009e\n\f\f\f\16\f\u00a1")
        buf.write("\13\f\3\f\3\f\3\r\3\r\7\r\u00a7\n\r\f\r\16\r\u00aa\13")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\7\16\u00b1\n\16\f\16\16\16\u00b4")
        buf.write("\13\16\3\16\3\16\3\17\3\17\7\17\u00ba\n\17\f\17\16\17")
        buf.write("\u00bd\13\17\3\17\3\17\3\20\3\20\7\20\u00c3\n\20\f\20")
        buf.write("\16\20\u00c6\13\20\5\20\u00c8\n\20\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\24\3\24\5\24\u00d3\n\24\3\24\3\24\3")
        buf.write("\24\3\24\7\24\u00d9\n\24\f\24\16\24\u00dc\13\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\7\25\u00e3\n\25\f\25\16\25\u00e6\13")
        buf.write("\25\3\25\16BO\\fq\u0081\u0093\u009f\u00a8\u00b2\u00bb")
        buf.write("\u00c4\2\26\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(\2\3\3\2\27\30\2\u00f3\2-\3\2\2\2\48\3\2\2\2\6:\3\2")
        buf.write("\2\2\bG\3\2\2\2\nT\3\2\2\2\fa\3\2\2\2\16m\3\2\2\2\20w")
        buf.write("\3\2\2\2\22\u008c\3\2\2\2\24\u008e\3\2\2\2\26\u0098\3")
        buf.write("\2\2\2\30\u00a4\3\2\2\2\32\u00ae\3\2\2\2\34\u00b7\3\2")
        buf.write("\2\2\36\u00c7\3\2\2\2 \u00c9\3\2\2\2\"\u00cb\3\2\2\2$")
        buf.write("\u00cd\3\2\2\2&\u00d2\3\2\2\2(\u00e4\3\2\2\2*,\5\4\3\2")
        buf.write("+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\60\3\2\2\2/")
        buf.write("-\3\2\2\2\60\61\7\2\2\3\61\3\3\2\2\2\629\5\6\4\2\639\5")
        buf.write("\b\5\2\649\5\n\6\2\659\5\f\7\2\669\5\22\n\2\679\5\16\b")
        buf.write("\28\62\3\2\2\28\63\3\2\2\28\64\3\2\2\28\65\3\2\2\28\66")
        buf.write("\3\2\2\28\67\3\2\2\29\5\3\2\2\2:;\7\3\2\2;=\5\"\22\2<")
        buf.write(">\5\32\16\2=<\3\2\2\2=>\3\2\2\2>B\3\2\2\2?A\13\2\2\2@")
        buf.write("?\3\2\2\2AD\3\2\2\2BC\3\2\2\2B@\3\2\2\2CE\3\2\2\2DB\3")
        buf.write("\2\2\2EF\7\4\2\2F\7\3\2\2\2GH\7\5\2\2HJ\5\"\22\2IK\5\32")
        buf.write("\16\2JI\3\2\2\2JK\3\2\2\2KO\3\2\2\2LN\13\2\2\2ML\3\2\2")
        buf.write("\2NQ\3\2\2\2OP\3\2\2\2OM\3\2\2\2PR\3\2\2\2QO\3\2\2\2R")
        buf.write("S\7\6\2\2S\t\3\2\2\2TV\7\7\2\2UW\5 \21\2VU\3\2\2\2VW\3")
        buf.write("\2\2\2WX\3\2\2\2X\\\5\"\22\2Y[\13\2\2\2ZY\3\2\2\2[^\3")
        buf.write("\2\2\2\\]\3\2\2\2\\Z\3\2\2\2]_\3\2\2\2^\\\3\2\2\2_`\7")
        buf.write("\b\2\2`\13\3\2\2\2ai\7\t\2\2bj\5\22\n\2ce\13\2\2\2dc\3")
        buf.write("\2\2\2eh\3\2\2\2fg\3\2\2\2fd\3\2\2\2gj\3\2\2\2hf\3\2\2")
        buf.write("\2ib\3\2\2\2if\3\2\2\2jk\3\2\2\2kl\7\n\2\2l\r\3\2\2\2")
        buf.write("mq\7\13\2\2np\13\2\2\2on\3\2\2\2ps\3\2\2\2qr\3\2\2\2q")
        buf.write("o\3\2\2\2rt\3\2\2\2sq\3\2\2\2tu\7\f\2\2u\17\3\2\2\2vx")
        buf.write("\7\r\2\2wv\3\2\2\2wx\3\2\2\2xy\3\2\2\2y{\7\16\2\2z|\5")
        buf.write(" \21\2{z\3\2\2\2{|\3\2\2\2|}\3\2\2\2}\u0081\5\"\22\2~")
        buf.write("\u0080\13\2\2\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081")
        buf.write("\u0082\3\2\2\2\u0081\177\3\2\2\2\u0082\u0084\3\2\2\2\u0083")
        buf.write("\u0081\3\2\2\2\u0084\u0086\7\17\2\2\u0085\u0087\5$\23")
        buf.write("\2\u0086\u0085\3\2\2\2\u0086\u0087\3\2\2\2\u0087\21\3")
        buf.write("\2\2\2\u0088\u008d\5\24\13\2\u0089\u008d\5\26\f\2\u008a")
        buf.write("\u008d\5\20\t\2\u008b\u008d\5\30\r\2\u008c\u0088\3\2\2")
        buf.write("\2\u008c\u0089\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008b")
        buf.write("\3\2\2\2\u008d\23\3\2\2\2\u008e\u008f\7\20\2\2\u008f\u0093")
        buf.write("\5\"\22\2\u0090\u0092\13\2\2\2\u0091\u0090\3\2\2\2\u0092")
        buf.write("\u0095\3\2\2\2\u0093\u0094\3\2\2\2\u0093\u0091\3\2\2\2")
        buf.write("\u0094\u0096\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097\7")
        buf.write("\21\2\2\u0097\25\3\2\2\2\u0098\u0099\7\22\2\2\u0099\u009a")
        buf.write("\5\36\20\2\u009a\u009b\5\"\22\2\u009b\u009f\7#\2\2\u009c")
        buf.write("\u009e\13\2\2\2\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2")
        buf.write("\2\u009f\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a2")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\7\23\2\2\u00a3")
        buf.write("\27\3\2\2\2\u00a4\u00a8\7\24\2\2\u00a5\u00a7\13\2\2\2")
        buf.write("\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a9\3")
        buf.write("\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\u00ac\5\"\22\2\u00ac\u00ad\7\'\2\2\u00ad")
        buf.write("\31\3\2\2\2\u00ae\u00b2\7\25\2\2\u00af\u00b1\13\2\2\2")
        buf.write("\u00b0\u00af\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b3\3")
        buf.write("\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b5\3\2\2\2\u00b4\u00b2")
        buf.write("\3\2\2\2\u00b5\u00b6\7$\2\2\u00b6\33\3\2\2\2\u00b7\u00bb")
        buf.write("\7#\2\2\u00b8\u00ba\13\2\2\2\u00b9\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bd\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2")
        buf.write("\u00bc\u00be\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00bf\7")
        buf.write("$\2\2\u00bf\35\3\2\2\2\u00c0\u00c8\7\26\2\2\u00c1\u00c3")
        buf.write("\13\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00c8\3\2\2\2")
        buf.write("\u00c6\u00c4\3\2\2\2\u00c7\u00c0\3\2\2\2\u00c7\u00c4\3")
        buf.write("\2\2\2\u00c8\37\3\2\2\2\u00c9\u00ca\t\2\2\2\u00ca!\3\2")
        buf.write("\2\2\u00cb\u00cc\78\2\2\u00cc#\3\2\2\2\u00cd\u00ce\7(")
        buf.write("\2\2\u00ce\u00cf\5\"\22\2\u00cf%\3\2\2\2\u00d0\u00d1\7")
        buf.write("\31\2\2\u00d1\u00d3\7,\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3")
        buf.write("\3\2\2\2\u00d3\u00da\3\2\2\2\u00d4\u00d5\78\2\2\u00d5")
        buf.write("\u00d6\5(\25\2\u00d6\u00d7\7,\2\2\u00d7\u00d9\3\2\2\2")
        buf.write("\u00d8\u00d4\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3")
        buf.write("\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dd\u00de\5\"\22\2\u00de\'\3\2\2\2\u00df\u00e0")
        buf.write("\7!\2\2\u00e0\u00e1\78\2\2\u00e1\u00e3\7\"\2\2\u00e2\u00df")
        buf.write("\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4")
        buf.write("\u00e5\3\2\2\2\u00e5)\3\2\2\2\u00e6\u00e4\3\2\2\2\34-")
        buf.write("8=BJOV\\fiqw{\u0081\u0086\u008c\u0093\u009f\u00a8\u00b2")
        buf.write("\u00bb\u00c4\u00c7\u00d2\u00da\u00e4")
        return buf.getvalue()


class SystemVerilogSymbolParser ( Parser ):

    grammarFileName = "SystemVerilogSymbol.g4"

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
            return self.getToken(SystemVerilogSymbolParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemVerilogSymbolParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(SystemVerilogSymbolParser.DeclarationContext,i)


        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_source

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

        localctx = SystemVerilogSymbolParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_source)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SystemVerilogSymbolParser.T__0) | (1 << SystemVerilogSymbolParser.T__2) | (1 << SystemVerilogSymbolParser.T__4) | (1 << SystemVerilogSymbolParser.T__6) | (1 << SystemVerilogSymbolParser.T__8) | (1 << SystemVerilogSymbolParser.T__10) | (1 << SystemVerilogSymbolParser.T__11) | (1 << SystemVerilogSymbolParser.T__13) | (1 << SystemVerilogSymbolParser.T__15) | (1 << SystemVerilogSymbolParser.T__17))) != 0):
                self.state = 40
                self.declaration()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(SystemVerilogSymbolParser.EOF)
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
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Module_declarationContext,0)


        def interface_declaration(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Interface_declarationContext,0)


        def program_declaration(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Program_declarationContext,0)


        def package_declaration(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Package_declarationContext,0)


        def package_item(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Package_itemContext,0)


        def config_declaration(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Config_declarationContext,0)


        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_declaration

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

        localctx = SystemVerilogSymbolParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SystemVerilogSymbolParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.module_declaration()
                pass
            elif token in [SystemVerilogSymbolParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.interface_declaration()
                pass
            elif token in [SystemVerilogSymbolParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.program_declaration()
                pass
            elif token in [SystemVerilogSymbolParser.T__6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.package_declaration()
                pass
            elif token in [SystemVerilogSymbolParser.T__10, SystemVerilogSymbolParser.T__11, SystemVerilogSymbolParser.T__13, SystemVerilogSymbolParser.T__15, SystemVerilogSymbolParser.T__17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.package_item()
                pass
            elif token in [SystemVerilogSymbolParser.T__8]:
                self.enterOuterAlt(localctx, 6)
                self.state = 53
                self.config_declaration()
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


    class Module_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.IdentifierContext,0)


        def parameter_port_list(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Parameter_port_listContext,0)


        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_module_declaration

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

        localctx = SystemVerilogSymbolParser.Module_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_module_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(SystemVerilogSymbolParser.T__0)
            self.state = 57
            self.identifier()
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 58
                self.parameter_port_list()


            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 61
                    self.matchWildcard() 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 67
            self.match(SystemVerilogSymbolParser.T__1)
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
            return self.getTypedRuleContext(SystemVerilogSymbolParser.IdentifierContext,0)


        def parameter_port_list(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Parameter_port_listContext,0)


        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_interface_declaration

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

        localctx = SystemVerilogSymbolParser.Interface_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_interface_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(SystemVerilogSymbolParser.T__2)
            self.state = 70
            self.identifier()
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 71
                self.parameter_port_list()


            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 74
                    self.matchWildcard() 
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 80
            self.match(SystemVerilogSymbolParser.T__3)
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
            return self.getTypedRuleContext(SystemVerilogSymbolParser.IdentifierContext,0)


        def life_time(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Life_timeContext,0)


        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_program_declaration

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

        localctx = SystemVerilogSymbolParser.Program_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_program_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(SystemVerilogSymbolParser.T__4)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SystemVerilogSymbolParser.T__20 or _la==SystemVerilogSymbolParser.T__21:
                self.state = 83
                self.life_time()


            self.state = 86
            self.identifier()
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 87
                    self.matchWildcard() 
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 93
            self.match(SystemVerilogSymbolParser.T__5)
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
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Package_itemContext,0)


        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_package_declaration

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

        localctx = SystemVerilogSymbolParser.Package_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_package_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(SystemVerilogSymbolParser.T__6)
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 96
                self.package_item()
                pass

            elif la_ == 2:
                self.state = 100
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 97
                        self.matchWildcard() 
                    self.state = 102
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass


            self.state = 105
            self.match(SystemVerilogSymbolParser.T__7)
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


        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_config_declaration

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

        localctx = SystemVerilogSymbolParser.Config_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_config_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(SystemVerilogSymbolParser.T__8)
            self.state = 111
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 108
                    self.matchWildcard() 
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 114
            self.match(SystemVerilogSymbolParser.T__9)
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
            return self.getTypedRuleContext(SystemVerilogSymbolParser.IdentifierContext,0)


        def life_time(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Life_timeContext,0)


        def label(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_class_declaration

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

        localctx = SystemVerilogSymbolParser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SystemVerilogSymbolParser.T__10:
                self.state = 116
                self.match(SystemVerilogSymbolParser.T__10)


            self.state = 119
            self.match(SystemVerilogSymbolParser.T__11)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SystemVerilogSymbolParser.T__20 or _la==SystemVerilogSymbolParser.T__21:
                self.state = 120
                self.life_time()


            self.state = 123
            self.identifier()
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 124
                    self.matchWildcard() 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 130
            self.match(SystemVerilogSymbolParser.T__12)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SystemVerilogSymbolParser.Colon:
                self.state = 131
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
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Task_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Function_declarationContext,0)


        def class_declaration(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Class_declarationContext,0)


        def type_declaration(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Type_declarationContext,0)


        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_package_item

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

        localctx = SystemVerilogSymbolParser.Package_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_package_item)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SystemVerilogSymbolParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.task_declaration()
                pass
            elif token in [SystemVerilogSymbolParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.function_declaration()
                pass
            elif token in [SystemVerilogSymbolParser.T__10, SystemVerilogSymbolParser.T__11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.class_declaration()
                pass
            elif token in [SystemVerilogSymbolParser.T__17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 137
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
            return self.getTypedRuleContext(SystemVerilogSymbolParser.IdentifierContext,0)


        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_task_declaration

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

        localctx = SystemVerilogSymbolParser.Task_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_task_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(SystemVerilogSymbolParser.T__13)
            self.state = 141
            self.identifier()
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 142
                    self.matchWildcard() 
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 148
            self.match(SystemVerilogSymbolParser.T__14)
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
            return self.getTypedRuleContext(SystemVerilogSymbolParser.Return_valContext,0)


        def identifier(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.IdentifierContext,0)


        def OpenParen(self):
            return self.getToken(SystemVerilogSymbolParser.OpenParen, 0)

        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_function_declaration

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

        localctx = SystemVerilogSymbolParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(SystemVerilogSymbolParser.T__15)
            self.state = 151
            self.return_val()
            self.state = 152
            self.identifier()
            self.state = 153
            self.match(SystemVerilogSymbolParser.OpenParen)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 154
                    self.matchWildcard() 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 160
            self.match(SystemVerilogSymbolParser.T__16)
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
            return self.getTypedRuleContext(SystemVerilogSymbolParser.IdentifierContext,0)


        def SemiColon(self):
            return self.getToken(SystemVerilogSymbolParser.SemiColon, 0)

        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_type_declaration

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

        localctx = SystemVerilogSymbolParser.Type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(SystemVerilogSymbolParser.T__17)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 163
                    self.matchWildcard() 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 169
            self.identifier()
            self.state = 170
            self.match(SystemVerilogSymbolParser.SemiColon)
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
            return self.getToken(SystemVerilogSymbolParser.CloseParen, 0)

        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_parameter_port_list

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

        localctx = SystemVerilogSymbolParser.Parameter_port_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter_port_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(SystemVerilogSymbolParser.T__18)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 173
                    self.matchWildcard() 
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 179
            self.match(SystemVerilogSymbolParser.CloseParen)
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
            return self.getToken(SystemVerilogSymbolParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SystemVerilogSymbolParser.CloseParen, 0)

        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_port_list

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

        localctx = SystemVerilogSymbolParser.Port_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_port_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(SystemVerilogSymbolParser.OpenParen)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 182
                    self.matchWildcard() 
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 188
            self.match(SystemVerilogSymbolParser.CloseParen)
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
            return SystemVerilogSymbolParser.RULE_return_val

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

        localctx = SystemVerilogSymbolParser.Return_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_return_val)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(SystemVerilogSymbolParser.T__19)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 191
                        self.matchWildcard() 
                    self.state = 196
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
            return SystemVerilogSymbolParser.RULE_life_time

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

        localctx = SystemVerilogSymbolParser.Life_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_life_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            _la = self._input.LA(1)
            if not(_la==SystemVerilogSymbolParser.T__20 or _la==SystemVerilogSymbolParser.T__21):
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
            return self.getToken(SystemVerilogSymbolParser.Word, 0)

        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_identifier

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

        localctx = SystemVerilogSymbolParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(SystemVerilogSymbolParser.Word)
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
            return self.getToken(SystemVerilogSymbolParser.Colon, 0)

        def identifier(self):
            return self.getTypedRuleContext(SystemVerilogSymbolParser.IdentifierContext,0)


        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_label

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

        localctx = SystemVerilogSymbolParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(SystemVerilogSymbolParser.Colon)
            self.state = 204
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
            return self.getTypedRuleContext(SystemVerilogSymbolParser.IdentifierContext,0)


        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(SystemVerilogSymbolParser.Dot)
            else:
                return self.getToken(SystemVerilogSymbolParser.Dot, i)

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(SystemVerilogSymbolParser.Word)
            else:
                return self.getToken(SystemVerilogSymbolParser.Word, i)

        def constant_bit_select(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemVerilogSymbolParser.Constant_bit_selectContext)
            else:
                return self.getTypedRuleContext(SystemVerilogSymbolParser.Constant_bit_selectContext,i)


        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_hierarchical_identifier

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

        localctx = SystemVerilogSymbolParser.Hierarchical_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_hierarchical_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SystemVerilogSymbolParser.T__22:
                self.state = 206
                self.match(SystemVerilogSymbolParser.T__22)
                self.state = 207
                self.match(SystemVerilogSymbolParser.Dot)


            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 210
                    self.match(SystemVerilogSymbolParser.Word)
                    self.state = 211
                    self.constant_bit_select()
                    self.state = 212
                    self.match(SystemVerilogSymbolParser.Dot) 
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 219
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
                return self.getTokens(SystemVerilogSymbolParser.OpenBracket)
            else:
                return self.getToken(SystemVerilogSymbolParser.OpenBracket, i)

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(SystemVerilogSymbolParser.Word)
            else:
                return self.getToken(SystemVerilogSymbolParser.Word, i)

        def CloseBracket(self, i:int=None):
            if i is None:
                return self.getTokens(SystemVerilogSymbolParser.CloseBracket)
            else:
                return self.getToken(SystemVerilogSymbolParser.CloseBracket, i)

        def getRuleIndex(self):
            return SystemVerilogSymbolParser.RULE_constant_bit_select

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

        localctx = SystemVerilogSymbolParser.Constant_bit_selectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_constant_bit_select)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SystemVerilogSymbolParser.OpenBracket:
                self.state = 221
                self.match(SystemVerilogSymbolParser.OpenBracket)
                self.state = 222
                self.match(SystemVerilogSymbolParser.Word)
                self.state = 223
                self.match(SystemVerilogSymbolParser.CloseBracket)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





