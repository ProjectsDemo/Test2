def func(s):
	if len(s)<1:
		return s
	else:
		return func(s[1:])+s[0]

	    
s=input("s:")
print("反转字符串为：{:s}".format(func(s)))
