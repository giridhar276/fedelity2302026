
### object oriented
import csv
class FileOperations:
    def __init__(self,filename):
        self.filename = filename
    def displayLines(self):
        with open(self.filename,"r") as self.fobj:
            self.reader = csv.reader(self.fobj)
            for line in self.reader:
                print(line)

if __name__ == "__main__":
    file1 = FileOperations("employee.csv")
    file1.displayLines()




# procedural
import csv
with open("employees.txt","r") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)