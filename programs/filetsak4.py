

try:
    with open("employee.csv") as fobj:
        with open("empbkp.csv","w") as fw:
            for line in fobj:
                line = line.replace("United-States","US")
                fw.write(line)
except Exception as err:
    print(err)

    