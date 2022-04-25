def prim's(points)
       def minkey(mst,key):
            ma=sys.maxsize
            ind=-1
            for i,j in enumerate(key):
                if j<ma and mst[i]!=True:
                    ma=j
                    ind=i
            return ind
        
        di=[[0]*len(points) for i in range(len(points))]
        for i in range(len(di)):
            for j in range(len(di)):
                if i!=j:
                    di[i][j]=abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        mst=[False]*len(points)
        key=[sys.maxsize]*len(points)
        parents=[None]*len(points)
        key[0]=0
        parents[0]=-1
        for i in range(len(points)):
            x=minkey(mst,key)
            mst[x]=True
            for i in range(len(di[x])):
                if di[x][i]>0 and key[i]>di[x][i] and mst[i]==False:
                    key[i]=di[x][i]
                    parents[i]=x
        return sum(key)
            
