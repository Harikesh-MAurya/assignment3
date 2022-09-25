# 1)............................
# l1=['Java','Python','SQl','c']
# print(l1)

# 2).........................
# print(type(l1))

# 3).......................
# print(l1[-1])

# 4).......................
# thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
# thislist[1]="NoSQL"
# thislist[3]="Flutter"
# print(thislist)

# 5).......................................
# l1.append("harikesh")
# print(l1)

# 6).....................................
# firstlist = ["Java", "Python", "SQL"]
# secondlist = ["C", "Cpp", "NoSQL"]
# # firstlist.append(secondlist)

# for i in secondlist:
#     firstlist.append(i)
# print(firstlist)
    
# 7)....................................

# thislist1 =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
# for i in range(0,len(thislist1)):
#     print(thislist1[i],end=" ")


# 8)........................................
# thislist1 =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
# print(sorted(thislist1))

# 9)........................................
# b=[]
# i=1
# n1=int(input("Enter n : "))
# while i<=n1:
#     a=input("Enter string : ")
#     b.append(a)
#     i+=1
# print(b)

# 10).........................................
num=int(input("Enter number : "))
b=[]
while num>0:
    r=num%10
    b.append(r)
    num//=10
print(b)