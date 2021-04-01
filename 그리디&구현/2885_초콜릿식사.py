def Chocolate():
  k = int(input())
  c = 0
  if k == 1:
    print(2, 1)
  else:
    for i in range(1, k):
      if 2**i >= k:
        c = 2**i
        break
    count = 0
    if c != k:
      n = c/(c - k)
      while n != 1:
        n //= 2
        count += 1
    print(c, count)
#k보다 큰 2의 x승 c 구하기 
#c / (c-k) = n 이때 n은 2의 count승 이다.
#c는 초콜릿의 개수 count는 쪼개는 최소 횟수 이다.