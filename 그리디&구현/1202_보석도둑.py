def JewelThief():
  n = 3
  k = 2
  jewel = [[1, 65], [5, 23], [2, 99]]
  b = [10, 2]

  # 입력 완료 했다 치고 여기서 부터 계산
  b.sort()
  result = 0
  passIndex = [-1]*k

  for i in range(k):
    count = 0
    for j in range(n):
      if jewel[j][0] <= b[i] and j not in passIndex:
        print(jewel[j][1], count)
        if jewel[j][1] > count:
          count = jewel[j][1]
          passIndex[i] = j
          print(count)
    result += count
  print(result)
  #작은 가방부터 나열한다.
  #가방에 들어갈 수 있는 무게의 보석 중 가장 비싼 보석을 추가 한다.

JewelThief()