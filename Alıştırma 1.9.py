for n in range(1,1000):
    n=str(n)
    if len(n)==1 and int(n)<9:
        print(n,end=" ")
    elif len(n)==2 and (int(n[0])+int(n[1]))<9:
        print(n, end=" ")
    elif len(n)==3 and (int(n[0])+int(n[1])+int(n[2]))<9:
        print(n, end=" ")
    
    
