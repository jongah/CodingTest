def card(n, lever):
  print('ddddd')
  coin = 0
  while len(lever) != 1:
    print(len(lever))
    i = lever.index(max(lever))

    if i == len(lever):
      coin += lever[i] + lever[i - 1]
      lever[i - 1] = lever[i] + lever[i - 1]
    else:
      coin += lever[i] + lever[i - 1]
      lever[i - 1] = lever[i] + lever[i - 1]
    del(lever[i])
  print(coin)
  

card(3, [30, 30, 40])
print("coin")

n = int(input())
lever = list(map(int,input().split()))
coin = 0
while len(lever) != 1:
  i = lever.index(max(lever))
  if i == len(lever):
    coin += lever[i] + lever[i - 1]
    lever[i - 1] = lever[i] + lever[i - 1]
  else:
    coin += lever[i] + lever[i - 1]
    lever[i - 1] = lever[i] + lever[i - 1]
  del(lever[i])
print(coin)



