import random
def missing():
    l1 = []
    N = random.randint(5,50)
    num = random.randint(1,N)
    
    for i in range(1,N+1):
        if i!=num:
            l1.append(i)
    random.shuffle(l1)
    print(l1)
    s = 0
    m = l1[0]
    for e in l1:
        s = s + e
        if e>m:
            m=e
    total = int(m*(m+1)/2)
    if total==s:
        print("\nMissing number is: ",m+1)
    else:
        print("\nMissing number is: ",total-s)
    if m==N or m==N-1:
        print("\nVerified for N = ",N)
missing()