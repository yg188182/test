	*args和**kwds作为形参时：

	*args作为形参时，作为一个元组匹配没有指定参数名的参数。而**kwds作为字典，匹配指定了参数名的参数。
	def myfunc(a,*args,**kwds):
	    print 'a:',a
	    for i in args:
	        print i
	    for i,j in kwds.iteritems():
	        print i,j
	>>>myfunc(1,2,3,a=1,b=2)
	'a:'1
	2
	3
	a 1
	b 2



	*args和**kwds作为实参时,需要加*和**：
	>>>args=(1,2)
	>>>kwds={"c":5,"d":6}
	>>>myfunc(0,*args,**kwds)
	'a:'1
	1
	2
	c 5
	d 6
