aset = {10,10,10,20,20,30,30}
aset.add(10)
aset.add(20)
aset.add(40)
print(aset)

bset ={ 30,30,40,40,40,50,50,40,60}
print(bset)

# union operation  A  U B
print(aset.union(bset))
# intersection 
print(aset.intersection(bset))
# difference  A - B
print(aset.difference(bset))

# condition
if 10 in aset:
    print("value exists")

# for loop
for value in aset:
    print(value)

print("before:",aset)
print("before:",bset)
aset.intersection_update(bset)
print("after:",aset)
print("after:",bset)

# symmetric difference: gives elements that are in aset or bset but not in both
aset = {10,20,30}
bset = {30,40,50}
print(aset.symmetric_difference(bset))


cset = {40,50,60}
dset = cset.copy()
print(dset)

cset.discard(40)
print("After discard:",cset)
cset.remove(50)
print(cset)