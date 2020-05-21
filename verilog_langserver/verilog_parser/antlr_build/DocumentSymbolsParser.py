# Generated from C:\Users\eirik\Desktop\verilog-langserver\verilog_langserver\verilog_parser/grammar/DocumentSymbols.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0182\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\6\2\65\n\2\r\2\16\2\66\7\29\n\2\f\2\16\2")
        buf.write("<\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3G\n\3\3")
        buf.write("\4\3\4\3\4\5\4L\n\4\3\4\7\4O\n\4\f\4\16\4R\13\4\3\4\3")
        buf.write("\4\5\4V\n\4\3\5\3\5\3\5\5\5[\n\5\3\5\7\5^\n\5\f\5\16\5")
        buf.write("a\13\5\3\5\3\5\5\5e\n\5\3\6\3\6\5\6i\n\6\3\6\3\6\7\6m")
        buf.write("\n\6\f\6\16\6p\13\6\3\6\3\6\5\6t\n\6\3\7\3\7\3\7\7\7y")
        buf.write("\n\7\f\7\16\7|\13\7\3\7\3\7\5\7\u0080\n\7\3\b\3\b\3\b")
        buf.write("\7\b\u0085\n\b\f\b\16\b\u0088\13\b\3\b\3\b\5\b\u008c\n")
        buf.write("\b\3\t\3\t\3\t\7\t\u0091\n\t\f\t\16\t\u0094\13\t\3\t\3")
        buf.write("\t\5\t\u0098\n\t\3\n\5\n\u009b\n\n\3\n\3\n\5\n\u009f\n")
        buf.write("\n\3\n\3\n\3\n\3\n\7\n\u00a5\n\n\f\n\16\n\u00a8\13\n\5")
        buf.write("\n\u00aa\n\n\3\n\3\n\3\n\5\n\u00af\n\n\3\n\3\n\3\n\5\n")
        buf.write("\u00b4\n\n\7\n\u00b6\n\n\f\n\16\n\u00b9\13\n\5\n\u00bb")
        buf.write("\n\n\3\n\3\n\7\n\u00bf\n\n\f\n\16\n\u00c2\13\n\3\n\3\n")
        buf.write("\5\n\u00c6\n\n\3\13\3\13\3\13\3\13\3\13\3\13\6\13\u00ce")
        buf.write("\n\13\r\13\16\13\u00cf\5\13\u00d2\n\13\3\f\3\f\3\f\7\f")
        buf.write("\u00d7\n\f\f\f\16\f\u00da\13\f\3\f\3\f\5\f\u00de\n\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\7\r\u00e5\n\r\f\r\16\r\u00e8\13\r\3")
        buf.write("\r\3\r\5\r\u00ec\n\r\3\16\3\16\7\16\u00f0\n\16\f\16\16")
        buf.write("\16\u00f3\13\16\3\16\3\16\3\16\3\17\3\17\7\17\u00fa\n")
        buf.write("\17\f\17\16\17\u00fd\13\17\3\17\3\17\3\20\3\20\7\20\u0103")
        buf.write("\n\20\f\20\16\20\u0106\13\20\3\20\3\20\3\21\3\21\7\21")
        buf.write("\u010c\n\21\f\21\16\21\u010f\13\21\5\21\u0111\n\21\3\22")
        buf.write("\3\22\3\23\3\23\3\23\7\23\u0118\n\23\f\23\16\23\u011b")
        buf.write("\13\23\3\23\3\23\3\24\3\24\5\24\u0121\n\24\3\24\3\24\3")
        buf.write("\24\7\24\u0126\n\24\f\24\16\24\u0129\13\24\3\24\7\24\u012c")
        buf.write("\n\24\f\24\16\24\u012f\13\24\3\24\5\24\u0132\n\24\3\24")
        buf.write("\3\24\3\24\3\24\7\24\u0138\n\24\f\24\16\24\u013b\13\24")
        buf.write("\3\24\7\24\u013e\n\24\f\24\16\24\u0141\13\24\3\24\5\24")
        buf.write("\u0144\n\24\7\24\u0146\n\24\f\24\16\24\u0149\13\24\3\24")
        buf.write("\3\24\3\24\6\24\u014e\n\24\r\24\16\24\u014f\5\24\u0152")
        buf.write("\n\24\3\25\3\25\5\25\u0156\n\25\3\25\3\25\3\25\7\25\u015b")
        buf.write("\n\25\f\25\16\25\u015e\13\25\3\25\7\25\u0161\n\25\f\25")
        buf.write("\16\25\u0164\13\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\5\30\u016d\n\30\3\30\3\30\3\30\3\30\7\30\u0173\n\30\f")
        buf.write("\30\16\30\u0176\13\30\3\30\3\30\3\31\3\31\3\31\7\31\u017d")
        buf.write("\n\31\f\31\16\31\u0180\13\31\3\31\27\66P_nz\u0086\u0092")
        buf.write("\u00a6\u00c0\u00cf\u00d8\u00e6\u00f1\u00fb\u0104\u010d")
        buf.write("\u0119\u0127\u0139\u014f\u015c\2\32\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\2\3\3\2\7\b\2\u01ab")
        buf.write("\2:\3\2\2\2\4F\3\2\2\2\6H\3\2\2\2\bW\3\2\2\2\nf\3\2\2")
        buf.write("\2\fu\3\2\2\2\16\u0081\3\2\2\2\20\u008d\3\2\2\2\22\u009a")
        buf.write("\3\2\2\2\24\u00d1\3\2\2\2\26\u00d3\3\2\2\2\30\u00df\3")
        buf.write("\2\2\2\32\u00ed\3\2\2\2\34\u00f7\3\2\2\2\36\u0100\3\2")
        buf.write("\2\2 \u0110\3\2\2\2\"\u0112\3\2\2\2$\u0114\3\2\2\2&\u0151")
        buf.write("\3\2\2\2(\u0155\3\2\2\2*\u0165\3\2\2\2,\u0167\3\2\2\2")
        buf.write(".\u016c\3\2\2\2\60\u017e\3\2\2\2\629\5\4\3\2\63\65\13")
        buf.write("\2\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\66\64")
        buf.write("\3\2\2\2\679\3\2\2\28\62\3\2\2\28\64\3\2\2\29<\3\2\2\2")
        buf.write(":8\3\2\2\2:;\3\2\2\2;=\3\2\2\2<:\3\2\2\2=>\7\2\2\3>\3")
        buf.write("\3\2\2\2?G\5\6\4\2@G\5\b\5\2AG\5\n\6\2BG\5\f\7\2CG\5\16")
        buf.write("\b\2DG\5\20\t\2EG\5\24\13\2F?\3\2\2\2F@\3\2\2\2FA\3\2")
        buf.write("\2\2FB\3\2\2\2FC\3\2\2\2FD\3\2\2\2FE\3\2\2\2G\5\3\2\2")
        buf.write("\2HI\7!\2\2IK\5*\26\2JL\5\34\17\2KJ\3\2\2\2KL\3\2\2\2")
        buf.write("LP\3\2\2\2MO\5\24\13\2NM\3\2\2\2OR\3\2\2\2PQ\3\2\2\2P")
        buf.write("N\3\2\2\2QS\3\2\2\2RP\3\2\2\2SU\7\"\2\2TV\5,\27\2UT\3")
        buf.write("\2\2\2UV\3\2\2\2V\7\3\2\2\2WX\7#\2\2XZ\5*\26\2Y[\5\34")
        buf.write("\17\2ZY\3\2\2\2Z[\3\2\2\2[_\3\2\2\2\\^\5\24\13\2]\\\3")
        buf.write("\2\2\2^a\3\2\2\2_`\3\2\2\2_]\3\2\2\2`b\3\2\2\2a_\3\2\2")
        buf.write("\2bd\7$\2\2ce\5,\27\2dc\3\2\2\2de\3\2\2\2e\t\3\2\2\2f")
        buf.write("h\7+\2\2gi\5\"\22\2hg\3\2\2\2hi\3\2\2\2ij\3\2\2\2jn\5")
        buf.write("*\26\2km\5\24\13\2lk\3\2\2\2mp\3\2\2\2no\3\2\2\2nl\3\2")
        buf.write("\2\2oq\3\2\2\2pn\3\2\2\2qs\7,\2\2rt\5,\27\2sr\3\2\2\2")
        buf.write("st\3\2\2\2t\13\3\2\2\2uv\7\61\2\2vz\5*\26\2wy\5\24\13")
        buf.write("\2xw\3\2\2\2y|\3\2\2\2z{\3\2\2\2zx\3\2\2\2{}\3\2\2\2|")
        buf.write("z\3\2\2\2}\177\7\62\2\2~\u0080\5,\27\2\177~\3\2\2\2\177")
        buf.write("\u0080\3\2\2\2\u0080\r\3\2\2\2\u0081\u0082\7\'\2\2\u0082")
        buf.write("\u0086\5*\26\2\u0083\u0085\5\24\13\2\u0084\u0083\3\2\2")
        buf.write("\2\u0085\u0088\3\2\2\2\u0086\u0087\3\2\2\2\u0086\u0084")
        buf.write("\3\2\2\2\u0087\u0089\3\2\2\2\u0088\u0086\3\2\2\2\u0089")
        buf.write("\u008b\7(\2\2\u008a\u008c\5,\27\2\u008b\u008a\3\2\2\2")
        buf.write("\u008b\u008c\3\2\2\2\u008c\17\3\2\2\2\u008d\u008e\7)\2")
        buf.write("\2\u008e\u0092\5*\26\2\u008f\u0091\5\24\13\2\u0090\u008f")
        buf.write("\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0093\3\2\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0093\u0095\3\2\2\2\u0094\u0092\3\2\2\2")
        buf.write("\u0095\u0097\7*\2\2\u0096\u0098\5,\27\2\u0097\u0096\3")
        buf.write("\2\2\2\u0097\u0098\3\2\2\2\u0098\21\3\2\2\2\u0099\u009b")
        buf.write("\7\65\2\2\u009a\u0099\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009c\u009e\7%\2\2\u009d\u009f\5\"\22\2")
        buf.write("\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3")
        buf.write("\2\2\2\u00a0\u00a9\5*\26\2\u00a1\u00a2\7\3\2\2\u00a2\u00a6")
        buf.write("\5(\25\2\u00a3\u00a5\13\2\2\2\u00a4\u00a3\3\2\2\2\u00a5")
        buf.write("\u00a8\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2")
        buf.write("\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00a1\3")
        buf.write("\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ba\3\2\2\2\u00ab\u00ac")
        buf.write("\7\4\2\2\u00ac\u00ae\5(\25\2\u00ad\u00af\5\34\17\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b7\3\2\2\2")
        buf.write("\u00b0\u00b1\7\33\2\2\u00b1\u00b3\5(\25\2\u00b2\u00b4")
        buf.write("\5\34\17\2\u00b3\u00b2\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write("\u00b6\3\2\2\2\u00b5\u00b0\3\2\2\2\u00b6\u00b9\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00bb\3")
        buf.write("\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00ab\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00c0\7\31\2\2\u00bd")
        buf.write("\u00bf\5\24\13\2\u00be\u00bd\3\2\2\2\u00bf\u00c2\3\2\2")
        buf.write("\2\u00c0\u00c1\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c3")
        buf.write("\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c5\7&\2\2\u00c4")
        buf.write("\u00c6\5,\27\2\u00c5\u00c4\3\2\2\2\u00c5\u00c6\3\2\2\2")
        buf.write("\u00c6\23\3\2\2\2\u00c7\u00d2\5\26\f\2\u00c8\u00d2\5\30")
        buf.write("\r\2\u00c9\u00d2\5\22\n\2\u00ca\u00d2\5\32\16\2\u00cb")
        buf.write("\u00d2\5&\24\2\u00cc\u00ce\13\2\2\2\u00cd\u00cc\3\2\2")
        buf.write("\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\3\2\2\2\u00cf\u00cd")
        buf.write("\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00c7\3\2\2\2\u00d1")
        buf.write("\u00c8\3\2\2\2\u00d1\u00c9\3\2\2\2\u00d1\u00ca\3\2\2\2")
        buf.write("\u00d1\u00cb\3\2\2\2\u00d1\u00cd\3\2\2\2\u00d2\25\3\2")
        buf.write("\2\2\u00d3\u00d4\7-\2\2\u00d4\u00d8\5*\26\2\u00d5\u00d7")
        buf.write("\13\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00db\3\2\2\2")
        buf.write("\u00da\u00d8\3\2\2\2\u00db\u00dd\7.\2\2\u00dc\u00de\5")
        buf.write(",\27\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\27")
        buf.write("\3\2\2\2\u00df\u00e0\7/\2\2\u00e0\u00e1\5 \21\2\u00e1")
        buf.write("\u00e2\5*\26\2\u00e2\u00e6\7\25\2\2\u00e3\u00e5\13\2\2")
        buf.write("\2\u00e4\u00e3\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6\u00e7")
        buf.write("\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e9\3\2\2\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e9\u00eb\7\60\2\2\u00ea\u00ec\5,\27")
        buf.write("\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\31\3")
        buf.write("\2\2\2\u00ed\u00f1\7\66\2\2\u00ee\u00f0\13\2\2\2\u00ef")
        buf.write("\u00ee\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f1\u00ef\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00f1\3")
        buf.write("\2\2\2\u00f4\u00f5\5*\26\2\u00f5\u00f6\7\31\2\2\u00f6")
        buf.write("\33\3\2\2\2\u00f7\u00fb\7\5\2\2\u00f8\u00fa\13\2\2\2\u00f9")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00fb\3")
        buf.write("\2\2\2\u00fe\u00ff\7\26\2\2\u00ff\35\3\2\2\2\u0100\u0104")
        buf.write("\7\25\2\2\u0101\u0103\13\2\2\2\u0102\u0101\3\2\2\2\u0103")
        buf.write("\u0106\3\2\2\2\u0104\u0105\3\2\2\2\u0104\u0102\3\2\2\2")
        buf.write("\u0105\u0107\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108\7")
        buf.write("\26\2\2\u0108\37\3\2\2\2\u0109\u0111\7\6\2\2\u010a\u010c")
        buf.write("\13\2\2\2\u010b\u010a\3\2\2\2\u010c\u010f\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u0111\3\2\2\2")
        buf.write("\u010f\u010d\3\2\2\2\u0110\u0109\3\2\2\2\u0110\u010d\3")
        buf.write("\2\2\2\u0111!\3\2\2\2\u0112\u0113\t\2\2\2\u0113#\3\2\2")
        buf.write("\2\u0114\u0115\7\25\2\2\u0115\u0119\7\t\2\2\u0116\u0118")
        buf.write("\13\2\2\2\u0117\u0116\3\2\2\2\u0118\u011b\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011c\3\2\2\2")
        buf.write("\u011b\u0119\3\2\2\2\u011c\u011d\7\26\2\2\u011d%\3\2\2")
        buf.write("\2\u011e\u0120\5(\25\2\u011f\u0121\5\34\17\2\u0120\u011f")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\3\2\2\2\u0122")
        buf.write("\u012d\5*\26\2\u0123\u0127\7\23\2\2\u0124\u0126\13\2\2")
        buf.write("\2\u0125\u0124\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0128")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u012a\3\2\2\2\u0129")
        buf.write("\u0127\3\2\2\2\u012a\u012c\7\24\2\2\u012b\u0123\3\2\2")
        buf.write("\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e")
        buf.write("\3\2\2\2\u012e\u0131\3\2\2\2\u012f\u012d\3\2\2\2\u0130")
        buf.write("\u0132\5\36\20\2\u0131\u0130\3\2\2\2\u0131\u0132\3\2\2")
        buf.write("\2\u0132\u0147\3\2\2\2\u0133\u0134\7\33\2\2\u0134\u013f")
        buf.write("\5*\26\2\u0135\u0139\7\23\2\2\u0136\u0138\13\2\2\2\u0137")
        buf.write("\u0136\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u013a\3\2\2\2")
        buf.write("\u0139\u0137\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u0139\3")
        buf.write("\2\2\2\u013c\u013e\7\24\2\2\u013d\u0135\3\2\2\2\u013e")
        buf.write("\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2")
        buf.write("\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0144\5")
        buf.write("\36\20\2\u0143\u0142\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("\u0146\3\2\2\2\u0145\u0133\3\2\2\2\u0146\u0149\3\2\2\2")
        buf.write("\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u014a\3")
        buf.write("\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b\7\31\2\2\u014b")
        buf.write("\u0152\3\2\2\2\u014c\u014e\13\2\2\2\u014d\u014c\3\2\2")
        buf.write("\2\u014e\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u014f\u014d")
        buf.write("\3\2\2\2\u0150\u0152\3\2\2\2\u0151\u011e\3\2\2\2\u0151")
        buf.write("\u014d\3\2\2\2\u0152\'\3\2\2\2\u0153\u0154\7A\2\2\u0154")
        buf.write("\u0156\7\n\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156\u0157\3\2\2\2\u0157\u0162\7A\2\2\u0158\u015c\7")
        buf.write("\23\2\2\u0159\u015b\13\2\2\2\u015a\u0159\3\2\2\2\u015b")
        buf.write("\u015e\3\2\2\2\u015c\u015d\3\2\2\2\u015c\u015a\3\2\2\2")
        buf.write("\u015d\u015f\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0161\7")
        buf.write("\24\2\2\u0160\u0158\3\2\2\2\u0161\u0164\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163)\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0165\u0166\7A\2\2\u0166+\3\2\2\2\u0167")
        buf.write("\u0168\7\32\2\2\u0168\u0169\5*\26\2\u0169-\3\2\2\2\u016a")
        buf.write("\u016b\7\13\2\2\u016b\u016d\7\36\2\2\u016c\u016a\3\2\2")
        buf.write("\2\u016c\u016d\3\2\2\2\u016d\u0174\3\2\2\2\u016e\u016f")
        buf.write("\7A\2\2\u016f\u0170\5\60\31\2\u0170\u0171\7\36\2\2\u0171")
        buf.write("\u0173\3\2\2\2\u0172\u016e\3\2\2\2\u0173\u0176\3\2\2\2")
        buf.write("\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0177\3")
        buf.write("\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\5*\26\2\u0178/")
        buf.write("\3\2\2\2\u0179\u017a\7\23\2\2\u017a\u017b\7A\2\2\u017b")
        buf.write("\u017d\7\24\2\2\u017c\u0179\3\2\2\2\u017d\u0180\3\2\2")
        buf.write("\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\61\3")
        buf.write("\2\2\2\u0180\u017e\3\2\2\2;\668:FKPUZ_dhnsz\177\u0086")
        buf.write("\u008b\u0092\u0097\u009a\u009e\u00a6\u00a9\u00ae\u00b3")
        buf.write("\u00b7\u00ba\u00c0\u00c5\u00cf\u00d1\u00d8\u00dd\u00e6")
        buf.write("\u00eb\u00f1\u00fb\u0104\u010d\u0110\u0119\u0120\u0127")
        buf.write("\u012d\u0131\u0139\u013f\u0143\u0147\u014f\u0151\u0155")
        buf.write("\u015c\u0162\u016c\u0174\u017e")
        return buf.getvalue()


class DocumentSymbolsParser ( Parser ):

    grammarFileName = "DocumentSymbols.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'extends'", "'implements'", "'#('", "'void'", 
                     "'static'", "'automatic'", "'*'", "'::'", "'$root'", 
                     "<INVALID>", "<INVALID>", "' '", "'\t'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'['", "']'", "'('", "')'", 
                     "'{'", "'}'", "';'", "':'", "','", "'='", "'?'", "'.'", 
                     "<INVALID>", "<INVALID>", "'module'", "'endmodule'", 
                     "'interface'", "'endinterface'", "'class'", "'endclass'", 
                     "'config'", "'endconfig'", "'primitive'", "'endprimitive'", 
                     "'program'", "'endprogram'", "'task'", "'endtask'", 
                     "'function'", "'endfunction'", "'package'", "'endpackage'", 
                     "'input'", "'output'", "'virtual'", "'typedef'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SINGLELINE_COMMENT", "MULTILINE_COMMENT", 
                      "SPACE", "TAB", "NEWLINE", "String", "COMPILER_DIRECTIVE", 
                      "OpenBracket", "CloseBracket", "OpenParen", "CloseParen", 
                      "OpenBrace", "CloseBrace", "SemiColon", "Colon", "Comma", 
                      "Assign", "QuestionMark", "Dot", "Apostrophe", "Operators", 
                      "Module", "Endmodule", "Interface", "Endinterface", 
                      "Class", "Endclass", "Config", "Endconfig", "Primitive", 
                      "Endprimitive", "Program", "Endprogram", "Task", "Endtask", 
                      "Function", "Endfunction", "Package", "Endpackage", 
                      "Input", "Output", "Virtual", "Typedef", "Number", 
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
    RULE_udp_declaration = 7
    RULE_class_declaration = 8
    RULE_item = 9
    RULE_task_declaration = 10
    RULE_function_declaration = 11
    RULE_type_declaration = 12
    RULE_parameter_list = 13
    RULE_port_list = 14
    RULE_return_val = 15
    RULE_life_time = 16
    RULE_attribute = 17
    RULE_instantiation = 18
    RULE_type_identifier = 19
    RULE_identifier = 20
    RULE_label = 21
    RULE_hierarchical_identifier = 22
    RULE_constant_bit_select = 23

    ruleNames =  [ "source", "declaration", "module_declaration", "interface_declaration", 
                   "program_declaration", "package_declaration", "config_declaration", 
                   "udp_declaration", "class_declaration", "item", "task_declaration", 
                   "function_declaration", "type_declaration", "parameter_list", 
                   "port_list", "return_val", "life_time", "attribute", 
                   "instantiation", "type_identifier", "identifier", "label", 
                   "hierarchical_identifier", "constant_bit_select" ]

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
    SINGLELINE_COMMENT=10
    MULTILINE_COMMENT=11
    SPACE=12
    TAB=13
    NEWLINE=14
    String=15
    COMPILER_DIRECTIVE=16
    OpenBracket=17
    CloseBracket=18
    OpenParen=19
    CloseParen=20
    OpenBrace=21
    CloseBrace=22
    SemiColon=23
    Colon=24
    Comma=25
    Assign=26
    QuestionMark=27
    Dot=28
    Apostrophe=29
    Operators=30
    Module=31
    Endmodule=32
    Interface=33
    Endinterface=34
    Class=35
    Endclass=36
    Config=37
    Endconfig=38
    Primitive=39
    Endprimitive=40
    Program=41
    Endprogram=42
    Task=43
    Endtask=44
    Function=45
    Endfunction=46
    Package=47
    Endpackage=48
    Input=49
    Output=50
    Virtual=51
    Typedef=52
    Number=53
    IntegralNumber=54
    RealNumber=55
    UnsignedNumber=56
    DecimalNumber=57
    BinaryNumber=58
    OctalNumber=59
    HexNumber=60
    UnbasedUnsizedLiteral=61
    Time=62
    Word=63

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
            return self.getToken(DocumentSymbolsParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.DeclarationContext,i)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_source

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSource" ):
                return visitor.visitSource(self)
            else:
                return visitor.visitChildren(self)




    def source(self):

        localctx = DocumentSymbolsParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_source)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DocumentSymbolsParser.T__0) | (1 << DocumentSymbolsParser.T__1) | (1 << DocumentSymbolsParser.T__2) | (1 << DocumentSymbolsParser.T__3) | (1 << DocumentSymbolsParser.T__4) | (1 << DocumentSymbolsParser.T__5) | (1 << DocumentSymbolsParser.T__6) | (1 << DocumentSymbolsParser.T__7) | (1 << DocumentSymbolsParser.T__8) | (1 << DocumentSymbolsParser.SINGLELINE_COMMENT) | (1 << DocumentSymbolsParser.MULTILINE_COMMENT) | (1 << DocumentSymbolsParser.SPACE) | (1 << DocumentSymbolsParser.TAB) | (1 << DocumentSymbolsParser.NEWLINE) | (1 << DocumentSymbolsParser.String) | (1 << DocumentSymbolsParser.COMPILER_DIRECTIVE) | (1 << DocumentSymbolsParser.OpenBracket) | (1 << DocumentSymbolsParser.CloseBracket) | (1 << DocumentSymbolsParser.OpenParen) | (1 << DocumentSymbolsParser.CloseParen) | (1 << DocumentSymbolsParser.OpenBrace) | (1 << DocumentSymbolsParser.CloseBrace) | (1 << DocumentSymbolsParser.SemiColon) | (1 << DocumentSymbolsParser.Colon) | (1 << DocumentSymbolsParser.Comma) | (1 << DocumentSymbolsParser.Assign) | (1 << DocumentSymbolsParser.QuestionMark) | (1 << DocumentSymbolsParser.Dot) | (1 << DocumentSymbolsParser.Apostrophe) | (1 << DocumentSymbolsParser.Operators) | (1 << DocumentSymbolsParser.Module) | (1 << DocumentSymbolsParser.Endmodule) | (1 << DocumentSymbolsParser.Interface) | (1 << DocumentSymbolsParser.Endinterface) | (1 << DocumentSymbolsParser.Class) | (1 << DocumentSymbolsParser.Endclass) | (1 << DocumentSymbolsParser.Config) | (1 << DocumentSymbolsParser.Endconfig) | (1 << DocumentSymbolsParser.Primitive) | (1 << DocumentSymbolsParser.Endprimitive) | (1 << DocumentSymbolsParser.Program) | (1 << DocumentSymbolsParser.Endprogram) | (1 << DocumentSymbolsParser.Task) | (1 << DocumentSymbolsParser.Endtask) | (1 << DocumentSymbolsParser.Function) | (1 << DocumentSymbolsParser.Endfunction) | (1 << DocumentSymbolsParser.Package) | (1 << DocumentSymbolsParser.Endpackage) | (1 << DocumentSymbolsParser.Input) | (1 << DocumentSymbolsParser.Output) | (1 << DocumentSymbolsParser.Virtual) | (1 << DocumentSymbolsParser.Typedef) | (1 << DocumentSymbolsParser.Number) | (1 << DocumentSymbolsParser.IntegralNumber) | (1 << DocumentSymbolsParser.RealNumber) | (1 << DocumentSymbolsParser.UnsignedNumber) | (1 << DocumentSymbolsParser.DecimalNumber) | (1 << DocumentSymbolsParser.BinaryNumber) | (1 << DocumentSymbolsParser.OctalNumber) | (1 << DocumentSymbolsParser.HexNumber) | (1 << DocumentSymbolsParser.UnbasedUnsizedLiteral) | (1 << DocumentSymbolsParser.Time) | (1 << DocumentSymbolsParser.Word))) != 0):
                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 48
                    self.declaration()
                    pass

                elif la_ == 2:
                    self.state = 50 
                    self._errHandler.sync(self)
                    _alt = 1+1
                    while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1+1:
                            self.state = 49
                            self.matchWildcard()

                        else:
                            raise NoViableAltException(self)
                        self.state = 52 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                    pass


                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(DocumentSymbolsParser.EOF)
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
            return self.getTypedRuleContext(DocumentSymbolsParser.Module_declarationContext,0)


        def interface_declaration(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Interface_declarationContext,0)


        def program_declaration(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Program_declarationContext,0)


        def package_declaration(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Package_declarationContext,0)


        def config_declaration(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Config_declarationContext,0)


        def udp_declaration(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Udp_declarationContext,0)


        def item(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.ItemContext,0)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = DocumentSymbolsParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.module_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.interface_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.program_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.package_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                self.config_declaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.udp_declaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 67
                self.item()
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

        def Module(self):
            return self.getToken(DocumentSymbolsParser.Module, 0)

        def identifier(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,0)


        def Endmodule(self):
            return self.getToken(DocumentSymbolsParser.Endmodule, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Parameter_listContext,0)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.ItemContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.ItemContext,i)


        def label(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.LabelContext,0)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_module_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule_declaration" ):
                return visitor.visitModule_declaration(self)
            else:
                return visitor.visitChildren(self)




    def module_declaration(self):

        localctx = DocumentSymbolsParser.Module_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_module_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(DocumentSymbolsParser.Module)
            self.state = 71
            self.identifier()
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 72
                self.parameter_list()


            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 75
                    self.item() 
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 81
            self.match(DocumentSymbolsParser.Endmodule)
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 82
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

        def Interface(self):
            return self.getToken(DocumentSymbolsParser.Interface, 0)

        def identifier(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,0)


        def Endinterface(self):
            return self.getToken(DocumentSymbolsParser.Endinterface, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Parameter_listContext,0)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.ItemContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.ItemContext,i)


        def label(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.LabelContext,0)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_interface_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declaration" ):
                return visitor.visitInterface_declaration(self)
            else:
                return visitor.visitChildren(self)




    def interface_declaration(self):

        localctx = DocumentSymbolsParser.Interface_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_interface_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(DocumentSymbolsParser.Interface)
            self.state = 86
            self.identifier()
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 87
                self.parameter_list()


            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 90
                    self.item() 
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 96
            self.match(DocumentSymbolsParser.Endinterface)
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 97
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

        def Program(self):
            return self.getToken(DocumentSymbolsParser.Program, 0)

        def identifier(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,0)


        def Endprogram(self):
            return self.getToken(DocumentSymbolsParser.Endprogram, 0)

        def life_time(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Life_timeContext,0)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.ItemContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.ItemContext,i)


        def label(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.LabelContext,0)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_program_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_declaration" ):
                return visitor.visitProgram_declaration(self)
            else:
                return visitor.visitChildren(self)




    def program_declaration(self):

        localctx = DocumentSymbolsParser.Program_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_program_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(DocumentSymbolsParser.Program)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DocumentSymbolsParser.T__4 or _la==DocumentSymbolsParser.T__5:
                self.state = 101
                self.life_time()


            self.state = 104
            self.identifier()
            self.state = 108
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 105
                    self.item() 
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 111
            self.match(DocumentSymbolsParser.Endprogram)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 112
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

        def Package(self):
            return self.getToken(DocumentSymbolsParser.Package, 0)

        def identifier(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,0)


        def Endpackage(self):
            return self.getToken(DocumentSymbolsParser.Endpackage, 0)

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.ItemContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.ItemContext,i)


        def label(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.LabelContext,0)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_package_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackage_declaration" ):
                return visitor.visitPackage_declaration(self)
            else:
                return visitor.visitChildren(self)




    def package_declaration(self):

        localctx = DocumentSymbolsParser.Package_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_package_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(DocumentSymbolsParser.Package)
            self.state = 116
            self.identifier()
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 117
                    self.item() 
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 123
            self.match(DocumentSymbolsParser.Endpackage)
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 124
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

        def Config(self):
            return self.getToken(DocumentSymbolsParser.Config, 0)

        def identifier(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,0)


        def Endconfig(self):
            return self.getToken(DocumentSymbolsParser.Endconfig, 0)

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.ItemContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.ItemContext,i)


        def label(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.LabelContext,0)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_config_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfig_declaration" ):
                return visitor.visitConfig_declaration(self)
            else:
                return visitor.visitChildren(self)




    def config_declaration(self):

        localctx = DocumentSymbolsParser.Config_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_config_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(DocumentSymbolsParser.Config)
            self.state = 128
            self.identifier()
            self.state = 132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 129
                    self.item() 
                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 135
            self.match(DocumentSymbolsParser.Endconfig)
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 136
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Udp_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Primitive(self):
            return self.getToken(DocumentSymbolsParser.Primitive, 0)

        def identifier(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,0)


        def Endprimitive(self):
            return self.getToken(DocumentSymbolsParser.Endprimitive, 0)

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.ItemContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.ItemContext,i)


        def label(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.LabelContext,0)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_udp_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUdp_declaration" ):
                return visitor.visitUdp_declaration(self)
            else:
                return visitor.visitChildren(self)




    def udp_declaration(self):

        localctx = DocumentSymbolsParser.Udp_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_udp_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(DocumentSymbolsParser.Primitive)
            self.state = 140
            self.identifier()
            self.state = 144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 141
                    self.item() 
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 147
            self.match(DocumentSymbolsParser.Endprimitive)
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 148
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

        def Class(self):
            return self.getToken(DocumentSymbolsParser.Class, 0)

        def identifier(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,0)


        def SemiColon(self):
            return self.getToken(DocumentSymbolsParser.SemiColon, 0)

        def Endclass(self):
            return self.getToken(DocumentSymbolsParser.Endclass, 0)

        def Virtual(self):
            return self.getToken(DocumentSymbolsParser.Virtual, 0)

        def life_time(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Life_timeContext,0)


        def type_identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.Type_identifierContext,i)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.ItemContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.ItemContext,i)


        def label(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.LabelContext,0)


        def parameter_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.Parameter_listContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.Parameter_listContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(DocumentSymbolsParser.Comma)
            else:
                return self.getToken(DocumentSymbolsParser.Comma, i)

        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_class_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = DocumentSymbolsParser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DocumentSymbolsParser.Virtual:
                self.state = 151
                self.match(DocumentSymbolsParser.Virtual)


            self.state = 154
            self.match(DocumentSymbolsParser.Class)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DocumentSymbolsParser.T__4 or _la==DocumentSymbolsParser.T__5:
                self.state = 155
                self.life_time()


            self.state = 158
            self.identifier()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DocumentSymbolsParser.T__0:
                self.state = 159
                self.match(DocumentSymbolsParser.T__0)
                self.state = 160
                self.type_identifier()
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 161
                        self.matchWildcard() 
                    self.state = 166
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)



            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DocumentSymbolsParser.T__1:
                self.state = 169
                self.match(DocumentSymbolsParser.T__1)
                self.state = 170
                self.type_identifier()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==DocumentSymbolsParser.T__2:
                    self.state = 171
                    self.parameter_list()


                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DocumentSymbolsParser.Comma:
                    self.state = 174
                    self.match(DocumentSymbolsParser.Comma)
                    self.state = 175
                    self.type_identifier()
                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==DocumentSymbolsParser.T__2:
                        self.state = 176
                        self.parameter_list()


                    self.state = 183
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 186
            self.match(DocumentSymbolsParser.SemiColon)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 187
                    self.item() 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 193
            self.match(DocumentSymbolsParser.Endclass)
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 194
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def task_declaration(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Task_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Function_declarationContext,0)


        def class_declaration(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Class_declarationContext,0)


        def type_declaration(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Type_declarationContext,0)


        def instantiation(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.InstantiationContext,0)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = DocumentSymbolsParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_item)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.task_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.function_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.class_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 200
                self.type_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 201
                self.instantiation()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 203 
                self._errHandler.sync(self)
                _alt = 1+1
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1+1:
                        self.state = 202
                        self.matchWildcard()

                    else:
                        raise NoViableAltException(self)
                    self.state = 205 
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


    class Task_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Task(self):
            return self.getToken(DocumentSymbolsParser.Task, 0)

        def identifier(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,0)


        def Endtask(self):
            return self.getToken(DocumentSymbolsParser.Endtask, 0)

        def label(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.LabelContext,0)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_task_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTask_declaration" ):
                return visitor.visitTask_declaration(self)
            else:
                return visitor.visitChildren(self)




    def task_declaration(self):

        localctx = DocumentSymbolsParser.Task_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_task_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(DocumentSymbolsParser.Task)
            self.state = 210
            self.identifier()
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 211
                    self.matchWildcard() 
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

            self.state = 217
            self.match(DocumentSymbolsParser.Endtask)
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 218
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

        def Function(self):
            return self.getToken(DocumentSymbolsParser.Function, 0)

        def return_val(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Return_valContext,0)


        def identifier(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,0)


        def OpenParen(self):
            return self.getToken(DocumentSymbolsParser.OpenParen, 0)

        def Endfunction(self):
            return self.getToken(DocumentSymbolsParser.Endfunction, 0)

        def label(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.LabelContext,0)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = DocumentSymbolsParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(DocumentSymbolsParser.Function)
            self.state = 222
            self.return_val()
            self.state = 223
            self.identifier()
            self.state = 224
            self.match(DocumentSymbolsParser.OpenParen)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 225
                    self.matchWildcard() 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 231
            self.match(DocumentSymbolsParser.Endfunction)
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 232
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

        def Typedef(self):
            return self.getToken(DocumentSymbolsParser.Typedef, 0)

        def identifier(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,0)


        def SemiColon(self):
            return self.getToken(DocumentSymbolsParser.SemiColon, 0)

        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_type_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_declaration" ):
                return visitor.visitType_declaration(self)
            else:
                return visitor.visitChildren(self)




    def type_declaration(self):

        localctx = DocumentSymbolsParser.Type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(DocumentSymbolsParser.Typedef)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 236
                    self.matchWildcard() 
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 242
            self.identifier()
            self.state = 243
            self.match(DocumentSymbolsParser.SemiColon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CloseParen(self):
            return self.getToken(DocumentSymbolsParser.CloseParen, 0)

        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = DocumentSymbolsParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(DocumentSymbolsParser.T__2)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 246
                    self.matchWildcard() 
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 252
            self.match(DocumentSymbolsParser.CloseParen)
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
            return self.getToken(DocumentSymbolsParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(DocumentSymbolsParser.CloseParen, 0)

        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_port_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPort_list" ):
                return visitor.visitPort_list(self)
            else:
                return visitor.visitChildren(self)




    def port_list(self):

        localctx = DocumentSymbolsParser.Port_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_port_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(DocumentSymbolsParser.OpenParen)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 255
                    self.matchWildcard() 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            self.state = 261
            self.match(DocumentSymbolsParser.CloseParen)
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
            return DocumentSymbolsParser.RULE_return_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_val" ):
                return visitor.visitReturn_val(self)
            else:
                return visitor.visitChildren(self)




    def return_val(self):

        localctx = DocumentSymbolsParser.Return_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_return_val)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(DocumentSymbolsParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 264
                        self.matchWildcard() 
                    self.state = 269
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
            return DocumentSymbolsParser.RULE_life_time

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLife_time" ):
                return visitor.visitLife_time(self)
            else:
                return visitor.visitChildren(self)




    def life_time(self):

        localctx = DocumentSymbolsParser.Life_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_life_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            _la = self._input.LA(1)
            if not(_la==DocumentSymbolsParser.T__4 or _la==DocumentSymbolsParser.T__5):
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


    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenParen(self):
            return self.getToken(DocumentSymbolsParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(DocumentSymbolsParser.CloseParen, 0)

        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = DocumentSymbolsParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(DocumentSymbolsParser.OpenParen)
            self.state = 275
            self.match(DocumentSymbolsParser.T__6)
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 276
                    self.matchWildcard() 
                self.state = 281
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self.state = 282
            self.match(DocumentSymbolsParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstantiationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_identifier(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Type_identifierContext,0)


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,i)


        def SemiColon(self):
            return self.getToken(DocumentSymbolsParser.SemiColon, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.Parameter_listContext,0)


        def OpenBracket(self, i:int=None):
            if i is None:
                return self.getTokens(DocumentSymbolsParser.OpenBracket)
            else:
                return self.getToken(DocumentSymbolsParser.OpenBracket, i)

        def CloseBracket(self, i:int=None):
            if i is None:
                return self.getTokens(DocumentSymbolsParser.CloseBracket)
            else:
                return self.getToken(DocumentSymbolsParser.CloseBracket, i)

        def port_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.Port_listContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.Port_listContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(DocumentSymbolsParser.Comma)
            else:
                return self.getToken(DocumentSymbolsParser.Comma, i)

        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_instantiation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstantiation" ):
                return visitor.visitInstantiation(self)
            else:
                return visitor.visitChildren(self)




    def instantiation(self):

        localctx = DocumentSymbolsParser.InstantiationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_instantiation)
        self._la = 0 # Token type
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.type_identifier()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==DocumentSymbolsParser.T__2:
                    self.state = 285
                    self.parameter_list()


                self.state = 288
                self.identifier()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DocumentSymbolsParser.OpenBracket:
                    self.state = 289
                    self.match(DocumentSymbolsParser.OpenBracket)
                    self.state = 293
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
                    while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1+1:
                            self.state = 290
                            self.matchWildcard() 
                        self.state = 295
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

                    self.state = 296
                    self.match(DocumentSymbolsParser.CloseBracket)
                    self.state = 301
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==DocumentSymbolsParser.OpenParen:
                    self.state = 302
                    self.port_list()


                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DocumentSymbolsParser.Comma:
                    self.state = 305
                    self.match(DocumentSymbolsParser.Comma)
                    self.state = 306
                    self.identifier()
                    self.state = 317
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==DocumentSymbolsParser.OpenBracket:
                        self.state = 307
                        self.match(DocumentSymbolsParser.OpenBracket)
                        self.state = 311
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
                        while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1+1:
                                self.state = 308
                                self.matchWildcard() 
                            self.state = 313
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

                        self.state = 314
                        self.match(DocumentSymbolsParser.CloseBracket)
                        self.state = 319
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 321
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==DocumentSymbolsParser.OpenParen:
                        self.state = 320
                        self.port_list()


                    self.state = 327
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 328
                self.match(DocumentSymbolsParser.SemiColon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331 
                self._errHandler.sync(self)
                _alt = 1+1
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1+1:
                        self.state = 330
                        self.matchWildcard()

                    else:
                        raise NoViableAltException(self)
                    self.state = 333 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(DocumentSymbolsParser.Word)
            else:
                return self.getToken(DocumentSymbolsParser.Word, i)

        def OpenBracket(self, i:int=None):
            if i is None:
                return self.getTokens(DocumentSymbolsParser.OpenBracket)
            else:
                return self.getToken(DocumentSymbolsParser.OpenBracket, i)

        def CloseBracket(self, i:int=None):
            if i is None:
                return self.getTokens(DocumentSymbolsParser.CloseBracket)
            else:
                return self.getToken(DocumentSymbolsParser.CloseBracket, i)

        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_type_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_identifier" ):
                return visitor.visitType_identifier(self)
            else:
                return visitor.visitChildren(self)




    def type_identifier(self):

        localctx = DocumentSymbolsParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 337
                self.match(DocumentSymbolsParser.Word)
                self.state = 338
                self.match(DocumentSymbolsParser.T__7)


            self.state = 341
            self.match(DocumentSymbolsParser.Word)
            self.state = 352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 342
                    self.match(DocumentSymbolsParser.OpenBracket)
                    self.state = 346
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
                    while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1+1:
                            self.state = 343
                            self.matchWildcard() 
                        self.state = 348
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

                    self.state = 349
                    self.match(DocumentSymbolsParser.CloseBracket) 
                self.state = 354
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

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
            return self.getToken(DocumentSymbolsParser.Word, 0)

        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = DocumentSymbolsParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(DocumentSymbolsParser.Word)
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
            return self.getToken(DocumentSymbolsParser.Colon, 0)

        def identifier(self):
            return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,0)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_label

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = DocumentSymbolsParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(DocumentSymbolsParser.Colon)
            self.state = 358
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
            return self.getTypedRuleContext(DocumentSymbolsParser.IdentifierContext,0)


        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(DocumentSymbolsParser.Dot)
            else:
                return self.getToken(DocumentSymbolsParser.Dot, i)

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(DocumentSymbolsParser.Word)
            else:
                return self.getToken(DocumentSymbolsParser.Word, i)

        def constant_bit_select(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DocumentSymbolsParser.Constant_bit_selectContext)
            else:
                return self.getTypedRuleContext(DocumentSymbolsParser.Constant_bit_selectContext,i)


        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_hierarchical_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHierarchical_identifier" ):
                return visitor.visitHierarchical_identifier(self)
            else:
                return visitor.visitChildren(self)




    def hierarchical_identifier(self):

        localctx = DocumentSymbolsParser.Hierarchical_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_hierarchical_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DocumentSymbolsParser.T__8:
                self.state = 360
                self.match(DocumentSymbolsParser.T__8)
                self.state = 361
                self.match(DocumentSymbolsParser.Dot)


            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 364
                    self.match(DocumentSymbolsParser.Word)
                    self.state = 365
                    self.constant_bit_select()
                    self.state = 366
                    self.match(DocumentSymbolsParser.Dot) 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

            self.state = 373
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
                return self.getTokens(DocumentSymbolsParser.OpenBracket)
            else:
                return self.getToken(DocumentSymbolsParser.OpenBracket, i)

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(DocumentSymbolsParser.Word)
            else:
                return self.getToken(DocumentSymbolsParser.Word, i)

        def CloseBracket(self, i:int=None):
            if i is None:
                return self.getTokens(DocumentSymbolsParser.CloseBracket)
            else:
                return self.getToken(DocumentSymbolsParser.CloseBracket, i)

        def getRuleIndex(self):
            return DocumentSymbolsParser.RULE_constant_bit_select

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant_bit_select" ):
                return visitor.visitConstant_bit_select(self)
            else:
                return visitor.visitChildren(self)




    def constant_bit_select(self):

        localctx = DocumentSymbolsParser.Constant_bit_selectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_constant_bit_select)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DocumentSymbolsParser.OpenBracket:
                self.state = 375
                self.match(DocumentSymbolsParser.OpenBracket)
                self.state = 376
                self.match(DocumentSymbolsParser.Word)
                self.state = 377
                self.match(DocumentSymbolsParser.CloseBracket)
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





