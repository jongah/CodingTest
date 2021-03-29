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