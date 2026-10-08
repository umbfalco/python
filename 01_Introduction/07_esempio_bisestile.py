#Un anno `e bisestile se `e divisibile per 4 ma non per 100,
# o se è divisibile per 400

anno=int(input("Inserisci anno:"))
isBisestile= False
if (anno % 4 == 0 and anno % 100 != 0) or anno % 400 ==0:
    isBisestile=True

print(isBisestile)