import multiprocessing
import time

def cal_sqr(var):
    for x in var:
        time.sleep(3)
        print(f'the square of {x} is {x*x}')

def cal_cub(var):
    for x in var:
        time.sleep(1)
        print(f'the cube of {x} is {x*x*x}')


if __name__ == '__main__':
    l = [2,3,4,5,6,7]
    t1 = multiprocessing.Process(target=cal_cub,args=(l,)) #this will create seprate process

    t2 = multiprocessing.Process(target=cal_sqr,args=(l,)) #this will create seprate process

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("done")

