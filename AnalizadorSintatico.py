import re
import sys

##--------------------EXPRESIONES REGULARES------------------

entero = re.compile('^[0-9]+$')
flotante = re.compile('^[0-9]+[.][0-9]*$')
identificador = re.compile('^(([a-zA-Z])+[0-9]*)+$')
tokensreservados1 = re.compile('^({$|}$|,$|:$|#$|\[$|\]$|\($|\)$|>$|<$|!$|\+$|-$|\*$|/$|%$|\^$|=$|\.$)+')
tokensreservados2 = re.compile('^(>=$|<=$|==$|!=$|&&$|\|\|$)+')
tokensLargos = re.compile('^(desde$|todo$|end$|retorno$|true$|false$|funcion$|retorno$|log$|end$|for$|while$|if$|in$|importar$|else$|nil$|elif$)+')
comentario = re.compile('^#.*')
stringCompleta = re.compile('^\".*\"$')
stringIncompleta = re.compile('^\".*')
espacios = re.compile('^(\ +|\n+|\t)+')

diccionarioTokens={'{':'token_llave_izq','}':'token_llave_der','#':'token_com','[':'token_cor_izq',']':'token_cor_der','(':'token_par_izq',')':'token_par_der','>':'token_mayor','<':'token_menor','.':'token_point','!':'token_not','+':'token_mas','-':'token_menos','*':'token_mul','/':'token_div','%':'token_mod','^':'token_pot','=':'token_assign','>=':'token_mayor_igual','<=':'token_menor_igual','==':'token_igual_num','!=':'token_diff_num','&&':'token_and','||':'token_or',',':'token_coma',':':'token_dosp','\.':'token_point'}

##------------------PILA DEL PROGRAMA-----------------------

pila=[];

##-----------------CONJUNTOS DE PREDICCION------------------

ATOM={
'<token_integer>':['<token_integer>'],
'<token_float>':['<token_float>'],
'<true>':['<true>'],
'<false>':['<false>'],
'<token_string>':['<token_string>'],
'<token_cor_izq>':[ARRAY],
'<token_llave_izq':[OBJETO],
'<id>':[VARIABLE],
'<nil>':['<nil>']
}

EXPR={
'<token_not':[EXPR2,FACTOREXPR2],
'<token_par_izq>':[EXPR2,FACTOREXPR2],
'<token_integer>':[EXPR2,FACTOREXPR2],
'<token_float>':[EXPR2,FACTOREXPR2],
'<true>':[EXPR2,FACTOREXPR2],
'<false>':[EXPR2,FACTOREXPR2],
'<token_string>':[EXPR2,FACTOREXPR2],
'<nil>':[EXPR2,FACTOREXPR2],
'<token_llave_izq>':[EXPR2,FACTOREXPR2],
'<id>':[EXPR2,FACTOREXPR2],
'<token_cor_izq>':[EXPR2,FACTOREXPR2]
}

EXPRCOMA={
'<token_menos>':['<token_menos>',EXPR],
'<token_not':[EXPR],
'<token_par_izq>':[EXPR],
'<token_integer>':[EXPR],
'<token_float>':[EXPR],
'<true>':[EXPR],
'<false>':[EXPR2],
'<token_string>':[EXPR2],
'<nil>':[EXPR2],
'<token_llave_izq>':[EXPR2],
'<id>':[EXPR2],
'<token_cor_izq>':[EXPR2]
}

EXPR2={'<token_not>':['<token_not>',EXPR2],
'<token_par_izq>':['<token_par_izq>',EXPRCOMA,'<token_par_der>'],
  
}

SOURCE={}

def checkLine(T,i):
  inicio=0
  last = 0
  k=0
  while(k <= len(T)):
    encontrado = checkRegex(T[inicio:k],i)
    #print(str(encontrado) + str(T[inicio:k]))
    #print(encontrado)
    if(((encontrado==0 or encontrado == "espacios") and (last != 0 and last != "espacios" and last != "completa"))):
      (darFormato(str(last),inicio,T[inicio:k-1],i))
      inicio = k-1
    elif(k==len(T) and encontrado=="espacios"):
      k+=1
    elif(k==len(T) and encontrado==0 and last == 0):
      (darFormato(str(encontrado),inicio,T[inicio:k],i))
      k+=1
    elif(k==len(T) and encontrado!=0):
      (darFormato(str(encontrado),inicio,T[inicio:k],i))
      k+=1
    elif(k==len(T) and encontrado==0 and last != 0):
      print("holi")
      (darFormato(str(last),inicio,T[inicio:k-1],i))
      (darFormato(str(encontrado),k-1,T[k-1:k],i))
      k+=1
    elif(encontrado=="espacios"):
      inicio = k
    elif(encontrado=="completa"):
      darFormato(str(encontrado),inicio,T[inicio:k],i)
      inicio=k
      k += 1
    else:
      k += 1
    last=encontrado

def darFormato(tipo, k, cadena,i):
  print("\n")
  if(tipo == "t1"):
    pila.append("<"+diccionarioTokens[cadena]+">")
  elif(tipo == "t2"):
    pila.append("<"+diccionarioTokens[cadena]+">")
  elif(tipo == "tl"):
    pila.append("<"+cadena+">")
  elif(tipo == "identificador"):
    pila.append("<id>")
  elif(tipo == "flotante"):
    pila.append("<token_float>")
  elif(tipo == "entero"):
    pila.append("<token_integer>")
  elif(tipo == "comentario"):
    return("")
  elif(tipo == "incompleta"):
    print("Error lexico(linea:"+str(i+1)+",posicion:"+str(k+1)+")")
  elif(tipo == "completa"):
    pila.append("<token_string>")
  elif(tipo == "0"):
    print(">>> Error lexico(linea:"+str(i+1)+",posicion:"+str(k+1)+")")
    sys.exit()

def checkRegex(T,i):
  if(re.search(comentario,T)):
    return("comentario")
  elif(re.search(stringCompleta,T)):
    return("completa")
  elif(re.search(stringIncompleta,T)):
    return("incompleta")
  elif(re.search(tokensreservados1,T)):
    return("t1")
  elif(re.search(tokensreservados2,T)):
    return("t2")
  elif(re.search(tokensLargos,T)):
    return("tl")
  elif(re.search(identificador,T)):
    return("identificador")
  elif(re.search(flotante,T)):
    return("flotante")
  elif(re.search(entero,T)):
    return("entero")
  elif(re.search(espacios,T)):
    return("espacios")
  else:
    return(0)

#i=0

Entrada= open("archivo.txt", "r")
lines = Entrada.readlines()
for i in range(0, len(lines)):
  if(len(lines[i][:-1])>=1):
    print(lines[i][:-1])
    checkLine(lines[i][:-1],i)
  pila.append("<enter>")
print(pila)

 
'''
while(True):
    try:
        lines = input()
        print(pila)
    except EOFError:
        print("\n")
        sys.exit()
    if(len(lines)>=1):
        checkLine(lines,i)
    i+=1
'''

Entrada.close()
