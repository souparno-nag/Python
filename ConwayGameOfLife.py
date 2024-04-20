# CONWAY GAME OF LIFE
n=30
grid=[[0 for x in range(n)] for y in range(n)]

def checklife(L,p):
  if p[0]==0 and p[1]==0:
    livecell=L[0][1]+L[1][0]+L[1][1]
  elif p[0]==0 and p[1]==(n-1):
    livecell=L[0][n-2]+L[1][n-2]+L[1][n-1]
  elif p[0]==n-1 and p[1]==0:
    livecell=L[n-2][0]+L[n-2][1]+L[n-1][1]
  elif p[0]==n-1 and p[1]==n-1:
    livecell=L[n-2][n-1]+L[n-2][n-2]+L[n-1][n-2]
  elif p[0]==0:
    livecell=L[0][p[1]-1]+L[0][p[1]+1]+L[1][p[1]-1]+L[1][p[1]]+L[1][p[1]+1]
  elif p[0]==(n-1):
    livecell=L[n-1][p[1]-1]+L[n-1][p[1]+1]+L[n-2][p[1]-1]+L[n-2][p[1]]+L[n-2][p[1]+1]
  elif p[1]==0:
    livecell=L[p[0]-1][0]+L[p[0]+1][0]+L[p[0]-1][1]+L[p[0]+1][1]+L[p[0]][1]
  elif p[1]==(n-1):
    livecell=L[p[0]-1][n-1]+L[p[0]+1][n-1]+L[p[0]-1][n-2]+L[p[0]+1][n-2]+L[p[0]][n-2]
  else:
    livecell=L[p[0]-1][p[1]-1]+L[p[0]-1][p[1]]+L[p[0]-1][p[1]+1]+L[p[0]][p[1]-1]+L[p[0]][p[1]+1]+L[p[0]+1][p[1]-1]+L[p[0]+1][p[1]]+L[p[0]+1][p[1]]
  if livecell<2 or livecell>3:
    return 0
  elif livecell==3:
    return 1
  elif L[p[0]][p[1]]==0 and livecell==2:
    return 0
  elif L[p[0]][p[1]]==1 and livecell==2:
    return 1

  if livecell<2 or livecell>3:
    return 0
  elif livecell==3:
    return 1
  elif L[p[0]][p[1]]==0 and livecell==2:
    return 0
  elif L[p[0]][p[1]]==1 and livecell==2:
    return 1

Ngrid=[[0 for x in range(n)] for y in range(n)]
def addoscillator(L,p):
  L[p[0]][p[1]]=1
  L[p[0]-1][p[1]]=1
  L[p[0]+1][p[1]]=1
def addglider(L,p):
  L[p[0]][p[1]]=1
  L[p[0]+1][p[1]+1]=1
  L[p[0]+2][p[1]-1]=1
  L[p[0]+2][p[1]]=1
  L[p[0]+2][p[1]+1]=1
def addsquare(L,p):
  L[p[0]][p[1]]=1
  L[p[0]][p[1]+1]=1
  L[p[0]+1][p[1]]=1
addoscillator(grid,[1,1])
addsquare(grid,[1,16])
addglider(grid,[5,5])
addglider(grid,[5,10])
print(checklife(grid,[8,5]))
print(checklife(grid,[5,6]))
for i in grid:
  print(i)
print()
count=5
while count>0:
  for i in range(n):
    for j in range(n):
      Ngrid[i][j]=checklife(grid,[i,j])
  for i in Ngrid:
    print(i)
  print()
  count-=1
  grid=Ngrid.copy()
