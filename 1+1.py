from random import choice#随机选择用的

end = False#结束

def _try(a, b):
	"""
	a:自己的两个数 b:对方的两个数
	返回relist:所有可以成功的自己的两个数的列表
	当下一步返回的relist为空时有可能输
	当下一步返回的relist非空时有策略赢
	"""
	relist = []#返回非空时已经赢了

	"""
	递归出口(自己赢了):
	1、自己有一个数为10
	2、对方全爆
	"""
	if a[0] == 10 or a[1] == 10\
		or (a[0] == None and a[1] == None):
		return b

	if a[0] != None and a[0] > 10:#爆炸
		a[0] = None
	if a[1] != None and a[1] > 10:
		a[1] = None

	for i in range(2):
		if a[i] == None:
			continue#爆死了，跳过

		for j in range(2):
			if b[j] == None:
				continue

			l = a[:]#副本，不会影响a本身
			l[i] += b[j]#加选中对方的数

			if not _try(b, l):#对方的自己是对方，对方的对方是自己
				#如果返回的为空，即对方会输
				relist.append(l)#那么自己会赢，那么就把它加到“自己可以赢的”列表里吧

	return relist#返回

def player(a, b):#对于玩家的操作
	global end
	
	m = input("请输入自己和对方要加的位置：")#输入

	while True:#直到输入成功之前一直输入
		m = m.split(' ')#用空格分隔开成列表
		try:
			a[int(m[0]) - 1] += b[int(m[1]) - 1]#加选中对方的数
		except:#输入不成功 继续输入
			m = input("输入错误, 请再输入一遍:")
		else:#输入成功，退出循环
			break
	
	if a[0] == 10 or a[1] == 10:#玩家有一个是10，玩家赢了
		print("你赢了\n")
		end = True#退出
		return a

	if a[0] != None and a[0] > 10:#玩家爆炸
		a[0] = None
	if a[1] != None and a[1] > 10:
		a[1] = None
		
	if a[0] == None and a[1] == None:#玩家全爆，电脑赢了
		print("你输了\n")
		end = True
		return a

	return a#返回玩家的a

def computer(a, b):#对于电脑的操作
	global end

	print("电脑计算中...")
	relist = _try(b, a)#获取电脑计算可以赢的列表
	if relist:
		b = choice(relist)#随机选择一种
	
	if b[0] == 10 or b[1] == 10:#电脑有一个是10，电脑赢了
		print("你输了\n")
		end = True
		return b
	
	if not relist:#空的话，就随便加一下吧，自己理解即可
		#记得这个要不要放79行if语句后面，不然会报错
		ra, rb = choice(range(2)), choice(range(2))
		if a[ra] != None:
			if b[rb] != None:
				b[rb] += a[ra]
			else:
				b[1 - rb] += a[ra]
		else:
			if b[rb] != None:
				b[rb] += a[1 - ra]
			else:
				b[1 - rb] += a[1 - ra]
	
	if b[0] != None and b[0] > 10:#电脑爆炸
		b[0] = None
	if b[1] != None and b[1] > 10:
		b[1] = None
		
	if b[0] == None and b[1] == None:#电脑全爆，玩家赢了
		print("你赢了\n")
		end = True
		return b

	return b

def main():
	a = [1, 1]#初始化
	b = [1, 1]
	global end
	printlist(a, b)

	while True:#主循环
		a = player(a, b)
		#b = computer(a, b)#电脑操作一次
		if end:
			break
		printlist(a, b)#打印当前战况
		#a = player(a, b)#玩家操作一次
		#b = player(b, a)
		b = computer(a, b)
		#a = computer(b, a)
		if end:
			break
		printlist(a, b)

	printlist(a, b)

def strnum(num):
	"""返回一个元素的字符串"""
	if num != None:
		return str(num)
	else:
		return "爆"

def printlist(a, b):
	"""打印当前战况"""
	print("当前战况:\n{} {}\n{} {}\n".format(strnum(a[0]), strnum(a[1]), strnum(b[0]), strnum(b[1])))

if __name__ == '__main__':
	main()




