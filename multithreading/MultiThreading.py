import time
import threading

def cal_powOf2(ele):
    for x in ele:
        time.sleep(0.2)
        print(f'2 pow {x} :',2**x)


def cal_powOf3(ele):
    for x in ele:
        time.sleep(0.2)
        print(f'3 pow {x} :',3**x)



l = [2,3,4,5]

t = time.time()

t1 = threading.Thread(target=cal_powOf2,args=(l,))
t2 = threading.Thread(target=cal_powOf3,args=(l,))
t1.start()
t2.start()

t1.join()  # this wait for the thread to execut then it will execute next print statement
t2.join()  # else next instruction is executed without completion of thread execution  

print("time consumed = ",time.time()-t)