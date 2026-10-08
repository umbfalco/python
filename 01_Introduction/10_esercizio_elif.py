#elif sta per else if; permette di concatenare i controlli
voto=int(input("Inserisci il voto:"))

if(voto<18):
    print("Voto insufficiente")
elif (voto==18):
    print("Voto sufficiente")
elif (voto>18 and voto<25):
    print("Voto buono")
elif (voto>=25 and voto<28):
    print("Voto ottimo")
elif (voto >=28 and voto<=30):
    print("Complimenti!")
elif (voto>30):
    print("Numero non valido")