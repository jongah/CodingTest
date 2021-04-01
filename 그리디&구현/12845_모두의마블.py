coin = 0
n = int(input())
cards = list(map(int,input().split()))
ma = max(cards)
del (cards[cards.index(max(cards))])
#print(cards)
for card in cards:
    coin+=(card+ma)

print(coin)

n = int(input()) # 카드의 개수 입력 받음
cards = list(map(int,input().split())) # 카드의 레벨

level = max(cards) # 카드 중에서 가장 레벨이 높은 것 저장
del cards[cards.index(max(cards))] # 가장 레벨 높은 카드 삭제
gold = 0 # for문에서 사용하기 위한 초기화
for i in range(len(cards)): # 카드의 개수만큼 for문 돌림 
  gold += level+cards[i] # 레벨과 카드의 값 더하기
print(gold) # 골드의 최댓값 출력