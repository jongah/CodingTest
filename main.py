def move(x, y):
  mx = [0, 1, 0, -1]
  my = [-1, 0, 1, 0]
  #2차원 배열 이므로 up이 -1 down이 +1
  #상 우 하 좌
  up = 0
  right = 1
  down = 2
  left = 3
  #위로 이동
  x += mx[up]
  y += my[up]
  print(x, y)

def Q1_test1():
  n = int(input())
  move = [x for x in input().split()]
  x = 1
  y = 1
  tx = 0
  ty = 0

  mx = [0, 1, 0, -1]
  my = [-1, 0, 1, 0]
  #2차원 배열 이므로 up이 -1 down이 +1
  up = 0
  right = 1
  down = 2
  left = 3
  
  for i in move:
    if i == 'R':
      tx = x + mx[right]
      ty = y + my[right]
    elif i == 'L':
      tx = x + mx[left]
      ty = y + my[left]
    elif i == 'U':
      tx = x + mx[up]
      ty = y + my[up]
    elif i == 'D':
      tx = x + mx[down]
      ty = y + my[down]
    if tx >= 1 and tx <= n and y >= 1 and y <= ty:
      x = tx
      y = ty
  print(y, x)
  #y가 세로 x가 가로이므로 바꿔서 출력


def Q1_answer():
  n = int(input())
  x, y = 1, 1
  plans = input().split
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  move_type = ['L', 'R', 'U', 'D']

  for plan in plans:
    for i in range(len(move_type)):
      if plan == move_type[i]:
        nx = x + dx[i]
        ny = y + dy[i]
      if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
      x, y = nx, ny
  print(x, y)

def Q1_test1_modify():
  n = int(input())
  move = [x for x in input().split()]
  x, y = 1, 1
  mx = [0, 1, 0, -1]
  my = [-1, 0, 1, 0]
  #2차원 배열 이므로 up이 -1 down이 +1
  up = 0
  right = 1
  down = 2
  left = 3
  
  for i in move:
    if i == 'R':
      tx = x + mx[right]
      ty = y + my[right]
    elif i == 'L':
      tx = x + mx[left]
      ty = y + my[left]
    elif i == 'U':
      tx = x + mx[up]
      ty = y + my[up]
    elif i == 'D':
      tx = x + mx[down]
      ty = y + my[down]
    if tx >= 1 and tx <= n and y >= 1 and y <= ty:
      x = tx
      y = ty
  print(y, x)
  #y가 세로 x가 가로이므로 바꿔서 출력

def Q2_test1():
  n = int(input())
  print(n)
  check = 10 + 3*5
  count = 0
  #앞자리가3인경우 10 + 뒷자리가 3인 경우 3*5
  for i in range(n):
    if i != 3 and i != 13 and i != 23:
      count += check * 60 + (check - 60) * check
    else:
      count += 60 *60
  print(count)
Q2_test1()