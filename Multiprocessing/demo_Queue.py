import multiprocessing as mp

def job(q):
    '多线程不能有return 需要使用到Queue'
    res = 0
    for i in range(10):
        res += i +i**2 + i**3
    q.put(res) #queue


if __name__ == "__main__":
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1,res2)