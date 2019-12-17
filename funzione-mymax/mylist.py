from timeit import time
from random import randrange


def mymax (list):
    nm = list[0]
    for n in list:    
        if nm < n:
            nm = n
    return nm


mylist = [randrange(1000) for _ in range(100000)]

sorted_list = []


start_time = time.time()
for idx in range(len(mylist)):
    nm = mymax(mylist)
    sorted_list.append(nm)
    mylist.remove(nm)
stop_time = time.time()
print(f"{(stop_time-start_time):.9f}")





#print(sorted_list)

# assert sorted_list[0] == 124
# assert sorted_list[1] == 656
# assert sorted_list[2] == 2
# assert sorted_list[3] == 45  
# assert sorted_list[4] == 11
# assert sorted_list[5] == 542