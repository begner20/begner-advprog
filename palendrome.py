
def pal(x):
    if x = x[::-1]:
        return True
    else:
        return False

def main():
    palMAX=0
    for i in range (100,1000):
        for j in range (100,1000):
            x=i*j
            pal(x)
            if i>palMAX:
                palMAX=i
    print palMAX

main()


def paltest(x):
    if x = x[::-1]:
        return True
    else:
        return False
