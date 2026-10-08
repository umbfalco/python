num1=int(input("Inserisci il primo numero:"))
num2=int(input("Inserisci il secondo numero:"))

if(num1>num2):
    temp=num2
    num2=num1
    num1=temp

print(f"I numeri orinati crescenti sono: {num1},{num2} ")