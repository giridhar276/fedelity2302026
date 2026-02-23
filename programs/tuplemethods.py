
####### difference between list and tuple
alist = [10,20,30]
alist[0] = 100
print(alist)

""" this is not executable
atup = (10,20,30)
atup[0] = 100
print(atup)
"""


atup = (10,20,30)
alist = list(atup)  # converting to list
alist.append(40)    # makgin changes
atup = tuple(alist) # reconverting back to tuple
print(atup)