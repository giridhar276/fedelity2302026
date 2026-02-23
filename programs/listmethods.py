alist =[40,34,56,23,56,25,3,83]
#slicing
print(alist[0:5])
print(alist[::-1])

#methods
alist.append(100)   # adding single object ot the list
print("AFter appneding:",alist)
#list.extend(list)
alist.extend([45,17,34,83]) # adding multiple values to the list
print("After extending:",alist)
#list.insert(index,value)
alist.insert(1,200)
print("After inserting :",alist)
#list.pop(index)
alist.pop(0) # list.pop(index)
print("After pop operation:",alist)

#alist.remove(1000)
if 100 in alist:    
    alist.remove(100)
else:
    print("100 is not the part of list")

alist.reverse()
print("reversing the list :",alist)
alist.sort()
print("ascending order:", alist)
alist.sort(reverse=True)
print("descending order:",alist)


alist = [10,120,20,30,100,40,50]
if 100 in alist:
    getindex = alist.index(100)
    alist.insert(getindex+1,200)
    print(alist)