import re
import sys

def checkRegex(token):
  if(re.match(tokensreservados1,T)):
    print(re.match(tokensreservados1,T))
    print("t1")
  elif(re.match(tokensreservados2,T)):
    print(re.match(tokensreservados2,T))
    print("t2")
  elif(re.match(identificador,T)):
    print(re.match(identificador,T))
    print("Identifier")
  elif(re.match(entero,T)):
    print(re.match(entero,T))
    print("entero")
  else:
    print("ERROR MONDAFOCA")

entero = re.compile('[1-9]+')
identificador = re.compile('([a-z,A-Z])+[0-9]*')
tokensreservados1 = re.compile('{|}|#|\[|\]|\(|\)|>|<|\.|!|\+|-|\*|/|%|\^|=')
tokensreservados2 = re.compile('>=|<=|==|!=|in|&&|\|\|')

T = (sys.stdin.readline())

checkRegex(T)
