def create_grid(n):
    grid=[]
    for i in range(n):
        grid.append(['']*n)

    return grid


def is_safe(grid,i,j,n):
    a=i
    b=j
    if j in res:            #checking column
        return False

    while a>=0 and b>=0:   #checking left top diagonal
        if grid[a][b]:
            return False
        a-=1
        b-=1
    a=i
    b=j
    while a>=0 and b<n:     #checking right top diagonal
        if grid[a][b]:
           return False
        a-=1
        b+=1

    return True


def n_queen(grid,i,n):
    global res
    if len(res)==n:
        all_res.append(res)
        res_opp=[]
        for k in res:
            res_opp.append(n-k)
        all_res.append(res_opp)
        nex=res[0]+1
        if nex<=(n/2):
            res=[]
            res.append(nex)
            grid=create_grid(n)
            n_queen(grid,1,n)
        return True
    if i>=n:
        return
    for j in range(n):
        if is_safe(grid,i,j,n):
            grid[i][j]='Q'
            res.append(j)

            if n_queen(grid,i+1,n):
                return True

            grid[i][j]=''
            res.pop()


all_res=[]
res=[]
grid= create_grid(8)
n_queen(grid,0,8)
print(all_res)
    
