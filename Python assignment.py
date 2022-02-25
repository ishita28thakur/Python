#Q2
# 5**9 = 1953125
# 3//2 = 1
# 7//3 = 2
# 7/3 = 2.3333333333333335
# 6 == 6 = True
# a = 20; a+= 30; a%=3; print(a) = 2
# True * False = 0
# True & False = False
# True and False = False
# ((6>3) and (7<4) or (18==3)) and (9>3) = False
# True is False = False
# False in ‘False’ = error
# ((True == False) or (False > True)) and (False <= True) = False

#Q3
s1 = "Nice to have it"
s2 = "here"

add = s1 + " " + s2
print("quetion 3 Added string : ", add)

#Q4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
index1 = a[3]
index2 = index1[1]
index3 = index2[2]
final_index = index3[0]
print("quetion 4 Index of HELLO: ", final_index)

#Q5
a.append(s1)
a.append(s2)
a.insert(0,s2)
a.insert(0,s1)
print("question 5 New list: ", a)

#Q6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]

for i in numbers:
    if i % 2 == 0:
        print("question 6 Number: ", i)
    if i == 237:
        break
    
#Q7
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("question 7 the final color list: ", color_list_1.difference(color_list_2))

#Q8
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
  
    return True
      
string = str(input("enter a string: "))
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")

#Q9
n = input(" type a number: ")
print ("final value: ", int(n) + int(n*2) + int(n*3))

#Q10
inp = input("enter the input: ")
raw = inp.split("#")
for i in range(len(raw)):
    raw[i]=raw[i].split(" ")
rx = raw[0]
ry = raw[1]
x = []
y = []
for i in rx:
    x.append(int(i))
for i in ry:
    y.append(int(i))
print("x = ",x)
print("y = ",y)

#Q11
words = input("enter words sperated with commas: ")
words_list = words.split(",")
words_list.sort()
listToStr = ','.join(words_list)
print("question 11 final answer: ",listToStr)

#Q12
d = {'Student': ['Rahul', 'Kishore', 'Vidhya','Raakhi'],'Marks': [57,87,67,79]}
students = d['Student']
marks = d['Marks']
maxm = max(marks)
i = marks.index(maxm)
print("question 12 output: ", students[i])

#Q13
str_num = input("input to question 13: ")
Letters = 0
digits = 0
for i in str_num:
    if i.isalpha() == True:
        Letters += 1
    if i.isdigit() == True:
        digits += 1
print("question 13 number of letters: ", Letters)
print("question 13 number of digits: ", digits)

#Q14
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
name1 = d['Name']
sub1 = d['Subject']
ratings1 = d['Ratings']
inp = input("input to question 14: ")
x = []
y = []
z = []
count = sub1.count(inp)
for i in range(count):
    j = sub1.index(inp)
    x.append(name1[j])
    y.append(sub1[j])
    z.append(ratings1[j])
    del name1[j]
    del sub1[j]
    del ratings1[j]
newData = dict()
newData['Name'] = x
newData['Subject'] = y
newData['Ratings'] = z
print(newData)

#Q15
n = int(input("enter an integer: "))
divBy7 = [i for i in range(0, n) if (i % 7 == 0)]
print(divBy7)

def divChecker(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i, value)

divChecker(n)

#Q16
import math

x, y = 0, 0

while True:
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")
        

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)

print("Distance:", c)

