#La formula del quadrato costruito sull'ipotenusa
# in un triangolo rettangolo è uguale alla somma dei quadrati
# costruiti sui due cateti (\(c^2 = a^2 + b^2\))
# Spiegazione delle Formule
#Se indichiamo con:
# (c) l'ipotenusa (il lato opposto all'angolo retto)
# (a) e (b) i due cateti
# Area del quadrato sull'ipotenusa: (c^2 = a^2 + b^2)
# Lunghezza dell'ipotenusa: (c = sqrt{a^2 + b^2})
import math

a=float(input("Inserisci il cateto a:"))
b=float(input("Inserisci il cateto b:"))
c=math.sqrt(a**2+b**2)
print(f"Il valore dell'ipotenusa è {c}")
