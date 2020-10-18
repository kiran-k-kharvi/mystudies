import time

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

cal_powOf2(l)
cal_powOf3(l)

print("time consumed = ",time.time()-t)