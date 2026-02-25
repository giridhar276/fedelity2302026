
# regular way / traditional way
############# file write operation
fobj = open("languages.txt","w")
print(fobj)
fobj.write("pythonprogramming\n")
fobj.write("unix\n")
fobj.writelines(["unix","java","genai\n"])
for value in range(1,10):
    fobj.write(str(value) + "\n")
fobj.close()


# pythonic way
#  context manager: if any line beings using 'with' keyword it is called context manager
# Advantage: file is closed automatically 

with open("languages.txt","a") as fobj:
    print("file status:",fobj.closed)
    fobj.write("oracle\n")
    fobj.writelines(["java","genai\n"])

print("file status:",fobj.closed)


