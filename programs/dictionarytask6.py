
#Write a program to list customers to increment balance with 1000.


customers = {
    "C001": {"name": "Alice", "balance": 5000},
    "C002": {"name": "Bob", "balance": 12000},
    "C003": {"name": "Charlie", "balance": 3000}
}


for key,value in customers.items():
    customers[key]['balance']+=1000
print(customers)



## hardcoded code
customers['C001']['balance']+=1000
customers['C002']['balance']+=1000
customers['C003']['balance']+=1000
print(customers)