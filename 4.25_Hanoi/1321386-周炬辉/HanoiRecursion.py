def hanoiRecursion(n,A,B,C):
    if(n==1):
        move(A,1,C)
    else:
        hanoiRecursion(n-1,A,C,B)
        move(A,n,C)
        hanoiRecursion(n-1,B,A,C)
def move(x,n,y):
    print("把编号为{0}盘从{1}移动到{2}".format(n,x,y))

n=input("请输入A塔上盘子的个数")
hanoiRecursion(int(n),'A','B','C')
    
