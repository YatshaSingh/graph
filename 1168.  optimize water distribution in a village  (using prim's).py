def supplyWater( wells, pipes):
	def minkey(key,mst):
		ma=1000000000
		ind=-1
		for i in range(len(key)):
			if ma>key[i] and mst[i]==False:
				ma=key[i]
				ind=i
		return ind
	n=len(wells)+1
	dp=[[-1]*n for i in range(n)]
	for i in range(len(wells)):
		dp[0][i+1]=wells[i]
		dp[i+1][0]=wells[i]
	for i,j,x in pipes:
		dp[i][j]=x
		dp[j][i]=x
	parent=[None]*n
	key=[100000000000000]*n
	mst=[False]*n
	parent[0]=-1
	key[0]=0
	for i in range(n):
		x=minkey(key,mst)
		mst[x]=True
		for j in range(len(dp[x])):
			if dp[x][j]>-1 and mst[j]==False and key[j]>dp[x][j]:
				key[j]=dp[x][j]
				parent[j]=x
	print(key)
	return sum(key)
wells=[1,0,2]
pipes=[ [1, 2, 1], [2 , 3, 3]]
print(supplyWater(wells, pipes))

 
