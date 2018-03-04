import re
import sys

entero = re.compile('^[0-9]+$')
flotante = re.compile('^[0-9]+.[0-9]+$')
identificador = re.compile('^(([a-z,A-Z])+[0-9]*)+$')
tokensreservados1 = re.compile('^({|}|#|\[|\]|\(|\)|>|<|!|\+|-|\*|/|%|\^|=)+$')
tokensreservados2 = re.compile('^(>=|<=|==|!=|in|&&|\|\|)+$')
tokensLargos = re.compile('^(true|false|funcion|retorno|log|end|for|while|if)+$')
comentario = re.compile('^#.*')
stringCompleta = re.compile('^\".*\"$')
stringIncompleta = re.compile('^\".*')
espacios = re.compile('^(\ +|\n+|\t)+')

diccionarioTokens={'{':'token_llave_izq','}':'token_llave_der','#':'token_com','[':'token_cor_izq',']':'token-cor-der','(':'token_par_izq',')':'token_par_der','>':'token_mayor','<':'token_menor','.':'token_point','!':'token_not','+':'token_mas','-':'token_menos','*':'token_mul','/':'token_div','%':'token_mod','^':'token_pot','=':'token_assign','>=':'token_mayor_igual','<=':'token_menor_igual','==':'token_igual_num','!=':'token_diff_num','in':'token_in','&&':'token_and','||':'token_or'}

def checkLine(T,i):
    inicio=0
    last = 0
    k=0
    while(k < len(T)):
        encontrado = checkRegex(T[inicio:k],i)
        #print(T[inicio:k])
        if(k==len(T)-1 and encontrado != 0):
            (darFormato(str(encontrado),inicio,T[inicio:k],i))
            k+=1
        elif(((encontrado==0 or encontrado == "espacios") and (last != 0 and last != "espacios"))):
            (darFormato(str(last),inicio,T[inicio:k-1],i))
            inicio = k-1
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
    if(tipo == "t1"):
        print("<"+diccionarioTokens[cadena]+","+str(i+1)+","+str(k+1)+">")
    elif(tipo == "t2"):
        print("<"+diccionarioTokens[cadena]+","+str(i+1)+","+str(k+1)+">")
    elif(tipo == "tl"):
        print("<"+cadena+","+str(i+1)+","+str(k+1)+">")
    elif(tipo == "identificador"):
        print("<id,"+cadena+","+str(i+1)+","+str(k+1)+">")
    elif(tipo == "flotante"):
        print("<token_float,"+cadena+","+str(i+1)+","+str(k+1)+">")
    elif(tipo == "entero"):
        print("<token_integer,"+cadena+","+str(i+1)+","+str(k+1)+">")
    elif(tipo == "comentario"):
        return("")
    elif(tipo == "incompleta"):
        print("Error lexico(linea:"+str(i+1)+",posicion:"+str(k+1)+")")
    elif(tipo == "completa"):
        print("<token_string,"+ cadena[1:-1] +","+str(i+1)+","+str(k+1)+">")
    elif(tipo == 0):
        print("Error lexico(linea:"+str(i+1)+",posicion:"+str(k+1)+")")

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

#T = (sys.stdin.readline())
Entrada= open("archivo.txt", "r")
lines = Entrada.readlines()
for i in range(0, len(lines)):
    checkLine(lines[i],i)




Entrada.close()

#me voy adormir perri perri perrito
