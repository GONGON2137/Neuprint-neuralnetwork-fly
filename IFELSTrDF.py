from asyncio import wait
import time, random
a=0
czas= 1
przegrana= random.randrange(1,2000)
while a < 1000:
    czas= czas*2
    a= a+1
    if a == 1000:
        print("wygrywasz!")
    elif a == 69:
        print("nice")
        print("wynik to:" + str(a))
        time.sleep(czas)
    else:
        if a == przegrana:
            print("przegrywasz")
            1/0
        else:
            print("wynik to:"+str(a))
            time.sleep(czas)
