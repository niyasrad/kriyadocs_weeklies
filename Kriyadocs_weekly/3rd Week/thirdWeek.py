import re

l1 = ["hello", "bello", "hello"]
d = {i:l1.count(i) for i in l1}
print(d)

l2 = ["omni", "sigma", "idontevenknow"]
c = {i:len(i) for i in l2}
print(c)


def vowelcount(string):
    count = 0
    for i in string:
        if i in ['a','e','i','o','u', 'A','E','I','O','U']:
            count = count + 1;
    return count

l3 = ["aeiou", "what", "How"]
v = {i:vowelcount(i) for i in l3}

print(v)


l4 = ["!!!aeiou", "wha...t", "How3,.!."]
v = {re.sub(r'[^a-z\d ]','',i.lower()):vowelcount(i) for i in l4}
print(v)



#5. bigrams
s = "Hello my name is rad and welcome back to a new episode on how to make your videos better. I am a student in SVCE."
a = re.sub(r'[^a-zA-Z\d]'," ",s ).split()
b = list(zip(a, a[2:]))
c = {' '.join(i):b.count(i) for i in set(b)} 

#5. trigrams
a = re.sub(r'[^a-zA-Z\d]'," ",s ).split()
b = list(zip(a, a[1:], a[2:]))
c = {' '.join(i):b.count(i) for i in set(b)} 

#6. ngrams function
def ngrams(n, string):
    a = re.sub(r'[^a-zA-Z\d]'," ",string ).split()
    b = list(zip(*[a[i:] for i in range(n)]))
    c = {' '.join(i):b.count(i) for i in set(b)} 
    return c


#7. comparing two files to find the common words of bi, trigrams
f = open("ngrams1.txt")
a = f.read()
f1 = open("ngrams2.txt")
b = f1.read()
c = ngrams(2, a)
d = ngrams(2, b)
res = [ele for ele in c if ele in d]
print(res)
e = ngrams(3, a)
f = ngrams(3, b)
res = [ele for ele in e if ele in f]
print(res)
