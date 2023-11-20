# Generated from Python3Lexer.g4 by ANTLR 4.7.2
import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO

if __name__ is not None and "." in __name__:
    from .Python3LexerBase import Python3LexerBase
else:
    from Python3LexerBase import Python3LexerBase

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2j")
        buf.write("\u039a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4")
        buf.write("y\ty\4z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080")
        buf.write("\t\u0080\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083")
        buf.write("\4\u0084\t\u0084\3\2\3\2\5\2\u010c\n\2\3\3\3\3\3\3\5\3")
        buf.write("\u0111\n\3\3\4\3\4\3\4\3\4\5\4\u0117\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!")
        buf.write("\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3(\3(\3(")
        buf.write("\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\5")
        buf.write("+\u01e7\n+\3+\3+\5+\u01eb\n+\3+\5+\u01ee\n+\5+\u01f0\n")
        buf.write("+\3+\3+\3,\3,\7,\u01f6\n,\f,\16,\u01f9\13,\3-\3-\3-\3")
        buf.write("-\3-\5-\u0200\n-\3-\3-\5-\u0204\n-\3.\3.\3.\3.\3.\5.\u020b")
        buf.write("\n.\3.\3.\5.\u020f\n.\3/\3/\7/\u0213\n/\f/\16/\u0216\13")
        buf.write("/\3/\6/\u0219\n/\r/\16/\u021a\5/\u021d\n/\3\60\3\60\3")
        buf.write("\60\6\60\u0222\n\60\r\60\16\60\u0223\3\61\3\61\3\61\6")
        buf.write("\61\u0229\n\61\r\61\16\61\u022a\3\62\3\62\3\62\6\62\u0230")
        buf.write("\n\62\r\62\16\62\u0231\3\63\3\63\5\63\u0236\n\63\3\64")
        buf.write("\3\64\5\64\u023a\n\64\3\64\3\64\3\65\3\65\3\66\3\66\3")
        buf.write("\66\3\66\3\67\3\67\38\38\38\39\39\39\3:\3:\3;\3;\3<\3")
        buf.write("<\3=\3=\3=\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3B\3B\3C\3C\3")
        buf.write("D\3D\3D\3E\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3J\3K\3")
        buf.write("K\3L\3L\3L\3M\3M\3M\3N\3N\3O\3O\3P\3P\3P\3Q\3Q\3Q\3R\3")
        buf.write("R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3V\3V\3V\3W\3W\3W\3X\3X\3")
        buf.write("X\3Y\3Y\3Y\3Z\3Z\3Z\3[\3[\3[\3\\\3\\\3\\\3]\3]\3]\3^\3")
        buf.write("^\3^\3_\3_\3_\3`\3`\3`\3`\3a\3a\3a\3a\3b\3b\3b\3b\3c\3")
        buf.write("c\3c\3c\3d\3d\3e\3e\3e\3e\3f\3f\3f\5f\u02c8\nf\3f\3f\3")
        buf.write("g\3g\3h\3h\3h\7h\u02d1\nh\fh\16h\u02d4\13h\3h\3h\3h\3")
        buf.write("h\7h\u02da\nh\fh\16h\u02dd\13h\3h\5h\u02e0\nh\3i\3i\3")
        buf.write("i\3i\3i\7i\u02e7\ni\fi\16i\u02ea\13i\3i\3i\3i\3i\3i\3")
        buf.write("i\3i\3i\7i\u02f4\ni\fi\16i\u02f7\13i\3i\3i\3i\5i\u02fc")
        buf.write("\ni\3j\3j\5j\u0300\nj\3k\3k\3l\3l\3l\3l\5l\u0308\nl\3")
        buf.write("m\3m\3n\3n\3o\3o\3p\3p\3q\3q\3r\5r\u0315\nr\3r\3r\3r\3")
        buf.write("r\5r\u031b\nr\3s\3s\5s\u031f\ns\3s\3s\3t\6t\u0324\nt\r")
        buf.write("t\16t\u0325\3u\3u\6u\u032a\nu\ru\16u\u032b\3v\3v\5v\u0330")
        buf.write("\nv\3v\6v\u0333\nv\rv\16v\u0334\3w\3w\3w\7w\u033a\nw\f")
        buf.write("w\16w\u033d\13w\3w\3w\3w\3w\7w\u0343\nw\fw\16w\u0346\13")
        buf.write("w\3w\5w\u0349\nw\3x\3x\3x\3x\3x\7x\u0350\nx\fx\16x\u0353")
        buf.write("\13x\3x\3x\3x\3x\3x\3x\3x\3x\7x\u035d\nx\fx\16x\u0360")
        buf.write("\13x\3x\3x\3x\5x\u0365\nx\3y\3y\5y\u0369\ny\3z\5z\u036c")
        buf.write("\nz\3{\5{\u036f\n{\3|\5|\u0372\n|\3}\3}\3}\3~\6~\u0378")
        buf.write("\n~\r~\16~\u0379\3\177\3\177\7\177\u037e\n\177\f\177\16")
        buf.write("\177\u0381\13\177\3\u0080\3\u0080\5\u0080\u0385\n\u0080")
        buf.write("\3\u0080\5\u0080\u0388\n\u0080\3\u0080\3\u0080\5\u0080")
        buf.write("\u038c\n\u0080\3\u0081\3\u0081\3\u0082\3\u0082\3\u0083")
        buf.write("\3\u0083\5\u0083\u0394\n\u0083\3\u0084\3\u0084\3\u0084")
        buf.write("\5\u0084\u0399\n\u0084\6\u02e8\u02f5\u0351\u035e\2\u0085")
        buf.write("\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17")
        buf.write("\31\20\33\21\35\22\37\23!\24#\25%\26\'\27)\30+\31-\32")
        buf.write("/\33\61\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O")
        buf.write("+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66g\67i8k9m:o;q<s=")
        buf.write("u>w?y@{A}B\177C\u0081D\u0083E\u0085F\u0087G\u0089H\u008b")
        buf.write("I\u008dJ\u008fK\u0091L\u0093M\u0095N\u0097O\u0099P\u009b")
        buf.write("Q\u009dR\u009fS\u00a1T\u00a3U\u00a5V\u00a7W\u00a9X\u00ab")
        buf.write("Y\u00adZ\u00af[\u00b1\\\u00b3]\u00b5^\u00b7_\u00b9`\u00bb")
        buf.write("a\u00bdb\u00bfc\u00c1d\u00c3e\u00c5f\u00c7g\u00c9h\u00cb")
        buf.write("i\u00cdj\u00cf\2\u00d1\2\u00d3\2\u00d5\2\u00d7\2\u00d9")
        buf.write("\2\u00db\2\u00dd\2\u00df\2\u00e1\2\u00e3\2\u00e5\2\u00e7")
        buf.write("\2\u00e9\2\u00eb\2\u00ed\2\u00ef\2\u00f1\2\u00f3\2\u00f5")
        buf.write("\2\u00f7\2\u00f9\2\u00fb\2\u00fd\2\u00ff\2\u0101\2\u0103")
        buf.write("\2\u0105\2\u0107\2\3\2\33\b\2HHTTWWhhttww\4\2HHhh\4\2")
        buf.write("TTtt\4\2DDdd\4\2QQqq\4\2ZZzz\4\2LLll\6\2\f\f\16\17))^")
        buf.write("^\6\2\f\f\16\17$$^^\3\2^^\3\2\63;\3\2\62;\3\2\629\5\2")
        buf.write("\62;CHch\3\2\62\63\4\2GGgg\4\2--//\7\2\2\13\r\16\20(*")
        buf.write("]_\u0081\7\2\2\13\r\16\20#%]_\u0081\4\2\2]_\u0081\3\2")
        buf.write("\2\u0081\4\2\13\13\"\"\4\2\f\f\16\17\6\2\u1887\u1888\u211a")
        buf.write("\u211a\u2130\u2130\u309d\u309e\6\2\u00b9\u00b9\u0389\u0389")
        buf.write("\u136b\u1373\u19dc\u19dc\4\u0274\2C\2\\\2a\2a\2c\2|\2")
        buf.write("\u00ac\2\u00ac\2\u00b7\2\u00b7\2\u00bc\2\u00bc\2\u00c2")
        buf.write("\2\u00d8\2\u00da\2\u00f8\2\u00fa\2\u02c3\2\u02c8\2\u02d3")
        buf.write("\2\u02e2\2\u02e6\2\u02ee\2\u02ee\2\u02f0\2\u02f0\2\u0372")
        buf.write("\2\u0376\2\u0378\2\u0379\2\u037c\2\u037f\2\u0381\2\u0381")
        buf.write("\2\u0388\2\u0388\2\u038a\2\u038c\2\u038e\2\u038e\2\u0390")
        buf.write("\2\u03a3\2\u03a5\2\u03f7\2\u03f9\2\u0483\2\u048c\2\u0531")
        buf.write("\2\u0533\2\u0558\2\u055b\2\u055b\2\u0562\2\u058a\2\u05d2")
        buf.write("\2\u05ec\2\u05f1\2\u05f4\2\u0622\2\u064c\2\u0670\2\u0671")
        buf.write("\2\u0673\2\u06d5\2\u06d7\2\u06d7\2\u06e7\2\u06e8\2\u06f0")
        buf.write("\2\u06f1\2\u06fc\2\u06fe\2\u0701\2\u0701\2\u0712\2\u0712")
        buf.write("\2\u0714\2\u0731\2\u074f\2\u07a7\2\u07b3\2\u07b3\2\u07cc")
        buf.write("\2\u07ec\2\u07f6\2\u07f7\2\u07fc\2\u07fc\2\u0802\2\u0817")
        buf.write("\2\u081c\2\u081c\2\u0826\2\u0826\2\u082a\2\u082a\2\u0842")
        buf.write("\2\u085a\2\u0862\2\u086c\2\u08a2\2\u08b6\2\u08b8\2\u08c9")
        buf.write("\2\u0906\2\u093b\2\u093f\2\u093f\2\u0952\2\u0952\2\u095a")
        buf.write("\2\u0963\2\u0973\2\u0982\2\u0987\2\u098e\2\u0991\2\u0992")
        buf.write("\2\u0995\2\u09aa\2\u09ac\2\u09b2\2\u09b4\2\u09b4\2\u09b8")
        buf.write("\2\u09bb\2\u09bf\2\u09bf\2\u09d0\2\u09d0\2\u09de\2\u09df")
        buf.write("\2\u09e1\2\u09e3\2\u09f2\2\u09f3\2\u09fe\2\u09fe\2\u0a07")
        buf.write("\2\u0a0c\2\u0a11\2\u0a12\2\u0a15\2\u0a2a\2\u0a2c\2\u0a32")
        buf.write("\2\u0a34\2\u0a35\2\u0a37\2\u0a38\2\u0a3a\2\u0a3b\2\u0a5b")
        buf.write("\2\u0a5e\2\u0a60\2\u0a60\2\u0a74\2\u0a76\2\u0a87\2\u0a8f")
        buf.write("\2\u0a91\2\u0a93\2\u0a95\2\u0aaa\2\u0aac\2\u0ab2\2\u0ab4")
        buf.write("\2\u0ab5\2\u0ab7\2\u0abb\2\u0abf\2\u0abf\2\u0ad2\2\u0ad2")
        buf.write("\2\u0ae2\2\u0ae3\2\u0afb\2\u0afb\2\u0b07\2\u0b0e\2\u0b11")
        buf.write("\2\u0b12\2\u0b15\2\u0b2a\2\u0b2c\2\u0b32\2\u0b34\2\u0b35")
        buf.write("\2\u0b37\2\u0b3b\2\u0b3f\2\u0b3f\2\u0b5e\2\u0b5f\2\u0b61")
        buf.write("\2\u0b63\2\u0b73\2\u0b73\2\u0b85\2\u0b85\2\u0b87\2\u0b8c")
        buf.write("\2\u0b90\2\u0b92\2\u0b94\2\u0b97\2\u0b9b\2\u0b9c\2\u0b9e")
        buf.write("\2\u0b9e\2\u0ba0\2\u0ba1\2\u0ba5\2\u0ba6\2\u0baa\2\u0bac")
        buf.write("\2\u0bb0\2\u0bbb\2\u0bd2\2\u0bd2\2\u0c07\2\u0c0e\2\u0c10")
        buf.write("\2\u0c12\2\u0c14\2\u0c2a\2\u0c2c\2\u0c3b\2\u0c3f\2\u0c3f")
        buf.write("\2\u0c5a\2\u0c5c\2\u0c62\2\u0c63\2\u0c82\2\u0c82\2\u0c87")
        buf.write("\2\u0c8e\2\u0c90\2\u0c92\2\u0c94\2\u0caa\2\u0cac\2\u0cb5")
        buf.write("\2\u0cb7\2\u0cbb\2\u0cbf\2\u0cbf\2\u0ce0\2\u0ce0\2\u0ce2")
        buf.write("\2\u0ce3\2\u0cf3\2\u0cf4\2\u0d06\2\u0d0e\2\u0d10\2\u0d12")
        buf.write("\2\u0d14\2\u0d3c\2\u0d3f\2\u0d3f\2\u0d50\2\u0d50\2\u0d56")
        buf.write("\2\u0d58\2\u0d61\2\u0d63\2\u0d7c\2\u0d81\2\u0d87\2\u0d98")
        buf.write("\2\u0d9c\2\u0db3\2\u0db5\2\u0dbd\2\u0dbf\2\u0dbf\2\u0dc2")
        buf.write("\2\u0dc8\2\u0e03\2\u0e32\2\u0e34\2\u0e35\2\u0e42\2\u0e48")
        buf.write("\2\u0e83\2\u0e84\2\u0e86\2\u0e86\2\u0e88\2\u0e8c\2\u0e8e")
        buf.write("\2\u0ea5\2\u0ea7\2\u0ea7\2\u0ea9\2\u0eb2\2\u0eb4\2\u0eb5")
        buf.write("\2\u0ebf\2\u0ebf\2\u0ec2\2\u0ec6\2\u0ec8\2\u0ec8\2\u0ede")
        buf.write("\2\u0ee1\2\u0f02\2\u0f02\2\u0f42\2\u0f49\2\u0f4b\2\u0f6e")
        buf.write("\2\u0f8a\2\u0f8e\2\u1002\2\u102c\2\u1041\2\u1041\2\u1052")
        buf.write("\2\u1057\2\u105c\2\u105f\2\u1063\2\u1063\2\u1067\2\u1068")
        buf.write("\2\u1070\2\u1072\2\u1077\2\u1083\2\u1090\2\u1090\2\u10a2")
        buf.write("\2\u10c7\2\u10c9\2\u10c9\2\u10cf\2\u10cf\2\u10d2\2\u10fc")
        buf.write("\2\u10fe\2\u124a\2\u124c\2\u124f\2\u1252\2\u1258\2\u125a")
        buf.write("\2\u125a\2\u125c\2\u125f\2\u1262\2\u128a\2\u128c\2\u128f")
        buf.write("\2\u1292\2\u12b2\2\u12b4\2\u12b7\2\u12ba\2\u12c0\2\u12c2")
        buf.write("\2\u12c2\2\u12c4\2\u12c7\2\u12ca\2\u12d8\2\u12da\2\u1312")
        buf.write("\2\u1314\2\u1317\2\u131a\2\u135c\2\u1382\2\u1391\2\u13a2")
        buf.write("\2\u13f7\2\u13fa\2\u13ff\2\u1403\2\u166e\2\u1671\2\u1681")
        buf.write("\2\u1683\2\u169c\2\u16a2\2\u16ec\2\u16f0\2\u16fa\2\u1702")
        buf.write("\2\u170e\2\u1710\2\u1713\2\u1722\2\u1733\2\u1742\2\u1753")
        buf.write("\2\u1762\2\u176e\2\u1770\2\u1772\2\u1782\2\u17b5\2\u17d9")
        buf.write("\2\u17d9\2\u17de\2\u17de\2\u1822\2\u187a\2\u1882\2\u1886")
        buf.write("\2\u1889\2\u18aa\2\u18ac\2\u18ac\2\u18b2\2\u18f7\2\u1902")
        buf.write("\2\u1920\2\u1952\2\u196f\2\u1972\2\u1976\2\u1982\2\u19ad")
        buf.write("\2\u19b2\2\u19cb\2\u1a02\2\u1a18\2\u1a22\2\u1a56\2\u1aa9")
        buf.write("\2\u1aa9\2\u1b07\2\u1b35\2\u1b47\2\u1b4d\2\u1b85\2\u1ba2")
        buf.write("\2\u1bb0\2\u1bb1\2\u1bbc\2\u1be7\2\u1c02\2\u1c25\2\u1c4f")
        buf.write("\2\u1c51\2\u1c5c\2\u1c7f\2\u1c82\2\u1c8a\2\u1c92\2\u1cbc")
        buf.write("\2\u1cbf\2\u1cc1\2\u1ceb\2\u1cee\2\u1cf0\2\u1cf5\2\u1cf7")
        buf.write("\2\u1cf8\2\u1cfc\2\u1cfc\2\u1d02\2\u1dc1\2\u1e02\2\u1f17")
        buf.write("\2\u1f1a\2\u1f1f\2\u1f22\2\u1f47\2\u1f4a\2\u1f4f\2\u1f52")
        buf.write("\2\u1f59\2\u1f5b\2\u1f5b\2\u1f5d\2\u1f5d\2\u1f5f\2\u1f5f")
        buf.write("\2\u1f61\2\u1f7f\2\u1f82\2\u1fb6\2\u1fb8\2\u1fbe\2\u1fc0")
        buf.write("\2\u1fc0\2\u1fc4\2\u1fc6\2\u1fc8\2\u1fce\2\u1fd2\2\u1fd5")
        buf.write("\2\u1fd8\2\u1fdd\2\u1fe2\2\u1fee\2\u1ff4\2\u1ff6\2\u1ff8")
        buf.write("\2\u1ffe\2\u2073\2\u2073\2\u2081\2\u2081\2\u2092\2\u209e")
        buf.write("\2\u2104\2\u2104\2\u2109\2\u2109\2\u210c\2\u2115\2\u2117")
        buf.write("\2\u2117\2\u211b\2\u211f\2\u2126\2\u2126\2\u2128\2\u2128")
        buf.write("\2\u212a\2\u212a\2\u212c\2\u212f\2\u2131\2\u213b\2\u213e")
        buf.write("\2\u2141\2\u2147\2\u214b\2\u2150\2\u2150\2\u2162\2\u218a")
        buf.write("\2\u2c02\2\u2c30\2\u2c32\2\u2c60\2\u2c62\2\u2ce6\2\u2ced")
        buf.write("\2\u2cf0\2\u2cf4\2\u2cf5\2\u2d02\2\u2d27\2\u2d29\2\u2d29")
        buf.write("\2\u2d2f\2\u2d2f\2\u2d32\2\u2d69\2\u2d71\2\u2d71\2\u2d82")
        buf.write("\2\u2d98\2\u2da2\2\u2da8\2\u2daa\2\u2db0\2\u2db2\2\u2db8")
        buf.write("\2\u2dba\2\u2dc0\2\u2dc2\2\u2dc8\2\u2dca\2\u2dd0\2\u2dd2")
        buf.write("\2\u2dd8\2\u2dda\2\u2de0\2\u2e31\2\u2e31\2\u3007\2\u3009")
        buf.write("\2\u3023\2\u302b\2\u3033\2\u3037\2\u303a\2\u303e\2\u3043")
        buf.write("\2\u3098\2\u309f\2\u30a1\2\u30a3\2\u30fc\2\u30fe\2\u3101")
        buf.write("\2\u3107\2\u3131\2\u3133\2\u3190\2\u31a2\2\u31c1\2\u31f2")
        buf.write("\2\u3201\2\u3402\2\u4dc1\2\u4e02\2\u9ffe\2\ua002\2\ua48e")
        buf.write("\2\ua4d2\2\ua4ff\2\ua502\2\ua60e\2\ua612\2\ua621\2\ua62c")
        buf.write("\2\ua62d\2\ua642\2\ua670\2\ua681\2\ua69f\2\ua6a2\2\ua6f1")
        buf.write("\2\ua719\2\ua721\2\ua724\2\ua78a\2\ua78d\2\ua7c1\2\ua7c4")
        buf.write("\2\ua7cc\2\ua7f7\2\ua803\2\ua805\2\ua807\2\ua809\2\ua80c")
        buf.write("\2\ua80e\2\ua824\2\ua842\2\ua875\2\ua884\2\ua8b5\2\ua8f4")
        buf.write("\2\ua8f9\2\ua8fd\2\ua8fd\2\ua8ff\2\ua900\2\ua90c\2\ua927")
        buf.write("\2\ua932\2\ua948\2\ua962\2\ua97e\2\ua986\2\ua9b4\2\ua9d1")
        buf.write("\2\ua9d1\2\ua9e2\2\ua9e6\2\ua9e8\2\ua9f1\2\ua9fc\2\uaa00")
        buf.write("\2\uaa02\2\uaa2a\2\uaa42\2\uaa44\2\uaa46\2\uaa4d\2\uaa62")
        buf.write("\2\uaa78\2\uaa7c\2\uaa7c\2\uaa80\2\uaab1\2\uaab3\2\uaab3")
        buf.write("\2\uaab7\2\uaab8\2\uaabb\2\uaabf\2\uaac2\2\uaac2\2\uaac4")
        buf.write("\2\uaac4\2\uaadd\2\uaadf\2\uaae2\2\uaaec\2\uaaf4\2\uaaf6")
        buf.write("\2\uab03\2\uab08\2\uab0b\2\uab10\2\uab13\2\uab18\2\uab22")
        buf.write("\2\uab28\2\uab2a\2\uab30\2\uab32\2\uab5c\2\uab5e\2\uab6b")
        buf.write("\2\uab72\2\uabe4\2\uac02\2\ud7a5\2\ud7b2\2\ud7c8\2\ud7cd")
        buf.write("\2\ud7fd\2\uf902\2\ufa6f\2\ufa72\2\ufadb\2\ufb02\2\ufb08")
        buf.write("\2\ufb15\2\ufb19\2\ufb1f\2\ufb1f\2\ufb21\2\ufb2a\2\ufb2c")
        buf.write("\2\ufb38\2\ufb3a\2\ufb3e\2\ufb40\2\ufb40\2\ufb42\2\ufb43")
        buf.write("\2\ufb45\2\ufb46\2\ufb48\2\ufbb3\2\ufbd5\2\ufd3f\2\ufd52")
        buf.write("\2\ufd91\2\ufd94\2\ufdc9\2\ufdf2\2\ufdfd\2\ufe72\2\ufe76")
        buf.write("\2\ufe78\2\ufefe\2\uff23\2\uff3c\2\uff43\2\uff5c\2\uff68")
        buf.write("\2\uffc0\2\uffc4\2\uffc9\2\uffcc\2\uffd1\2\uffd4\2\uffd9")
        buf.write("\2\uffdc\2\uffde\2\2\3\r\3\17\3(\3*\3<\3>\3?\3A\3O\3R")
        buf.write("\3_\3\u0082\3\u00fc\3\u0142\3\u0176\3\u0282\3\u029e\3")
        buf.write("\u02a2\3\u02d2\3\u0302\3\u0321\3\u032f\3\u034c\3\u0352")
        buf.write("\3\u0377\3\u0382\3\u039f\3\u03a2\3\u03c5\3\u03ca\3\u03d1")
        buf.write("\3\u03d3\3\u03d7\3\u0402\3\u049f\3\u04b2\3\u04d5\3\u04da")
        buf.write("\3\u04fd\3\u0502\3\u0529\3\u0532\3\u0565\3\u0602\3\u0738")
        buf.write("\3\u0742\3\u0757\3\u0762\3\u0769\3\u0802\3\u0807\3\u080a")
        buf.write("\3\u080a\3\u080c\3\u0837\3\u0839\3\u083a\3\u083e\3\u083e")
        buf.write("\3\u0841\3\u0857\3\u0862\3\u0878\3\u0882\3\u08a0\3\u08e2")
        buf.write("\3\u08f4\3\u08f6\3\u08f7\3\u0902\3\u0917\3\u0922\3\u093b")
        buf.write("\3\u0982\3\u09b9\3\u09c0\3\u09c1\3\u0a02\3\u0a02\3\u0a12")
        buf.write("\3\u0a15\3\u0a17\3\u0a19\3\u0a1b\3\u0a37\3\u0a62\3\u0a7e")
        buf.write("\3\u0a82\3\u0a9e\3\u0ac2\3\u0ac9\3\u0acb\3\u0ae6\3\u0b02")
        buf.write("\3\u0b37\3\u0b42\3\u0b57\3\u0b62\3\u0b74\3\u0b82\3\u0b93")
        buf.write("\3\u0c02\3\u0c4a\3\u0c82\3\u0cb4\3\u0cc2\3\u0cf4\3\u0d02")
        buf.write("\3\u0d25\3\u0e82\3\u0eab\3\u0eb2\3\u0eb3\3\u0f02\3\u0f1e")
        buf.write("\3\u0f29\3\u0f29\3\u0f32\3\u0f47\3\u0fb2\3\u0fc6\3\u0fe2")
        buf.write("\3\u0ff8\3\u1005\3\u1039\3\u1085\3\u10b1\3\u10d2\3\u10ea")
        buf.write("\3\u1105\3\u1128\3\u1146\3\u1146\3\u1149\3\u1149\3\u1152")
        buf.write("\3\u1174\3\u1178\3\u1178\3\u1185\3\u11b4\3\u11c3\3\u11c6")
        buf.write("\3\u11dc\3\u11dc\3\u11de\3\u11de\3\u1202\3\u1213\3\u1215")
        buf.write("\3\u122d\3\u1282\3\u1288\3\u128a\3\u128a\3\u128c\3\u128f")
        buf.write("\3\u1291\3\u129f\3\u12a1\3\u12aa\3\u12b2\3\u12e0\3\u1307")
        buf.write("\3\u130e\3\u1311\3\u1312\3\u1315\3\u132a\3\u132c\3\u1332")
        buf.write("\3\u1334\3\u1335\3\u1337\3\u133b\3\u133f\3\u133f\3\u1352")
        buf.write("\3\u1352\3\u135f\3\u1363\3\u1402\3\u1436\3\u1449\3\u144c")
        buf.write("\3\u1461\3\u1463\3\u1482\3\u14b1\3\u14c6\3\u14c7\3\u14c9")
        buf.write("\3\u14c9\3\u1582\3\u15b0\3\u15da\3\u15dd\3\u1602\3\u1631")
        buf.write("\3\u1646\3\u1646\3\u1682\3\u16ac\3\u16ba\3\u16ba\3\u1702")
        buf.write("\3\u171c\3\u1802\3\u182d\3\u18a2\3\u18e1\3\u1901\3\u1908")
        buf.write("\3\u190b\3\u190b\3\u190e\3\u1915\3\u1917\3\u1918\3\u191a")
        buf.write("\3\u1931\3\u1941\3\u1941\3\u1943\3\u1943\3\u19a2\3\u19a9")
        buf.write("\3\u19ac\3\u19d2\3\u19e3\3\u19e3\3\u19e5\3\u19e5\3\u1a02")
        buf.write("\3\u1a02\3\u1a0d\3\u1a34\3\u1a3c\3\u1a3c\3\u1a52\3\u1a52")
        buf.write("\3\u1a5e\3\u1a8b\3\u1a9f\3\u1a9f\3\u1ac2\3\u1afa\3\u1c02")
        buf.write("\3\u1c0a\3\u1c0c\3\u1c30\3\u1c42\3\u1c42\3\u1c74\3\u1c91")
        buf.write("\3\u1d02\3\u1d08\3\u1d0a\3\u1d0b\3\u1d0d\3\u1d32\3\u1d48")
        buf.write("\3\u1d48\3\u1d62\3\u1d67\3\u1d69\3\u1d6a\3\u1d6c\3\u1d8b")
        buf.write("\3\u1d9a\3\u1d9a\3\u1ee2\3\u1ef4\3\u1fb2\3\u1fb2\3\u2002")
        buf.write("\3\u239b\3\u2402\3\u2470\3\u2482\3\u2545\3\u3002\3\u3430")
        buf.write("\3\u4402\3\u4648\3\u6802\3\u6a3a\3\u6a42\3\u6a60\3\u6ad2")
        buf.write("\3\u6aef\3\u6b02\3\u6b31\3\u6b42\3\u6b45\3\u6b65\3\u6b79")
        buf.write("\3\u6b7f\3\u6b91\3\u6e42\3\u6e81\3\u6f02\3\u6f4c\3\u6f52")
        buf.write("\3\u6f52\3\u6f95\3\u6fa1\3\u6fe2\3\u6fe3\3\u6fe5\3\u6fe5")
        buf.write("\3\u7002\3\u87f9\3\u8802\3\u8cd7\3\u8d02\3\u8d0a\3\ub002")
        buf.write("\3\ub120\3\ub152\3\ub154\3\ub166\3\ub169\3\ub172\3\ub2fd")
        buf.write("\3\ubc02\3\ubc6c\3\ubc72\3\ubc7e\3\ubc82\3\ubc8a\3\ubc92")
        buf.write("\3\ubc9b\3\ud402\3\ud456\3\ud458\3\ud49e\3\ud4a0\3\ud4a1")
        buf.write("\3\ud4a4\3\ud4a4\3\ud4a7\3\ud4a8\3\ud4ab\3\ud4ae\3\ud4b0")
        buf.write("\3\ud4bb\3\ud4bd\3\ud4bd\3\ud4bf\3\ud4c5\3\ud4c7\3\ud507")
        buf.write("\3\ud509\3\ud50c\3\ud50f\3\ud516\3\ud518\3\ud51e\3\ud520")
        buf.write("\3\ud53b\3\ud53d\3\ud540\3\ud542\3\ud546\3\ud548\3\ud548")
        buf.write("\3\ud54c\3\ud552\3\ud554\3\ud6a7\3\ud6aa\3\ud6c2\3\ud6c4")
        buf.write("\3\ud6dc\3\ud6de\3\ud6fc\3\ud6fe\3\ud716\3\ud718\3\ud736")
        buf.write("\3\ud738\3\ud750\3\ud752\3\ud770\3\ud772\3\ud78a\3\ud78c")
        buf.write("\3\ud7aa\3\ud7ac\3\ud7c4\3\ud7c6\3\ud7cd\3\ue102\3\ue12e")
        buf.write("\3\ue139\3\ue13f\3\ue150\3\ue150\3\ue2c2\3\ue2ed\3\ue802")
        buf.write("\3\ue8c6\3\ue902\3\ue945\3\ue94d\3\ue94d\3\uee02\3\uee05")
        buf.write("\3\uee07\3\uee21\3\uee23\3\uee24\3\uee26\3\uee26\3\uee29")
        buf.write("\3\uee29\3\uee2b\3\uee34\3\uee36\3\uee39\3\uee3b\3\uee3b")
        buf.write("\3\uee3d\3\uee3d\3\uee44\3\uee44\3\uee49\3\uee49\3\uee4b")
        buf.write("\3\uee4b\3\uee4d\3\uee4d\3\uee4f\3\uee51\3\uee53\3\uee54")
        buf.write("\3\uee56\3\uee56\3\uee59\3\uee59\3\uee5b\3\uee5b\3\uee5d")
        buf.write("\3\uee5d\3\uee5f\3\uee5f\3\uee61\3\uee61\3\uee63\3\uee64")
        buf.write("\3\uee66\3\uee66\3\uee69\3\uee6c\3\uee6e\3\uee74\3\uee76")
        buf.write("\3\uee79\3\uee7b\3\uee7e\3\uee80\3\uee80\3\uee82\3\uee8b")
        buf.write("\3\uee8d\3\uee9d\3\ueea3\3\ueea5\3\ueea7\3\ueeab\3\ueead")
        buf.write("\3\ueebd\3\2\4\ua6df\4\ua702\4\ub736\4\ub742\4\ub81f\4")
        buf.write("\ub822\4\ucea3\4\uceb2\4\uebe2\4\uf802\4\ufa1f\4\2\5\u134c")
        buf.write("\5\u0162\2\62\2;\2a\2a\2\u0302\2\u0371\2\u0485\2\u0489")
        buf.write("\2\u0593\2\u05bf\2\u05c1\2\u05c1\2\u05c3\2\u05c4\2\u05c6")
        buf.write("\2\u05c7\2\u05c9\2\u05c9\2\u0612\2\u061c\2\u064d\2\u066b")
        buf.write("\2\u0672\2\u0672\2\u06d8\2\u06de\2\u06e1\2\u06e6\2\u06e9")
        buf.write("\2\u06ea\2\u06ec\2\u06ef\2\u06f2\2\u06fb\2\u0713\2\u0713")
        buf.write("\2\u0732\2\u074c\2\u07a8\2\u07b2\2\u07c2\2\u07cb\2\u07ed")
        buf.write("\2\u07f5\2\u07ff\2\u07ff\2\u0818\2\u081b\2\u081d\2\u0825")
        buf.write("\2\u0827\2\u0829\2\u082b\2\u082f\2\u085b\2\u085d\2\u08d5")
        buf.write("\2\u08e3\2\u08e5\2\u0905\2\u093c\2\u093e\2\u0940\2\u0951")
        buf.write("\2\u0953\2\u0959\2\u0964\2\u0965\2\u0968\2\u0971\2\u0983")
        buf.write("\2\u0985\2\u09be\2\u09be\2\u09c0\2\u09c6\2\u09c9\2\u09ca")
        buf.write("\2\u09cd\2\u09cf\2\u09d9\2\u09d9\2\u09e4\2\u09e5\2\u09e8")
        buf.write("\2\u09f1\2\u0a00\2\u0a00\2\u0a03\2\u0a05\2\u0a3e\2\u0a3e")
        buf.write("\2\u0a40\2\u0a44\2\u0a49\2\u0a4a\2\u0a4d\2\u0a4f\2\u0a53")
        buf.write("\2\u0a53\2\u0a68\2\u0a73\2\u0a77\2\u0a77\2\u0a83\2\u0a85")
        buf.write("\2\u0abe\2\u0abe\2\u0ac0\2\u0ac7\2\u0ac9\2\u0acb\2\u0acd")
        buf.write("\2\u0acf\2\u0ae4\2\u0ae5\2\u0ae8\2\u0af1\2\u0afc\2\u0b01")
        buf.write("\2\u0b03\2\u0b05\2\u0b3e\2\u0b3e\2\u0b40\2\u0b46\2\u0b49")
        buf.write("\2\u0b4a\2\u0b4d\2\u0b4f\2\u0b57\2\u0b59\2\u0b64\2\u0b65")
        buf.write("\2\u0b68\2\u0b71\2\u0b84\2\u0b84\2\u0bc0\2\u0bc4\2\u0bc8")
        buf.write("\2\u0bca\2\u0bcc\2\u0bcf\2\u0bd9\2\u0bd9\2\u0be8\2\u0bf1")
        buf.write("\2\u0c02\2\u0c06\2\u0c40\2\u0c46\2\u0c48\2\u0c4a\2\u0c4c")
        buf.write("\2\u0c4f\2\u0c57\2\u0c58\2\u0c64\2\u0c65\2\u0c68\2\u0c71")
        buf.write("\2\u0c83\2\u0c85\2\u0cbe\2\u0cbe\2\u0cc0\2\u0cc6\2\u0cc8")
        buf.write("\2\u0cca\2\u0ccc\2\u0ccf\2\u0cd7\2\u0cd8\2\u0ce4\2\u0ce5")
        buf.write("\2\u0ce8\2\u0cf1\2\u0d02\2\u0d05\2\u0d3d\2\u0d3e\2\u0d40")
        buf.write("\2\u0d46\2\u0d48\2\u0d4a\2\u0d4c\2\u0d4f\2\u0d59\2\u0d59")
        buf.write("\2\u0d64\2\u0d65\2\u0d68\2\u0d71\2\u0d83\2\u0d85\2\u0dcc")
        buf.write("\2\u0dcc\2\u0dd1\2\u0dd6\2\u0dd8\2\u0dd8\2\u0dda\2\u0de1")
        buf.write("\2\u0de8\2\u0df1\2\u0df4\2\u0df5\2\u0e33\2\u0e33\2\u0e36")
        buf.write("\2\u0e3c\2\u0e49\2\u0e50\2\u0e52\2\u0e5b\2\u0eb3\2\u0eb3")
        buf.write("\2\u0eb6\2\u0ebe\2\u0eca\2\u0ecf\2\u0ed2\2\u0edb\2\u0f1a")
        buf.write("\2\u0f1b\2\u0f22\2\u0f2b\2\u0f37\2\u0f37\2\u0f39\2\u0f39")
        buf.write("\2\u0f3b\2\u0f3b\2\u0f40\2\u0f41\2\u0f73\2\u0f86\2\u0f88")
        buf.write("\2\u0f89\2\u0f8f\2\u0f99\2\u0f9b\2\u0fbe\2\u0fc8\2\u0fc8")
        buf.write("\2\u102d\2\u1040\2\u1042\2\u104b\2\u1058\2\u105b\2\u1060")
        buf.write("\2\u1062\2\u1064\2\u1066\2\u1069\2\u106f\2\u1073\2\u1076")
        buf.write("\2\u1084\2\u108f\2\u1091\2\u109f\2\u135f\2\u1361\2\u1714")
        buf.write("\2\u1716\2\u1734\2\u1736\2\u1754\2\u1755\2\u1774\2\u1775")
        buf.write("\2\u17b6\2\u17d5\2\u17df\2\u17df\2\u17e2\2\u17eb\2\u180d")
        buf.write("\2\u180f\2\u1812\2\u181b\2\u1887\2\u1888\2\u18ab\2\u18ab")
        buf.write("\2\u1922\2\u192d\2\u1932\2\u193d\2\u1948\2\u1951\2\u19d2")
        buf.write("\2\u19db\2\u1a19\2\u1a1d\2\u1a57\2\u1a60\2\u1a62\2\u1a7e")
        buf.write("\2\u1a81\2\u1a8b\2\u1a92\2\u1a9b\2\u1ab2\2\u1abf\2\u1ac1")
        buf.write("\2\u1ac2\2\u1b02\2\u1b06\2\u1b36\2\u1b46\2\u1b52\2\u1b5b")
        buf.write("\2\u1b6d\2\u1b75\2\u1b82\2\u1b84\2\u1ba3\2\u1baf\2\u1bb2")
        buf.write("\2\u1bbb\2\u1be8\2\u1bf5\2\u1c26\2\u1c39\2\u1c42\2\u1c4b")
        buf.write("\2\u1c52\2\u1c5b\2\u1cd2\2\u1cd4\2\u1cd6\2\u1cea\2\u1cef")
        buf.write("\2\u1cef\2\u1cf6\2\u1cf6\2\u1cf9\2\u1cfb\2\u1dc2\2\u1dfb")
        buf.write("\2\u1dfd\2\u1e01\2\u2041\2\u2042\2\u2056\2\u2056\2\u20d2")
        buf.write("\2\u20de\2\u20e3\2\u20e3\2\u20e7\2\u20f2\2\u2cf1\2\u2cf3")
        buf.write("\2\u2d81\2\u2d81\2\u2de2\2\u2e01\2\u302c\2\u3031\2\u309b")
        buf.write("\2\u309c\2\ua622\2\ua62b\2\ua671\2\ua671\2\ua676\2\ua67f")
        buf.write("\2\ua6a0\2\ua6a1\2\ua6f2\2\ua6f3\2\ua804\2\ua804\2\ua808")
        buf.write("\2\ua808\2\ua80d\2\ua80d\2\ua825\2\ua829\2\ua82e\2\ua82e")
        buf.write("\2\ua882\2\ua883\2\ua8b6\2\ua8c7\2\ua8d2\2\ua8db\2\ua8e2")
        buf.write("\2\ua8f3\2\ua901\2\ua90b\2\ua928\2\ua92f\2\ua949\2\ua955")
        buf.write("\2\ua982\2\ua985\2\ua9b5\2\ua9c2\2\ua9d2\2\ua9db\2\ua9e7")
        buf.write("\2\ua9e7\2\ua9f2\2\ua9fb\2\uaa2b\2\uaa38\2\uaa45\2\uaa45")
        buf.write("\2\uaa4e\2\uaa4f\2\uaa52\2\uaa5b\2\uaa7d\2\uaa7f\2\uaab2")
        buf.write("\2\uaab2\2\uaab4\2\uaab6\2\uaab9\2\uaaba\2\uaac0\2\uaac1")
        buf.write("\2\uaac3\2\uaac3\2\uaaed\2\uaaf1\2\uaaf7\2\uaaf8\2\uabe5")
        buf.write("\2\uabec\2\uabee\2\uabef\2\uabf2\2\uabfb\2\ufb20\2\ufb20")
        buf.write("\2\ufe02\2\ufe11\2\ufe22\2\ufe31\2\ufe35\2\ufe36\2\ufe4f")
        buf.write("\2\ufe51\2\uff12\2\uff1b\2\uff41\2\uff41\2\u01ff\3\u01ff")
        buf.write("\3\u02e2\3\u02e2\3\u0378\3\u037c\3\u04a2\3\u04ab\3\u0a03")
        buf.write("\3\u0a05\3\u0a07\3\u0a08\3\u0a0e\3\u0a11\3\u0a3a\3\u0a3c")
        buf.write("\3\u0a41\3\u0a41\3\u0ae7\3\u0ae8\3\u0d26\3\u0d29\3\u0d32")
        buf.write("\3\u0d3b\3\u0ead\3\u0eae\3\u0f48\3\u0f52\3\u1002\3\u1004")
        buf.write("\3\u103a\3\u1048\3\u1068\3\u1071\3\u1081\3\u1084\3\u10b2")
        buf.write("\3\u10bc\3\u10f2\3\u10fb\3\u1102\3\u1104\3\u1129\3\u1136")
        buf.write("\3\u1138\3\u1141\3\u1147\3\u1148\3\u1175\3\u1175\3\u1182")
        buf.write("\3\u1184\3\u11b5\3\u11c2\3\u11cb\3\u11ce\3\u11d0\3\u11db")
        buf.write("\3\u122e\3\u1239\3\u1240\3\u1240\3\u12e1\3\u12ec\3\u12f2")
        buf.write("\3\u12fb\3\u1302\3\u1305\3\u133d\3\u133e\3\u1340\3\u1346")
        buf.write("\3\u1349\3\u134a\3\u134d\3\u134f\3\u1359\3\u1359\3\u1364")
        buf.write("\3\u1365\3\u1368\3\u136e\3\u1372\3\u1376\3\u1437\3\u1448")
        buf.write("\3\u1452\3\u145b\3\u1460\3\u1460\3\u14b2\3\u14c5\3\u14d2")
        buf.write("\3\u14db\3\u15b1\3\u15b7\3\u15ba\3\u15c2\3\u15de\3\u15df")
        buf.write("\3\u1632\3\u1642\3\u1652\3\u165b\3\u16ad\3\u16b9\3\u16c2")
        buf.write("\3\u16cb\3\u171f\3\u172d\3\u1732\3\u173b\3\u182e\3\u183c")
        buf.write("\3\u18e2\3\u18eb\3\u1932\3\u1937\3\u1939\3\u193a\3\u193d")
        buf.write("\3\u1940\3\u1942\3\u1942\3\u1944\3\u1945\3\u1952\3\u195b")
        buf.write("\3\u19d3\3\u19d9\3\u19dc\3\u19e2\3\u19e6\3\u19e6\3\u1a03")
        buf.write("\3\u1a0c\3\u1a35\3\u1a3b\3\u1a3d\3\u1a40\3\u1a49\3\u1a49")
        buf.write("\3\u1a53\3\u1a5d\3\u1a8c\3\u1a9b\3\u1c31\3\u1c38\3\u1c3a")
        buf.write("\3\u1c41\3\u1c52\3\u1c5b\3\u1c94\3\u1ca9\3\u1cab\3\u1cb8")
        buf.write("\3\u1d33\3\u1d38\3\u1d3c\3\u1d3c\3\u1d3e\3\u1d3f\3\u1d41")
        buf.write("\3\u1d47\3\u1d49\3\u1d49\3\u1d52\3\u1d5b\3\u1d8c\3\u1d90")
        buf.write("\3\u1d92\3\u1d93\3\u1d95\3\u1d99\3\u1da2\3\u1dab\3\u1ef5")
        buf.write("\3\u1ef8\3\u6a62\3\u6a6b\3\u6af2\3\u6af6\3\u6b32\3\u6b38")
        buf.write("\3\u6b52\3\u6b5b\3\u6f51\3\u6f51\3\u6f53\3\u6f89\3\u6f91")
        buf.write("\3\u6f94\3\u6fe6\3\u6fe6\3\u6ff2\3\u6ff3\3\ubc9f\3\ubca0")
        buf.write("\3\ud167\3\ud16b\3\ud16f\3\ud174\3\ud17d\3\ud184\3\ud187")
        buf.write("\3\ud18d\3\ud1ac\3\ud1af\3\ud244\3\ud246\3\ud7d0\3\ud801")
        buf.write("\3\uda02\3\uda38\3\uda3d\3\uda6e\3\uda77\3\uda77\3\uda86")
        buf.write("\3\uda86\3\uda9d\3\udaa1\3\udaa3\3\udab1\3\ue002\3\ue008")
        buf.write("\3\ue00a\3\ue01a\3\ue01d\3\ue023\3\ue025\3\ue026\3\ue028")
        buf.write("\3\ue02c\3\ue132\3\ue138\3\ue142\3\ue14b\3\ue2ee\3\ue2fb")
        buf.write("\3\ue8d2\3\ue8d8\3\ue946\3\ue94c\3\ue952\3\ue95b\3\ufbf2")
        buf.write("\3\ufbfb\3\u0102\20\u01f1\20\u03ba\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2")
        buf.write("\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd")
        buf.write("\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2")
        buf.write("\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2\2\2\u00cb")
        buf.write("\3\2\2\2\2\u00cd\3\2\2\2\3\u010b\3\2\2\2\5\u0110\3\2\2")
        buf.write("\2\7\u0116\3\2\2\2\t\u0118\3\2\2\2\13\u011c\3\2\2\2\r")
        buf.write("\u011f\3\2\2\2\17\u0126\3\2\2\2\21\u012c\3\2\2\2\23\u0132")
        buf.write("\3\2\2\2\25\u0138\3\2\2\2\27\u013d\3\2\2\2\31\u0143\3")
        buf.write("\2\2\2\33\u014c\3\2\2\2\35\u0150\3\2\2\2\37\u0154\3\2")
        buf.write("\2\2!\u0159\3\2\2\2#\u015e\3\2\2\2%\u0165\3\2\2\2\'\u016b")
        buf.write("\3\2\2\2)\u0173\3\2\2\2+\u0177\3\2\2\2-\u017c\3\2\2\2")
        buf.write("/\u0183\3\2\2\2\61\u0186\3\2\2\2\63\u018d\3\2\2\2\65\u0190")
        buf.write("\3\2\2\2\67\u0193\3\2\2\29\u019a\3\2\2\2;\u01a0\3\2\2")
        buf.write("\2=\u01a5\3\2\2\2?\u01ae\3\2\2\2A\u01b2\3\2\2\2C\u01b5")
        buf.write("\3\2\2\2E\u01ba\3\2\2\2G\u01c0\3\2\2\2I\u01c7\3\2\2\2")
        buf.write("K\u01cc\3\2\2\2M\u01d0\3\2\2\2O\u01d2\3\2\2\2Q\u01d8\3")
        buf.write("\2\2\2S\u01dd\3\2\2\2U\u01ef\3\2\2\2W\u01f3\3\2\2\2Y\u01ff")
        buf.write("\3\2\2\2[\u020a\3\2\2\2]\u021c\3\2\2\2_\u021e\3\2\2\2")
        buf.write("a\u0225\3\2\2\2c\u022c\3\2\2\2e\u0235\3\2\2\2g\u0239\3")
        buf.write("\2\2\2i\u023d\3\2\2\2k\u023f\3\2\2\2m\u0243\3\2\2\2o\u0245")
        buf.write("\3\2\2\2q\u0248\3\2\2\2s\u024b\3\2\2\2u\u024d\3\2\2\2")
        buf.write("w\u024f\3\2\2\2y\u0251\3\2\2\2{\u0254\3\2\2\2}\u0256\3")
        buf.write("\2\2\2\177\u0259\3\2\2\2\u0081\u025c\3\2\2\2\u0083\u025e")
        buf.write("\3\2\2\2\u0085\u0260\3\2\2\2\u0087\u0262\3\2\2\2\u0089")
        buf.write("\u0265\3\2\2\2\u008b\u0268\3\2\2\2\u008d\u026a\3\2\2\2")
        buf.write("\u008f\u026c\3\2\2\2\u0091\u026e\3\2\2\2\u0093\u0270\3")
        buf.write("\2\2\2\u0095\u0273\3\2\2\2\u0097\u0275\3\2\2\2\u0099\u0278")
        buf.write("\3\2\2\2\u009b\u027b\3\2\2\2\u009d\u027d\3\2\2\2\u009f")
        buf.write("\u027f\3\2\2\2\u00a1\u0282\3\2\2\2\u00a3\u0285\3\2\2\2")
        buf.write("\u00a5\u0288\3\2\2\2\u00a7\u028b\3\2\2\2\u00a9\u028e\3")
        buf.write("\2\2\2\u00ab\u0290\3\2\2\2\u00ad\u0293\3\2\2\2\u00af\u0296")
        buf.write("\3\2\2\2\u00b1\u0299\3\2\2\2\u00b3\u029c\3\2\2\2\u00b5")
        buf.write("\u029f\3\2\2\2\u00b7\u02a2\3\2\2\2\u00b9\u02a5\3\2\2\2")
        buf.write("\u00bb\u02a8\3\2\2\2\u00bd\u02ab\3\2\2\2\u00bf\u02ae\3")
        buf.write("\2\2\2\u00c1\u02b2\3\2\2\2\u00c3\u02b6\3\2\2\2\u00c5\u02ba")
        buf.write("\3\2\2\2\u00c7\u02be\3\2\2\2\u00c9\u02c0\3\2\2\2\u00cb")
        buf.write("\u02c7\3\2\2\2\u00cd\u02cb\3\2\2\2\u00cf\u02df\3\2\2\2")
        buf.write("\u00d1\u02fb\3\2\2\2\u00d3\u02ff\3\2\2\2\u00d5\u0301\3")
        buf.write("\2\2\2\u00d7\u0307\3\2\2\2\u00d9\u0309\3\2\2\2\u00db\u030b")
        buf.write("\3\2\2\2\u00dd\u030d\3\2\2\2\u00df\u030f\3\2\2\2\u00e1")
        buf.write("\u0311\3\2\2\2\u00e3\u031a\3\2\2\2\u00e5\u031e\3\2\2\2")
        buf.write("\u00e7\u0323\3\2\2\2\u00e9\u0327\3\2\2\2\u00eb\u032d\3")
        buf.write("\2\2\2\u00ed\u0348\3\2\2\2\u00ef\u0364\3\2\2\2\u00f1\u0368")
        buf.write("\3\2\2\2\u00f3\u036b\3\2\2\2\u00f5\u036e\3\2\2\2\u00f7")
        buf.write("\u0371\3\2\2\2\u00f9\u0373\3\2\2\2\u00fb\u0377\3\2\2\2")
        buf.write("\u00fd\u037b\3\2\2\2\u00ff\u0382\3\2\2\2\u0101\u038d\3")
        buf.write("\2\2\2\u0103\u038f\3\2\2\2\u0105\u0393\3\2\2\2\u0107\u0398")
        buf.write("\3\2\2\2\u0109\u010c\5Y-\2\u010a\u010c\5[.\2\u010b\u0109")
        buf.write("\3\2\2\2\u010b\u010a\3\2\2\2\u010c\4\3\2\2\2\u010d\u0111")
        buf.write("\5\7\4\2\u010e\u0111\5e\63\2\u010f\u0111\5g\64\2\u0110")
        buf.write("\u010d\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u010f\3\2\2\2")
        buf.write("\u0111\6\3\2\2\2\u0112\u0117\5]/\2\u0113\u0117\5_\60\2")
        buf.write("\u0114\u0117\5a\61\2\u0115\u0117\5c\62\2\u0116\u0112\3")
        buf.write("\2\2\2\u0116\u0113\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0115")
        buf.write("\3\2\2\2\u0117\b\3\2\2\2\u0118\u0119\7c\2\2\u0119\u011a")
        buf.write("\7p\2\2\u011a\u011b\7f\2\2\u011b\n\3\2\2\2\u011c\u011d")
        buf.write("\7c\2\2\u011d\u011e\7u\2\2\u011e\f\3\2\2\2\u011f\u0120")
        buf.write("\7c\2\2\u0120\u0121\7u\2\2\u0121\u0122\7u\2\2\u0122\u0123")
        buf.write("\7g\2\2\u0123\u0124\7t\2\2\u0124\u0125\7v\2\2\u0125\16")
        buf.write("\3\2\2\2\u0126\u0127\7c\2\2\u0127\u0128\7u\2\2\u0128\u0129")
        buf.write("\7{\2\2\u0129\u012a\7p\2\2\u012a\u012b\7e\2\2\u012b\20")
        buf.write("\3\2\2\2\u012c\u012d\7c\2\2\u012d\u012e\7y\2\2\u012e\u012f")
        buf.write("\7c\2\2\u012f\u0130\7k\2\2\u0130\u0131\7v\2\2\u0131\22")
        buf.write("\3\2\2\2\u0132\u0133\7d\2\2\u0133\u0134\7t\2\2\u0134\u0135")
        buf.write("\7g\2\2\u0135\u0136\7c\2\2\u0136\u0137\7m\2\2\u0137\24")
        buf.write("\3\2\2\2\u0138\u0139\7e\2\2\u0139\u013a\7c\2\2\u013a\u013b")
        buf.write("\7u\2\2\u013b\u013c\7g\2\2\u013c\26\3\2\2\2\u013d\u013e")
        buf.write("\7e\2\2\u013e\u013f\7n\2\2\u013f\u0140\7c\2\2\u0140\u0141")
        buf.write("\7u\2\2\u0141\u0142\7u\2\2\u0142\30\3\2\2\2\u0143\u0144")
        buf.write("\7e\2\2\u0144\u0145\7q\2\2\u0145\u0146\7p\2\2\u0146\u0147")
        buf.write("\7v\2\2\u0147\u0148\7k\2\2\u0148\u0149\7p\2\2\u0149\u014a")
        buf.write("\7w\2\2\u014a\u014b\7g\2\2\u014b\32\3\2\2\2\u014c\u014d")
        buf.write("\7f\2\2\u014d\u014e\7g\2\2\u014e\u014f\7h\2\2\u014f\34")
        buf.write("\3\2\2\2\u0150\u0151\7f\2\2\u0151\u0152\7g\2\2\u0152\u0153")
        buf.write("\7n\2\2\u0153\36\3\2\2\2\u0154\u0155\7g\2\2\u0155\u0156")
        buf.write("\7n\2\2\u0156\u0157\7k\2\2\u0157\u0158\7h\2\2\u0158 \3")
        buf.write("\2\2\2\u0159\u015a\7g\2\2\u015a\u015b\7n\2\2\u015b\u015c")
        buf.write("\7u\2\2\u015c\u015d\7g\2\2\u015d\"\3\2\2\2\u015e\u015f")
        buf.write("\7g\2\2\u015f\u0160\7z\2\2\u0160\u0161\7e\2\2\u0161\u0162")
        buf.write("\7g\2\2\u0162\u0163\7r\2\2\u0163\u0164\7v\2\2\u0164$\3")
        buf.write("\2\2\2\u0165\u0166\7H\2\2\u0166\u0167\7c\2\2\u0167\u0168")
        buf.write("\7n\2\2\u0168\u0169\7u\2\2\u0169\u016a\7g\2\2\u016a&\3")
        buf.write("\2\2\2\u016b\u016c\7h\2\2\u016c\u016d\7k\2\2\u016d\u016e")
        buf.write("\7p\2\2\u016e\u016f\7c\2\2\u016f\u0170\7n\2\2\u0170\u0171")
        buf.write("\7n\2\2\u0171\u0172\7{\2\2\u0172(\3\2\2\2\u0173\u0174")
        buf.write("\7h\2\2\u0174\u0175\7q\2\2\u0175\u0176\7t\2\2\u0176*\3")
        buf.write("\2\2\2\u0177\u0178\7h\2\2\u0178\u0179\7t\2\2\u0179\u017a")
        buf.write("\7q\2\2\u017a\u017b\7o\2\2\u017b,\3\2\2\2\u017c\u017d")
        buf.write("\7i\2\2\u017d\u017e\7n\2\2\u017e\u017f\7q\2\2\u017f\u0180")
        buf.write("\7d\2\2\u0180\u0181\7c\2\2\u0181\u0182\7n\2\2\u0182.\3")
        buf.write("\2\2\2\u0183\u0184\7k\2\2\u0184\u0185\7h\2\2\u0185\60")
        buf.write("\3\2\2\2\u0186\u0187\7k\2\2\u0187\u0188\7o\2\2\u0188\u0189")
        buf.write("\7r\2\2\u0189\u018a\7q\2\2\u018a\u018b\7t\2\2\u018b\u018c")
        buf.write("\7v\2\2\u018c\62\3\2\2\2\u018d\u018e\7k\2\2\u018e\u018f")
        buf.write("\7p\2\2\u018f\64\3\2\2\2\u0190\u0191\7k\2\2\u0191\u0192")
        buf.write("\7u\2\2\u0192\66\3\2\2\2\u0193\u0194\7n\2\2\u0194\u0195")
        buf.write("\7c\2\2\u0195\u0196\7o\2\2\u0196\u0197\7d\2\2\u0197\u0198")
        buf.write("\7f\2\2\u0198\u0199\7c\2\2\u01998\3\2\2\2\u019a\u019b")
        buf.write("\7o\2\2\u019b\u019c\7c\2\2\u019c\u019d\7v\2\2\u019d\u019e")
        buf.write("\7e\2\2\u019e\u019f\7j\2\2\u019f:\3\2\2\2\u01a0\u01a1")
        buf.write("\7P\2\2\u01a1\u01a2\7q\2\2\u01a2\u01a3\7p\2\2\u01a3\u01a4")
        buf.write("\7g\2\2\u01a4<\3\2\2\2\u01a5\u01a6\7p\2\2\u01a6\u01a7")
        buf.write("\7q\2\2\u01a7\u01a8\7p\2\2\u01a8\u01a9\7n\2\2\u01a9\u01aa")
        buf.write("\7q\2\2\u01aa\u01ab\7e\2\2\u01ab\u01ac\7c\2\2\u01ac\u01ad")
        buf.write("\7n\2\2\u01ad>\3\2\2\2\u01ae\u01af\7p\2\2\u01af\u01b0")
        buf.write("\7q\2\2\u01b0\u01b1\7v\2\2\u01b1@\3\2\2\2\u01b2\u01b3")
        buf.write("\7q\2\2\u01b3\u01b4\7t\2\2\u01b4B\3\2\2\2\u01b5\u01b6")
        buf.write("\7r\2\2\u01b6\u01b7\7c\2\2\u01b7\u01b8\7u\2\2\u01b8\u01b9")
        buf.write("\7u\2\2\u01b9D\3\2\2\2\u01ba\u01bb\7t\2\2\u01bb\u01bc")
        buf.write("\7c\2\2\u01bc\u01bd\7k\2\2\u01bd\u01be\7u\2\2\u01be\u01bf")
        buf.write("\7g\2\2\u01bfF\3\2\2\2\u01c0\u01c1\7t\2\2\u01c1\u01c2")
        buf.write("\7g\2\2\u01c2\u01c3\7v\2\2\u01c3\u01c4\7w\2\2\u01c4\u01c5")
        buf.write("\7t\2\2\u01c5\u01c6\7p\2\2\u01c6H\3\2\2\2\u01c7\u01c8")
        buf.write("\7V\2\2\u01c8\u01c9\7t\2\2\u01c9\u01ca\7w\2\2\u01ca\u01cb")
        buf.write("\7g\2\2\u01cbJ\3\2\2\2\u01cc\u01cd\7v\2\2\u01cd\u01ce")
        buf.write("\7t\2\2\u01ce\u01cf\7{\2\2\u01cfL\3\2\2\2\u01d0\u01d1")
        buf.write("\7a\2\2\u01d1N\3\2\2\2\u01d2\u01d3\7y\2\2\u01d3\u01d4")
        buf.write("\7j\2\2\u01d4\u01d5\7k\2\2\u01d5\u01d6\7n\2\2\u01d6\u01d7")
        buf.write("\7g\2\2\u01d7P\3\2\2\2\u01d8\u01d9\7y\2\2\u01d9\u01da")
        buf.write("\7k\2\2\u01da\u01db\7v\2\2\u01db\u01dc\7j\2\2\u01dcR\3")
        buf.write("\2\2\2\u01dd\u01de\7{\2\2\u01de\u01df\7k\2\2\u01df\u01e0")
        buf.write("\7g\2\2\u01e0\u01e1\7n\2\2\u01e1\u01e2\7f\2\2\u01e2T\3")
        buf.write("\2\2\2\u01e3\u01e4\6+\2\2\u01e4\u01f0\5\u00fb~\2\u01e5")
        buf.write("\u01e7\7\17\2\2\u01e6\u01e5\3\2\2\2\u01e6\u01e7\3\2\2")
        buf.write("\2\u01e7\u01e8\3\2\2\2\u01e8\u01eb\7\f\2\2\u01e9\u01eb")
        buf.write("\4\16\17\2\u01ea\u01e6\3\2\2\2\u01ea\u01e9\3\2\2\2\u01eb")
        buf.write("\u01ed\3\2\2\2\u01ec\u01ee\5\u00fb~\2\u01ed\u01ec\3\2")
        buf.write("\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f0\3\2\2\2\u01ef\u01e3")
        buf.write("\3\2\2\2\u01ef\u01ea\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1")
        buf.write("\u01f2\b+\2\2\u01f2V\3\2\2\2\u01f3\u01f7\5\u0105\u0083")
        buf.write("\2\u01f4\u01f6\5\u0107\u0084\2\u01f5\u01f4\3\2\2\2\u01f6")
        buf.write("\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8X\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa\u0200\t\2\2")
        buf.write("\2\u01fb\u01fc\t\3\2\2\u01fc\u0200\t\4\2\2\u01fd\u01fe")
        buf.write("\t\4\2\2\u01fe\u0200\t\3\2\2\u01ff\u01fa\3\2\2\2\u01ff")
        buf.write("\u01fb\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2")
        buf.write("\u0200\u0203\3\2\2\2\u0201\u0204\5\u00cfh\2\u0202\u0204")
        buf.write("\5\u00d1i\2\u0203\u0201\3\2\2\2\u0203\u0202\3\2\2\2\u0204")
        buf.write("Z\3\2\2\2\u0205\u020b\t\5\2\2\u0206\u0207\t\5\2\2\u0207")
        buf.write("\u020b\t\4\2\2\u0208\u0209\t\4\2\2\u0209\u020b\t\5\2\2")
        buf.write("\u020a\u0205\3\2\2\2\u020a\u0206\3\2\2\2\u020a\u0208\3")
        buf.write("\2\2\2\u020b\u020e\3\2\2\2\u020c\u020f\5\u00edw\2\u020d")
        buf.write("\u020f\5\u00efx\2\u020e\u020c\3\2\2\2\u020e\u020d\3\2")
        buf.write("\2\2\u020f\\\3\2\2\2\u0210\u0214\5\u00d9m\2\u0211\u0213")
        buf.write("\5\u00dbn\2\u0212\u0211\3\2\2\2\u0213\u0216\3\2\2\2\u0214")
        buf.write("\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u021d\3\2\2\2")
        buf.write("\u0216\u0214\3\2\2\2\u0217\u0219\7\62\2\2\u0218\u0217")
        buf.write("\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u0218\3\2\2\2\u021a")
        buf.write("\u021b\3\2\2\2\u021b\u021d\3\2\2\2\u021c\u0210\3\2\2\2")
        buf.write("\u021c\u0218\3\2\2\2\u021d^\3\2\2\2\u021e\u021f\7\62\2")
        buf.write("\2\u021f\u0221\t\6\2\2\u0220\u0222\5\u00ddo\2\u0221\u0220")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0221\3\2\2\2\u0223")
        buf.write("\u0224\3\2\2\2\u0224`\3\2\2\2\u0225\u0226\7\62\2\2\u0226")
        buf.write("\u0228\t\7\2\2\u0227\u0229\5\u00dfp\2\u0228\u0227\3\2")
        buf.write("\2\2\u0229\u022a\3\2\2\2\u022a\u0228\3\2\2\2\u022a\u022b")
        buf.write("\3\2\2\2\u022bb\3\2\2\2\u022c\u022d\7\62\2\2\u022d\u022f")
        buf.write("\t\5\2\2\u022e\u0230\5\u00e1q\2\u022f\u022e\3\2\2\2\u0230")
        buf.write("\u0231\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0232\3\2\2\2")
        buf.write("\u0232d\3\2\2\2\u0233\u0236\5\u00e3r\2\u0234\u0236\5\u00e5")
        buf.write("s\2\u0235\u0233\3\2\2\2\u0235\u0234\3\2\2\2\u0236f\3\2")
        buf.write("\2\2\u0237\u023a\5e\63\2\u0238\u023a\5\u00e7t\2\u0239")
        buf.write("\u0237\3\2\2\2\u0239\u0238\3\2\2\2\u023a\u023b\3\2\2\2")
        buf.write("\u023b\u023c\t\b\2\2\u023ch\3\2\2\2\u023d\u023e\7\60\2")
        buf.write("\2\u023ej\3\2\2\2\u023f\u0240\7\60\2\2\u0240\u0241\7\60")
        buf.write("\2\2\u0241\u0242\7\60\2\2\u0242l\3\2\2\2\u0243\u0244\7")
        buf.write(",\2\2\u0244n\3\2\2\2\u0245\u0246\7*\2\2\u0246\u0247\b")
        buf.write("8\3\2\u0247p\3\2\2\2\u0248\u0249\7+\2\2\u0249\u024a\b")
        buf.write("9\4\2\u024ar\3\2\2\2\u024b\u024c\7.\2\2\u024ct\3\2\2\2")
        buf.write("\u024d\u024e\7<\2\2\u024ev\3\2\2\2\u024f\u0250\7=\2\2")
        buf.write("\u0250x\3\2\2\2\u0251\u0252\7,\2\2\u0252\u0253\7,\2\2")
        buf.write("\u0253z\3\2\2\2\u0254\u0255\7?\2\2\u0255|\3\2\2\2\u0256")
        buf.write("\u0257\7]\2\2\u0257\u0258\b?\5\2\u0258~\3\2\2\2\u0259")
        buf.write("\u025a\7_\2\2\u025a\u025b\b@\6\2\u025b\u0080\3\2\2\2\u025c")
        buf.write("\u025d\7~\2\2\u025d\u0082\3\2\2\2\u025e\u025f\7`\2\2\u025f")
        buf.write("\u0084\3\2\2\2\u0260\u0261\7(\2\2\u0261\u0086\3\2\2\2")
        buf.write("\u0262\u0263\7>\2\2\u0263\u0264\7>\2\2\u0264\u0088\3\2")
        buf.write("\2\2\u0265\u0266\7@\2\2\u0266\u0267\7@\2\2\u0267\u008a")
        buf.write("\3\2\2\2\u0268\u0269\7-\2\2\u0269\u008c\3\2\2\2\u026a")
        buf.write("\u026b\7/\2\2\u026b\u008e\3\2\2\2\u026c\u026d\7\61\2\2")
        buf.write("\u026d\u0090\3\2\2\2\u026e\u026f\7\'\2\2\u026f\u0092\3")
        buf.write("\2\2\2\u0270\u0271\7\61\2\2\u0271\u0272\7\61\2\2\u0272")
        buf.write("\u0094\3\2\2\2\u0273\u0274\7\u0080\2\2\u0274\u0096\3\2")
        buf.write("\2\2\u0275\u0276\7}\2\2\u0276\u0277\bL\7\2\u0277\u0098")
        buf.write("\3\2\2\2\u0278\u0279\7\177\2\2\u0279\u027a\bM\b\2\u027a")
        buf.write("\u009a\3\2\2\2\u027b\u027c\7>\2\2\u027c\u009c\3\2\2\2")
        buf.write("\u027d\u027e\7@\2\2\u027e\u009e\3\2\2\2\u027f\u0280\7")
        buf.write("?\2\2\u0280\u0281\7?\2\2\u0281\u00a0\3\2\2\2\u0282\u0283")
        buf.write("\7@\2\2\u0283\u0284\7?\2\2\u0284\u00a2\3\2\2\2\u0285\u0286")
        buf.write("\7>\2\2\u0286\u0287\7?\2\2\u0287\u00a4\3\2\2\2\u0288\u0289")
        buf.write("\7>\2\2\u0289\u028a\7@\2\2\u028a\u00a6\3\2\2\2\u028b\u028c")
        buf.write("\7#\2\2\u028c\u028d\7?\2\2\u028d\u00a8\3\2\2\2\u028e\u028f")
        buf.write("\7B\2\2\u028f\u00aa\3\2\2\2\u0290\u0291\7/\2\2\u0291\u0292")
        buf.write("\7@\2\2\u0292\u00ac\3\2\2\2\u0293\u0294\7-\2\2\u0294\u0295")
        buf.write("\7?\2\2\u0295\u00ae\3\2\2\2\u0296\u0297\7/\2\2\u0297\u0298")
        buf.write("\7?\2\2\u0298\u00b0\3\2\2\2\u0299\u029a\7,\2\2\u029a\u029b")
        buf.write("\7?\2\2\u029b\u00b2\3\2\2\2\u029c\u029d\7B\2\2\u029d\u029e")
        buf.write("\7?\2\2\u029e\u00b4\3\2\2\2\u029f\u02a0\7\61\2\2\u02a0")
        buf.write("\u02a1\7?\2\2\u02a1\u00b6\3\2\2\2\u02a2\u02a3\7\'\2\2")
        buf.write("\u02a3\u02a4\7?\2\2\u02a4\u00b8\3\2\2\2\u02a5\u02a6\7")
        buf.write("(\2\2\u02a6\u02a7\7?\2\2\u02a7\u00ba\3\2\2\2\u02a8\u02a9")
        buf.write("\7~\2\2\u02a9\u02aa\7?\2\2\u02aa\u00bc\3\2\2\2\u02ab\u02ac")
        buf.write("\7`\2\2\u02ac\u02ad\7?\2\2\u02ad\u00be\3\2\2\2\u02ae\u02af")
        buf.write("\7>\2\2\u02af\u02b0\7>\2\2\u02b0\u02b1\7?\2\2\u02b1\u00c0")
        buf.write("\3\2\2\2\u02b2\u02b3\7@\2\2\u02b3\u02b4\7@\2\2\u02b4\u02b5")
        buf.write("\7?\2\2\u02b5\u00c2\3\2\2\2\u02b6\u02b7\7,\2\2\u02b7\u02b8")
        buf.write("\7,\2\2\u02b8\u02b9\7?\2\2\u02b9\u00c4\3\2\2\2\u02ba\u02bb")
        buf.write("\7\61\2\2\u02bb\u02bc\7\61\2\2\u02bc\u02bd\7?\2\2\u02bd")
        buf.write("\u00c6\3\2\2\2\u02be\u02bf\7A\2\2\u02bf\u00c8\3\2\2\2")
        buf.write("\u02c0\u02c1\7A\2\2\u02c1\u02c2\7#\2\2\u02c2\u02c3\7]")
        buf.write("\2\2\u02c3\u00ca\3\2\2\2\u02c4\u02c8\5\u00fb~\2\u02c5")
        buf.write("\u02c8\5\u00fd\177\2\u02c6\u02c8\5\u00ff\u0080\2\u02c7")
        buf.write("\u02c4\3\2\2\2\u02c7\u02c5\3\2\2\2\u02c7\u02c6\3\2\2\2")
        buf.write("\u02c8\u02c9\3\2\2\2\u02c9\u02ca\bf\t\2\u02ca\u00cc\3")
        buf.write("\2\2\2\u02cb\u02cc\13\2\2\2\u02cc\u00ce\3\2\2\2\u02cd")
        buf.write("\u02d2\7)\2\2\u02ce\u02d1\5\u00d7l\2\u02cf\u02d1\n\t\2")
        buf.write("\2\u02d0\u02ce\3\2\2\2\u02d0\u02cf\3\2\2\2\u02d1\u02d4")
        buf.write("\3\2\2\2\u02d2\u02d0\3\2\2\2\u02d2\u02d3\3\2\2\2\u02d3")
        buf.write("\u02d5\3\2\2\2\u02d4\u02d2\3\2\2\2\u02d5\u02e0\7)\2\2")
        buf.write("\u02d6\u02db\7$\2\2\u02d7\u02da\5\u00d7l\2\u02d8\u02da")
        buf.write("\n\n\2\2\u02d9\u02d7\3\2\2\2\u02d9\u02d8\3\2\2\2\u02da")
        buf.write("\u02dd\3\2\2\2\u02db\u02d9\3\2\2\2\u02db\u02dc\3\2\2\2")
        buf.write("\u02dc\u02de\3\2\2\2\u02dd\u02db\3\2\2\2\u02de\u02e0\7")
        buf.write("$\2\2\u02df\u02cd\3\2\2\2\u02df\u02d6\3\2\2\2\u02e0\u00d0")
        buf.write("\3\2\2\2\u02e1\u02e2\7)\2\2\u02e2\u02e3\7)\2\2\u02e3\u02e4")
        buf.write("\7)\2\2\u02e4\u02e8\3\2\2\2\u02e5\u02e7\5\u00d3j\2\u02e6")
        buf.write("\u02e5\3\2\2\2\u02e7\u02ea\3\2\2\2\u02e8\u02e9\3\2\2\2")
        buf.write("\u02e8\u02e6\3\2\2\2\u02e9\u02eb\3\2\2\2\u02ea\u02e8\3")
        buf.write("\2\2\2\u02eb\u02ec\7)\2\2\u02ec\u02ed\7)\2\2\u02ed\u02fc")
        buf.write("\7)\2\2\u02ee\u02ef\7$\2\2\u02ef\u02f0\7$\2\2\u02f0\u02f1")
        buf.write("\7$\2\2\u02f1\u02f5\3\2\2\2\u02f2\u02f4\5\u00d3j\2\u02f3")
        buf.write("\u02f2\3\2\2\2\u02f4\u02f7\3\2\2\2\u02f5\u02f6\3\2\2\2")
        buf.write("\u02f5\u02f3\3\2\2\2\u02f6\u02f8\3\2\2\2\u02f7\u02f5\3")
        buf.write("\2\2\2\u02f8\u02f9\7$\2\2\u02f9\u02fa\7$\2\2\u02fa\u02fc")
        buf.write("\7$\2\2\u02fb\u02e1\3\2\2\2\u02fb\u02ee\3\2\2\2\u02fc")
        buf.write("\u00d2\3\2\2\2\u02fd\u0300\5\u00d5k\2\u02fe\u0300\5\u00d7")
        buf.write("l\2\u02ff\u02fd\3\2\2\2\u02ff\u02fe\3\2\2\2\u0300\u00d4")
        buf.write("\3\2\2\2\u0301\u0302\n\13\2\2\u0302\u00d6\3\2\2\2\u0303")
        buf.write("\u0304\7^\2\2\u0304\u0308\13\2\2\2\u0305\u0306\7^\2\2")
        buf.write("\u0306\u0308\5U+\2\u0307\u0303\3\2\2\2\u0307\u0305\3\2")
        buf.write("\2\2\u0308\u00d8\3\2\2\2\u0309\u030a\t\f\2\2\u030a\u00da")
        buf.write("\3\2\2\2\u030b\u030c\t\r\2\2\u030c\u00dc\3\2\2\2\u030d")
        buf.write("\u030e\t\16\2\2\u030e\u00de\3\2\2\2\u030f\u0310\t\17\2")
        buf.write("\2\u0310\u00e0\3\2\2\2\u0311\u0312\t\20\2\2\u0312\u00e2")
        buf.write("\3\2\2\2\u0313\u0315\5\u00e7t\2\u0314\u0313\3\2\2\2\u0314")
        buf.write("\u0315\3\2\2\2\u0315\u0316\3\2\2\2\u0316\u031b\5\u00e9")
        buf.write("u\2\u0317\u0318\5\u00e7t\2\u0318\u0319\7\60\2\2\u0319")
        buf.write("\u031b\3\2\2\2\u031a\u0314\3\2\2\2\u031a\u0317\3\2\2\2")
        buf.write("\u031b\u00e4\3\2\2\2\u031c\u031f\5\u00e7t\2\u031d\u031f")
        buf.write("\5\u00e3r\2\u031e\u031c\3\2\2\2\u031e\u031d\3\2\2\2\u031f")
        buf.write("\u0320\3\2\2\2\u0320\u0321\5\u00ebv\2\u0321\u00e6\3\2")
        buf.write("\2\2\u0322\u0324\5\u00dbn\2\u0323\u0322\3\2\2\2\u0324")
        buf.write("\u0325\3\2\2\2\u0325\u0323\3\2\2\2\u0325\u0326\3\2\2\2")
        buf.write("\u0326\u00e8\3\2\2\2\u0327\u0329\7\60\2\2\u0328\u032a")
        buf.write("\5\u00dbn\2\u0329\u0328\3\2\2\2\u032a\u032b\3\2\2\2\u032b")
        buf.write("\u0329\3\2\2\2\u032b\u032c\3\2\2\2\u032c\u00ea\3\2\2\2")
        buf.write("\u032d\u032f\t\21\2\2\u032e\u0330\t\22\2\2\u032f\u032e")
        buf.write("\3\2\2\2\u032f\u0330\3\2\2\2\u0330\u0332\3\2\2\2\u0331")
        buf.write("\u0333\5\u00dbn\2\u0332\u0331\3\2\2\2\u0333\u0334\3\2")
        buf.write("\2\2\u0334\u0332\3\2\2\2\u0334\u0335\3\2\2\2\u0335\u00ec")
        buf.write("\3\2\2\2\u0336\u033b\7)\2\2\u0337\u033a\5\u00f3z\2\u0338")
        buf.write("\u033a\5\u00f9}\2\u0339\u0337\3\2\2\2\u0339\u0338\3\2")
        buf.write("\2\2\u033a\u033d\3\2\2\2\u033b\u0339\3\2\2\2\u033b\u033c")
        buf.write("\3\2\2\2\u033c\u033e\3\2\2\2\u033d\u033b\3\2\2\2\u033e")
        buf.write("\u0349\7)\2\2\u033f\u0344\7$\2\2\u0340\u0343\5\u00f5{")
        buf.write("\2\u0341\u0343\5\u00f9}\2\u0342\u0340\3\2\2\2\u0342\u0341")
        buf.write("\3\2\2\2\u0343\u0346\3\2\2\2\u0344\u0342\3\2\2\2\u0344")
        buf.write("\u0345\3\2\2\2\u0345\u0347\3\2\2\2\u0346\u0344\3\2\2\2")
        buf.write("\u0347\u0349\7$\2\2\u0348\u0336\3\2\2\2\u0348\u033f\3")
        buf.write("\2\2\2\u0349\u00ee\3\2\2\2\u034a\u034b\7)\2\2\u034b\u034c")
        buf.write("\7)\2\2\u034c\u034d\7)\2\2\u034d\u0351\3\2\2\2\u034e\u0350")
        buf.write("\5\u00f1y\2\u034f\u034e\3\2\2\2\u0350\u0353\3\2\2\2\u0351")
        buf.write("\u0352\3\2\2\2\u0351\u034f\3\2\2\2\u0352\u0354\3\2\2\2")
        buf.write("\u0353\u0351\3\2\2\2\u0354\u0355\7)\2\2\u0355\u0356\7")
        buf.write(")\2\2\u0356\u0365\7)\2\2\u0357\u0358\7$\2\2\u0358\u0359")
        buf.write("\7$\2\2\u0359\u035a\7$\2\2\u035a\u035e\3\2\2\2\u035b\u035d")
        buf.write("\5\u00f1y\2\u035c\u035b\3\2\2\2\u035d\u0360\3\2\2\2\u035e")
        buf.write("\u035f\3\2\2\2\u035e\u035c\3\2\2\2\u035f\u0361\3\2\2\2")
        buf.write("\u0360\u035e\3\2\2\2\u0361\u0362\7$\2\2\u0362\u0363\7")
        buf.write("$\2\2\u0363\u0365\7$\2\2\u0364\u034a\3\2\2\2\u0364\u0357")
        buf.write("\3\2\2\2\u0365\u00f0\3\2\2\2\u0366\u0369\5\u00f7|\2\u0367")
        buf.write("\u0369\5\u00f9}\2\u0368\u0366\3\2\2\2\u0368\u0367\3\2")
        buf.write("\2\2\u0369\u00f2\3\2\2\2\u036a\u036c\t\23\2\2\u036b\u036a")
        buf.write("\3\2\2\2\u036c\u00f4\3\2\2\2\u036d\u036f\t\24\2\2\u036e")
        buf.write("\u036d\3\2\2\2\u036f\u00f6\3\2\2\2\u0370\u0372\t\25\2")
        buf.write("\2\u0371\u0370\3\2\2\2\u0372\u00f8\3\2\2\2\u0373\u0374")
        buf.write("\7^\2\2\u0374\u0375\t\26\2\2\u0375\u00fa\3\2\2\2\u0376")
        buf.write("\u0378\t\27\2\2\u0377\u0376\3\2\2\2\u0378\u0379\3\2\2")
        buf.write("\2\u0379\u0377\3\2\2\2\u0379\u037a\3\2\2\2\u037a\u00fc")
        buf.write("\3\2\2\2\u037b\u037f\7%\2\2\u037c\u037e\n\30\2\2\u037d")
        buf.write("\u037c\3\2\2\2\u037e\u0381\3\2\2\2\u037f\u037d\3\2\2\2")
        buf.write("\u037f\u0380\3\2\2\2\u0380\u00fe\3\2\2\2\u0381\u037f\3")
        buf.write("\2\2\2\u0382\u0384\7^\2\2\u0383\u0385\5\u00fb~\2\u0384")
        buf.write("\u0383\3\2\2\2\u0384\u0385\3\2\2\2\u0385\u038b\3\2\2\2")
        buf.write("\u0386\u0388\7\17\2\2\u0387\u0386\3\2\2\2\u0387\u0388")
        buf.write("\3\2\2\2\u0388\u0389\3\2\2\2\u0389\u038c\7\f\2\2\u038a")
        buf.write("\u038c\4\16\17\2\u038b\u0387\3\2\2\2\u038b\u038a\3\2\2")
        buf.write("\2\u038c\u0100\3\2\2\2\u038d\u038e\t\31\2\2\u038e\u0102")
        buf.write("\3\2\2\2\u038f\u0390\t\32\2\2\u0390\u0104\3\2\2\2\u0391")
        buf.write("\u0394\t\33\2\2\u0392\u0394\5\u0101\u0081\2\u0393\u0391")
        buf.write("\3\2\2\2\u0393\u0392\3\2\2\2\u0394\u0106\3\2\2\2\u0395")
        buf.write("\u0399\5\u0105\u0083\2\u0396\u0399\t\34\2\2\u0397\u0399")
        buf.write("\5\u0103\u0082\2\u0398\u0395\3\2\2\2\u0398\u0396\3\2\2")
        buf.write("\2\u0398\u0397\3\2\2\2\u0399\u0108\3\2\2\2<\2\u010b\u0110")
        buf.write("\u0116\u01e6\u01ea\u01ed\u01ef\u01f7\u01ff\u0203\u020a")
        buf.write("\u020e\u0214\u021a\u021c\u0223\u022a\u0231\u0235\u0239")
        buf.write("\u02c7\u02d0\u02d2\u02d9\u02db\u02df\u02e8\u02f5\u02fb")
        buf.write("\u02ff\u0307\u0314\u031a\u031e\u0325\u032b\u032f\u0334")
        buf.write("\u0339\u033b\u0342\u0344\u0348\u0351\u035e\u0364\u0368")
        buf.write("\u036b\u036e\u0371\u0379\u037f\u0384\u0387\u038b\u0393")
        buf.write("\u0398\n\3+\2\38\3\39\4\3?\5\3@\6\3L\7\3M\b\b\2\2")
        return buf.getvalue()


