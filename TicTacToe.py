# TIC TAC TOE
grid=[['_']*3 for i in range(3)]
c=0
n=9
def checkwin(L,elem):
  for i in range(3):
    if L[i][0]==L[i][1]==L[i][2]==elem:
      return True
      break
  for i in range(3):
    if L[0][i]==L[1][i]==L[2][i]==elem:
      return True
      break
  if L[0][0]==L[1][1]==L[2][2]==elem or L[0][2]==L[1][1]==L[2][0]==elem:
    return True
while n>0:
  print(grid)
  print('Enter position of X in the form : row column')
  A=list(map(int,input().split()))
  grid[A[0]-1][A[1]-1]='X'
  if checkwin(grid,'X'):
    print(grid)
    print('X won')
    c=1
    break
  print('Enter position of O in the form : row column')
  B=list(map(int,input().split()))
  grid[B[0]-1][B[1]-1]='O'
  if checkwin(grid,'O'):
    print(grid)
    print('O won')
    c=1
    break
  n-=1
if c==0:
  print('It is a draw')
