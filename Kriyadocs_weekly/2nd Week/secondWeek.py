#The lists and strings are named after the Question Numbers.

l1 = [int(input()) for _ in range(5)]
print(sum(l1))

l2 = [input() for _ in range(3)]
longest = l2[0]
for i in l2:
    if len(i) > len(longest):
        longest = i
print(longest)

l3 = [int(input()) for _ in range(5)]
l3a = []
for i in l3:
    if i%2==0:
        l3a.append(i)
print(l3a)

l4 = [input() for _ in range(3)]
l4a = []
for i in l4:
    if i[0] == 'a':
        l4a.append(i)
print(l4a)

l5 = [[1,2,3],[2,5,4],[3,5,6]]
l5a = []
for i in l5:
    l5a.append(sum(i))
print(l5a)

l7 = [[1,2,3],['a','b','c'],[3,5,6]]
l7a = []
for i in l7:
    for j in i:
        l7a.append(j)
print(l7a)

l8 =[[1,2,3],['a','b','c'],[3,5,6]]

l8a = "\n".join(" ".join(str(i) for i in one) for one in l8)
print(l8a)





