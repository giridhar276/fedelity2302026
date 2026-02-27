


import threading 
import time 



def say_hello():
    for i in range(3):
        print("Hello from thread A")
        time.sleep(0.5)   

def prime_numbers():
    for i in range(1,6):
        print("Hello from thread B")
        time.sleep(0.3)  

t1 = threading.Thread(target=say_hello)
t2 = threading.Thread(target=prime_numbers)

t1.start()
t2.start()


t1.join()
t2.join()   

print("Done")