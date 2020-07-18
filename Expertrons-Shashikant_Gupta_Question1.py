#importing Regular Expresions libary for validation purpose
import re
n=input("Enter number:")
#The number taken from 0 to 9
#[7-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9] or [7-9][0-9]{9} or [7-9]\d{9}
m=re.fullmatch("[7-9]\d{9}",n)
if m!= None:
    print("Valid")
else:
    print("Not valid") 
