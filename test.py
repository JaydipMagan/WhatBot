from parser import parser
import sys

parse = parser()
try:
    parse.parse("help")
except SyntaxError as e:
    print(e)