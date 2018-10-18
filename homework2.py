######判断1000000以内的质数的个数######

#判断a是否为质数
#对质数判断方法改进，对每个数只需判断到a的平方根（取整）
def judge(a):
	b=2
	amin=int(a**0.5)	#如果是质数，a的平方根之前一定能判断出
	while b<=amin:
		if a%b==0:
			return False	#如果不是质数，返回False
		b=b+1
	if b>amin:
		return True		#如果是指数，返回True
		
if __name__=='__main__':
	n=0
	for i in range(2,1000001):	#对2到1000000的数逐一判断
		if judge(i):
			n=n+1	#如果是质数，质数的个数n增加1
	print(n)