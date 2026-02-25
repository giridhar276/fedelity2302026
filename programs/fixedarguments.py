# fixed argumenets
def display(a,b):
    print(a,b)
display(10,20)

# default arguments 
def display(a = 0,b = 0,c = 0):
    print(a,b,c)
display() # 0 0 0 
display(10) # 10 0 0 
display(10,20) # 10 20 0
display(10,20,30) # 10 20 30

# keyword arguments
def display(c,a,b):
    print(a,b,c)
display(b = 20, a= 10, c = 30)

#variable length arguments
# *args is treated as tuple, ** kwargs is treated as dictionary
def display(*args):
    print(args)
display(10,20,30,40,56,34,56,34,67,367,32,6,43,67,3,6,723,56,43,67,54,3,67,4)

def displayinfo(**kwargs):
    print(kwargs)
displayinfo(chap1 = 10 , chap2 = 20)



# requirement: connect to database and fetch all the rows and write to csv file and validate

def connect_db:
    ###
def query:
    ###
def read_records:
    ###
def write_to_csv:
    ##
def validate():
    ###