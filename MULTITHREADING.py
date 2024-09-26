#MULTITHREADING

import time
import threading

def calc_sqr(num):
    print("Calculating the square of nummbers")
    for n in num:
        time.sleep(0.2)
        print('Square:',n*n)

def calc_cub(num):
    print("Calculating the square of nummbers")
    for n in num:
        time.sleep(0.2)
        print('Cube:',n*n*n)

arr=[1,2,5,7]

t=time.time()
t1=threading.Thread(target=calc_sqr,args = (arr,))
t2=threading.Thread(target=calc_cub,args = (arr,))

t1.start()
t2.start()

t1.join()
t2.join()


print("I'm done in ",time.time()-t)
