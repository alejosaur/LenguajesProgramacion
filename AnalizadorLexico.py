import re
import sys

entero = re.compile('^[0-9]+$')
flotante = re.compile('^[0-9]+.[0-9]+$')
identificador = re.compile('^(([a-z,A-Z])+[0-9]*)+$')
tokensreservados1 = re.compile('^({|}|#|\[|\]|\(|\)|>|<|!|\+|-|\*|/|%|\^|=)+$')
tokensreservados2 = re.compile('^(>=|<=|==|!=|in|&&|\|\|)+$')
tokensLargos = re.compile('^(true|false|funcion|retorno|log|end|for|while|if)+$')
espacios = re.compile('^(\ +|\n+|\t)+')

diccionarioTokens={'{':'token_llave_izq','}':'token_llave_der','#':'token_com','[':'token_cor_izq',']':'token-cor-der','(':'token_par_izq',')':'token_par_der','>':'token_mayor','<':'token_menor','.':'token_point','!':'token_not','+':'token_mas','-':'token_menos','*':'token_mul','/':'token_div','%':'token_mod','^':'token_pot','=':'token_assign','>=':'token_mayor_igual','<=':'token_menor_igual','==':'token_igual_num','!=':'token_diff_num','in':'token_in','&&':'token_and','||':'token_or'}

def checkLine(T,i):
    inicio=0
    last = 0
    k=0
    while(k < len(T)):
        encontrado = checkRegex(T[inicio:k],i)
        if(k==len(T)-1 and encontrado != 0):
            print(encontrado +" "+ T[inicio:k])
            k+=1
        elif(((encontrado==0 or encontrado == "espacios") and (last != 0 and last != "espacios"))):
            print(str(last) + T[inicio:k-1])
            inicio = k-1
        elif(encontrado=="espacios"):
            inicio = k
        else:
            k += 1
        last=encontrado




def checkRegex(T,i):
    if(re.search(tokensreservados1,T)):
        m = re.search(tokensreservados1,T)
        #return("<"+diccionarioTokens[''+T[m.start():m.end()]+'']+","+str(i+1)+","+str(m.span()[0]+1)+">")
        return("t1")
    elif(re.search(tokensreservados2,T)):
        m = re.search(tokensreservados2,T)
        #return("<"+diccionarioTokens[''+T[m.start():m.end()]+'']+","+str(i+1)+","+str(m.span()[0]+1)+">")
        return("t2")
    elif(re.search(tokensLargos,T)):
        m = re.search(tokensLargos,T)
        #return("<"+T[m.start():m.end()]+","+str(i+1)+","+str(m.span()[0]+1)+">")
        return("tl")
    elif(re.search(identificador,T)):
        m = re.search(identificador,T)
        #return("<id,"+T[m.start():m.end()]+","+str(i+1)+","+str(m.span()[0]+1)+">")
        return("identificador")
    elif(re.search(flotante,T)):
        m = re.search(flotante,T)
        #return("<token_float,"+T[m.start():m.end()]+","+str(i+1)+","+str(m.span()[0]+1)+">")
        return("flotante")
    elif(re.search(entero,T)):
        m = re.search(entero,T)
        #return("<token_integer,"+T[m.start():m.end()]+","+str(i+1)+","+str(m.span()[0]+1)+">")
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
