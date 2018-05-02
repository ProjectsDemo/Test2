def Hanoi(n,a,b,c):
    if(n==1):
        move(a,1,c)
    else:
        Hanoi(n-1,a,c,b)
        move(a,n,c)
        Hanoi(n-1,b,a,c)
def move(x,n,y):
    print("{} --> {}".format(n,x,y))
n=input("please input a number for n: ")
Hanoi(int(n),'a','b','c')
