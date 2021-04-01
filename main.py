
n, k = map(int, input().split())
jewel = []
b = []
for i in range(n):
  a = list(map(int, input().split()))
  jewel.append(a)
for i in range(k):
  b.append(int(input()))

b.sort()
result = 0
passIndex = [-1]*k

for i in range(k):
  count = 0
  for j in range(n):
    if jewel[j][0] <= b[i] and j not in passIndex:
      if jewel[j][1] > count:
        count = jewel[j][1]
        passIndex[i] = j
  result += count

print(result)
  #작은 가방부터 나열한다.
  #가방에 들어갈 수 있는 무게의 보석 중 가장 비싼 보석을 추가 한다.
