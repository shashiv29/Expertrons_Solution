#first user input
user1= str(input("first enter a list elements separated by comma ")).split(',')
user2= str(input("second enter a list elements separated by comma ")).split(',')
result=list(set(user1)^set(user2))

print(result)