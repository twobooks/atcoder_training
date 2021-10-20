from datetime import datetime
import time
import threading

def shoriA(num):
    while True:
        time.sleep(1)
        print(datetime.now() , f"shori A - {num}")
        num = num + 1

def shoriB(x):
    print(datetime.now())
    print("shoriB",x)
    return x + 10

def shoriC(x):
    print(datetime.now())
    print("shoriC",x)
    return x * 10

def shoriD(x):
    print(datetime.now())
    print("shoriD" , x)
    x = x ** 2
    print(f"shori owari x = {x}")
    return 

def betsuNoShori(x):
    x = shoriB(x)
    x = shoriC(x)
    x = shoriD(x)

sc1 = threading.Thread(target=shoriA, args=(0,))
sc2 = threading.Thread(target=betsuNoShori, args=(2,))

threadList = [sc1, sc2]
for sc in threadList:
    sc.start()
    time.sleep(5)