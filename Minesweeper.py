# MINESWEEPER
import random
m = 4      #no. of rows
n = 5    #no. of columns
maze = [[[]]*n for i in range(m)]
for i in range(m):
    print(maze[i])
bomb = []
while len(bomb)<5:
    a = random.randint(0, m - 1)  # row
    b = random.randint(0, n - 1)  # column
    if [a,b] not in bomb:
        bomb.append([a, b])
selected_units = []
print(bomb)
all_units = [[i,j] for i in range(m) for j in range(n)]
desirable_units = [[i,j] for i in range(0,m) for j in range(0,n)]
for i in bomb:
    desirable_units.remove(i)
print(desirable_units)
while True:
  print('Enter row,column: ')
  (xr,xc)=tuple(map(int,input().split(',')))

  if [xr,xc] in bomb:
      for i in bomb:
          print(i)
          maze[i[0]][i[1]] = '[B]'
      for i in range(0, m):
          print(maze[i])
      print('You lose!')
      break
  else:
      selected_units.append([xr, xc])
      print(selected_units)
      count = 0
      if [xr-1,xc-1] in bomb:
          count +=1
      elif [xr+1,xc+1] in bomb:
          count +=1
      elif [xr-1,xc+1] in bomb:
          count +=1
      elif [xr+1,xc-1] in bomb:
          count +=1
      elif [xr,xc-1] in bomb:
          count +=1
      elif [xr,xc+1] in bomb:
          count +=1
      elif [xr-1,xc] in bomb:
          count +=1
      elif [xr+1,xc] in bomb:
          count +=1
      else:
          count = count
      maze[xr][xc] = f'[{count}]'
  for i in range(0, m):
           print(maze[i])
  won = False
  tally = []
  for i in desirable_units:
      if i in selected_units:
          won = True
          tally.append(won)
      else:
          won = False
          tally.append(won)
  if all(tally) == True:
      print('You won!')
      break
  else:
      pass
