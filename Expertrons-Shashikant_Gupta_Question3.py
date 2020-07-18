students = [[37.21,"Harry"], [ 37.21,"Berry"], [ 37.2,"Tina"], [41,"Akriti"],[39,"Harsh"]]
students.sort(reverse=True)
print (students)
score_list = []

for sublist in students:
    score_list.append(sublist[0])

a=0
for x in range (len(score_list)-2,-1,-1):
    if min(score_list) != score_list[x]:
        a = score_list[x]
        break

empty_list = [] 
for i in students: 
    if i[0] == a: 
        empty_list.append(i[1])
        
empty_list.sort()      


for x in empty_list:
    print(x)