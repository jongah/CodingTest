def Q1Test_1(money):
  coin = 0
  if money >= 500: 
    n = money // 500
    coin += n
    money -= n * 500

  if money >= 100: 
    n = money // 100
    coin += n
    money -= n * 100

  if money >= 50: 
    n = money // 50
    coin += n
    money -= n * 50

  if money >= 10: 
    n = money // 10
    coin += n
    money -= n * 10
  print(coin)

def Q1Test_2(m) : 
  coin = 0
  #m을 10으로 나눈다 -> 리버스한다 ->
  m = list(map(int,str(m//10)[::-1]))
  for i in m :
    if i >= 5 : 
      coin += 1
      i -= 5
    coin += i
  print(coin)

def Q1answer(m):
  count = 0
  arr = [500, 100, 50, 10]
  for coin in arr:
    count += m // coin
    m %= coin
  print(count)

Q1Test_1(1260)
Q1Test_2(1260)
Q1answer(1260)

def Q2Test_1(n, k):
  count = 0
  while n != 1:
    if n % k == 0:
      n //= k
      count += 1
    else :
      n -= 1
      count += 1
  print(n, count)

def Q2answer(n, k):
  count = 0
  while True:
    target = (n // k) * k
    count += (n - target)
    n = target
    print(n, count)
    if n < k :
      break
    count += 1
    n //= k
  print(count)


Q2Test_1(13, 4)
Q2answer(13, 4)

def Q3Test1(n):
  answer = int(n[0])
  for i in range(1, len(n)):
    i =int(n[i])
    answer = (answer * i) if i >= 2 else(answer + i)
  print(answer)

def Q3answer(n):
  answer = int(n[0])
  for i in range(1, len(n)):
    num = int(n[i])
    if num >= 2 :
      answer *= num
    else:
      answer += num
  print(answer)
  
Q3Test1('34019')
Q3answer('34019')

def Q3Test1(n):
  answer = int(n[0])
  for i in range(1, len(n)):
    i =int(n[i])
    answer = (answer * i) if i >= 2 else(answer + i)
  print(answer)

def Q3answer(n):
  answer = int(n[0])
  for i in range(1, len(n)):
    num = int(n[i])
    if num >= 2 :
      answer *= num
    else:
      answer += num
  print(answer)
  
Q3Test1('34019')
Q3answer('34019')

def Q4answer(n, data):
  data.sort()
  result = 0
  count = 0

  for i in data:
    count += 1
    if count >= i:
      result += 1
      count = 0
  print(result)