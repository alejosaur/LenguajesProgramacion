import re
import sys

entero = re.compile('[1-9]+')
identificador = re.compile('(([a-z,A-Z])+[0-9]*)+')
tokensreservados1 = re.compile('({|}|#|\[|\]|\(|\)|>|<|\.|!|\+|-|\*|/|%|\^|=)+')
tokensreservados2 = re.compile('(>=|<=|==|!=|in|&&|\|\|)+')
tokensLargos = re.compile('(funcion|retorno|log|end|for|while|if|lozano)+')
espacios = re.compile('\ +|\n+|\t+')

diccionarioTokens={'{':'token_llave_izq','}':'token_llave_der','#':'token_com','[':'token_cor_izq',']':'token-cor-der','(':'token_par_izq',')':'token_par_der','>':'token_mayor','<':'token_menor','.':'token_point','!':'token_not','+':'token_mas','-':'token_menos','*':'token_mul','/':'token_div','%':'token_mod','^':'token_pot','=':'token_assign','>=':'token_mayor_igual','<=':'token_menor_igual','==':'token_igual_num','!=':'token_diff_num','in':'token_in','&&':'token_and','||':'token_or'}

def checkRegex(T,i):
    if(re.search(tokensreservados1,T)):
        m = re.search(tokensreservados1,T)
        print("<"+diccionarioTokens[''+T[m.start():m.end()]+'']+","+str(i+1)+","+str(m.span()[0]+1)+">")
    elif(re.search(tokensreservados2,T)):
        m = re.search(tokensreservados2,T)
        print("<"+diccionarioTokens[''+T[m.start():m.end()]+'']+","+str(i+1)+","+str(m.span()[0]+1)+">")
    elif(re.search(tokensLargos,T)):
        m = re.search(tokensLargos,T)
        print("<"+T[m.start():m.end()]+","+str(i+1)+","+str(m.span()[0]+1)+">")
    elif(re.search(identificador,T)):
        m = re.search(identificador,T)
        print("<id,"+T[m.start():m.end()]+","+str(i+1)+","+str(m.span()[0]+1)+">")
    elif(re.search(entero,T)):
        m = re.search(entero,T)
        print("<"+T[m.start():m.end()]+","+str(i+1)+","+str(m.span()[0]+1)+">")
    elif(re.search(espacios,T)):
        return
    else:
        print("ERROR MONDAFOCA")

#T = (sys.stdin.readline())
Entrada= open("archivo.txt", "r")
print(diccionarioTokens['in'])
lines = Entrada.readlines()
for i in range(0, len(lines)):
    checkRegex(lines[i],i)


Entrada.close()

#me voy adormir perri perri perrito