class Python3Lexer(Python3LexerBase):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    STRING = 3
    NUMBER = 4
    INTEGER = 5
    AND = 6
    AS = 7
    ASSERT = 8
    ASYNC = 9
    AWAIT = 10
    BREAK = 11
    CASE = 12
    CLASS = 13
    CONTINUE = 14
    DEF = 15
    DEL = 16
    ELIF = 17
    ELSE = 18
    EXCEPT = 19
    FALSE = 20
    FINALLY = 21
    FOR = 22
    FROM = 23
    GLOBAL = 24
    IF = 25
    IMPORT = 26
    IN = 27
    IS = 28
    LAMBDA = 29
    MATCH = 30
    NONE = 31
    NONLOCAL = 32
    NOT = 33
    OR = 34
    PASS = 35
    RAISE = 36
    RETURN = 37
    TRUE = 38
    TRY = 39
    UNDERSCORE = 40
    WHILE = 41
    WITH = 42
    YIELD = 43
    NEWLINE = 44
    NAME = 45
    STRING_LITERAL = 46
    BYTES_LITERAL = 47
    DECIMAL_INTEGER = 48
    OCT_INTEGER = 49
    HEX_INTEGER = 50
    BIN_INTEGER = 51
    FLOAT_NUMBER = 52
    IMAG_NUMBER = 53
    DOT = 54
    ELLIPSIS = 55
    STAR = 56
    OPEN_PAREN = 57
    CLOSE_PAREN = 58
    COMMA = 59
    COLON = 60
    SEMI_COLON = 61
    POWER = 62
    ASSIGN = 63
    OPEN_BRACK = 64
    CLOSE_BRACK = 65
    OR_OP = 66
    XOR = 67
    AND_OP = 68
    LEFT_SHIFT = 69
    RIGHT_SHIFT = 70
    ADD = 71
    MINUS = 72
    DIV = 73
    MOD = 74
    IDIV = 75
    NOT_OP = 76
    OPEN_BRACE = 77
    CLOSE_BRACE = 78
    LESS_THAN = 79
    GREATER_THAN = 80
    EQUALS = 81
    GT_EQ = 82
    LT_EQ = 83
    NOT_EQ_1 = 84
    NOT_EQ_2 = 85
    AT = 86
    ARROW = 87
    ADD_ASSIGN = 88
    SUB_ASSIGN = 89
    MULT_ASSIGN = 90
    AT_ASSIGN = 91
    DIV_ASSIGN = 92
    MOD_ASSIGN = 93
    AND_ASSIGN = 94
    OR_ASSIGN = 95
    XOR_ASSIGN = 96
    LEFT_SHIFT_ASSIGN = 97
    RIGHT_SHIFT_ASSIGN = 98
    POWER_ASSIGN = 99
    IDIV_ASSIGN = 100
    WILDCARD = 101
    SYNTAX_STRICT_START = 102
    SKIP_ = 103
    UNKNOWN_CHAR = 104

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'and'", "'as'", "'assert'", "'async'", "'await'", "'break'", 
            "'case'", "'class'", "'continue'", "'def'", "'del'", "'elif'", 
            "'else'", "'except'", "'False'", "'finally'", "'for'", "'from'", 
            "'global'", "'if'", "'import'", "'in'", "'is'", "'lambda'", 
            "'match'", "'None'", "'nonlocal'", "'not'", "'or'", "'pass'", 
            "'raise'", "'return'", "'True'", "'try'", "'_'", "'while'", 
            "'with'", "'yield'", "'.'", "'...'", "'*'", "'('", "')'", "','", 
            "':'", "';'", "'**'", "'='", "'['", "']'", "'|'", "'^'", "'&'", 
            "'<<'", "'>>'", "'+'", "'-'", "'/'", "'%'", "'//'", "'~'", "'{'", 
            "'}'", "'<'", "'>'", "'=='", "'>='", "'<='", "'<>'", "'!='", 
            "'@'", "'->'", "'+='", "'-='", "'*='", "'@='", "'/='", "'%='", 
            "'&='", "'|='", "'^='", "'<<='", "'>>='", "'**='", "'//='", 
            "'?'", "'?!['" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "STRING", "NUMBER", "INTEGER", "AND", "AS", 
            "ASSERT", "ASYNC", "AWAIT", "BREAK", "CASE", "CLASS", "CONTINUE", 
            "DEF", "DEL", "ELIF", "ELSE", "EXCEPT", "FALSE", "FINALLY", 
            "FOR", "FROM", "GLOBAL", "IF", "IMPORT", "IN", "IS", "LAMBDA", 
            "MATCH", "NONE", "NONLOCAL", "NOT", "OR", "PASS", "RAISE", "RETURN", 
            "TRUE", "TRY", "UNDERSCORE", "WHILE", "WITH", "YIELD", "NEWLINE", 
            "NAME", "STRING_LITERAL", "BYTES_LITERAL", "DECIMAL_INTEGER", 
            "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", 
            "IMAG_NUMBER", "DOT", "ELLIPSIS", "STAR", "OPEN_PAREN", "CLOSE_PAREN", 
            "COMMA", "COLON", "SEMI_COLON", "POWER", "ASSIGN", "OPEN_BRACK", 
            "CLOSE_BRACK", "OR_OP", "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", 
            "ADD", "MINUS", "DIV", "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", 
            "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", 
            "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", "ADD_ASSIGN", 
            "SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", 
            "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", "WILDCARD", 
            "SYNTAX_STRICT_START", "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "STRING", "NUMBER", "INTEGER", "AND", "AS", "ASSERT", 
                  "ASYNC", "AWAIT", "BREAK", "CASE", "CLASS", "CONTINUE", 
                  "DEF", "DEL", "ELIF", "ELSE", "EXCEPT", "FALSE", "FINALLY", 
                  "FOR", "FROM", "GLOBAL", "IF", "IMPORT", "IN", "IS", "LAMBDA", 
                  "MATCH", "NONE", "NONLOCAL", "NOT", "OR", "PASS", "RAISE", 
                  "RETURN", "TRUE", "TRY", "UNDERSCORE", "WHILE", "WITH", 
                  "YIELD", "NEWLINE", "NAME", "STRING_LITERAL", "BYTES_LITERAL", 
                  "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
                  "FLOAT_NUMBER", "IMAG_NUMBER", "DOT", "ELLIPSIS", "STAR", 
                  "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", 
                  "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", 
                  "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", 
                  "DIV", "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", "CLOSE_BRACE", 
                  "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", 
                  "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", 
                  "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", "WILDCARD", 
                  "SYNTAX_STRICT_START", "SKIP_", "UNKNOWN_CHAR", "SHORT_STRING", 
                  "LONG_STRING", "LONG_STRING_ITEM", "LONG_STRING_CHAR", 
                  "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", "DIGIT", "OCT_DIGIT", 
                  "HEX_DIGIT", "BIN_DIGIT", "POINT_FLOAT", "EXPONENT_FLOAT", 
                  "INT_PART", "FRACTION", "EXPONENT", "SHORT_BYTES", "LONG_BYTES", 
                  "LONG_BYTES_ITEM", "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE", 
                  "SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE", "LONG_BYTES_CHAR", 
                  "BYTES_ESCAPE_SEQ", "SPACES", "COMMENT", "LINE_JOINING", 
                  "UNICODE_OIDS", "UNICODE_OIDC", "ID_START", "ID_CONTINUE" ]

    grammarFileName = "Python3Lexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[41] = self.NEWLINE_action 
            actions[54] = self.OPEN_PAREN_action 
            actions[55] = self.CLOSE_PAREN_action 
            actions[61] = self.OPEN_BRACK_action 
            actions[62] = self.CLOSE_BRACK_action 
            actions[74] = self.OPEN_BRACE_action 
            actions[75] = self.CLOSE_BRACE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.onNewLine();
     

    def OPEN_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.openBrace();
     

    def CLOSE_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.closeBrace();
     

    def OPEN_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.openBrace();
     

    def CLOSE_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.closeBrace();
     

    def OPEN_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.openBrace();
     

    def CLOSE_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.closeBrace();
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[41] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


