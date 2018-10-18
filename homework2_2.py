class c():
	def insertSort(self,a):
		for i in range(1, len(a)):	#从下标为1的元素遍历到最后一个元素
			t=a[i]	#t为当前要插入的元素
			j=i-1	#j为已排好序的最后一个元素的下标
			while t<a[j] and j>=0:	#从后往前遍历已排好序的元素，如果已排好序的元素大于待排序的元素，则将已排好序的元素向后移一位
				a[j+1]=a[j]
				j=j-1	#遍历前面一个元素
			a[j+1]=t	#最后将带待排序的元素插入


a = c()
s=[5,5,4,89,7,8,55,468,7,56]
a.insertSort(s)
print(s)