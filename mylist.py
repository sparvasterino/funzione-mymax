def mymax (list):
    nm = list[0]
    for n in list:    
        if nm > n:
            nm = n
    return nm


mylist = [124,656,2,45,11,542]

sorted_list = []


for idx in range(len(mylist)):
    nm = mymax(mylist)
    sorted_list.append(nm)
    mylist.remove(nm)

print(sorted_list)





assert sorted_list[0] == 124
assert sorted_list[1] == 656
assert sorted_list[2] == 2
assert sorted_list[3] == 45  
assert sorted_list[4] == 11
assert sorted_list[5] == 542