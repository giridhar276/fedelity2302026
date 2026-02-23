book  = {"chap1":10 ,"chap2":20 ,"chap3":30 }


#print(book["chap4"])
print(book.get("chap4")) # if key exists.. it returns value
                         # if key is not found...it returns None

# display dictionary
print(book)
# add new key-value pairs
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60
print(book)
# display individual values
print(book["chap1"]) #10
print(book["chap2"]) #20

## methods
# display all the keys
print( book.keys())

# display all the values
print(book.values())

# display key-value pairs
print(book.items())


book.pop("chap1") # chap1-10 will be removed from dictionary
print(book)
# will remove the last key-value pair
book.popitem()
book.popitem()
book.popitem()
print(book)

## combining 2 dictionaries
book  = {"chap1":10 ,"chap2":20 ,"chap3":30 }
newbook = {"chap4":40,"chap5":50}
#method1
book.update(newbook)
print(book)
# method2
finalbook = { **book, **newbook}
print(finalbook)