def move(n, src, tmp, dst):
    if n == 1:
        print('{} --> {}'.format(src, dst))
    else:
        move(n-1, src, dst, tmp)
        print('{} --> {}'.format(src, dst))
        move(n-1, tmp, src, dst)

n = int(input('please input a number for n: '))
move(n, 'a', 'b', 'c')
