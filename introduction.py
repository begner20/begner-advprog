def main():
    x=3
    y=5
    numlist=[]
    sum=[]
    tot = 0
    for i in range (1000):
        numlist.append(i)
        if i % 3 == 0 or i % 5 ==0:
            sum.append(i)
    for i in sum:
        tot = tot + i
    print sum
    print tot
main()
