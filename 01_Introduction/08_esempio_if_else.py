#1 if condizione_logica:
#2      istruzione1  istruzioni 1 e 2 vengono eseguite
#3      istruzione2  se la condizione `e vera
#4 else:
#5      istruzione3  istruzioni 3 e 4 vengono eseguite
#6      istruzione4  se la condizione `e falsa
#7 istruzione5  istruzioni 5 e 6 vengono eseguite in ogni caso
#8 istruzione6

#L’indentazione del codice `e fondamentale in Python: identifica i
# blocchi di istruzioni da eseguire nei vari casi

a=int(input("Inserisci un numero:"))
if(a>0):
    print("Il numero è positivo")
else:
    print("Il numero è negativo")