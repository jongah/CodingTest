def solution(board, moves):
    answer = 0      #답
    basket = []     #뽑은 인형을 담을 배열 

    #인형을 뽑고 0으로 만든다.
    for i in moves:     #뽑을 위치값(x)을 하나씩 뽑아서 i에 넣는다.
        for j in range(len(board)):     #2차원공간에서 세로(y)의 길이만큼 반복한다.
            if board[j][i - 1] != 0:    #한칸씩 내려가다 0이 아닌값(인형)을 만나면
                basket.append(board[j][i - 1])      #인형의 번호를 바구니에 담는다.
                board[j][i - 1] = 0                 #인형의 자리값은 아무것도 없는 0으로 변경한다.
                break                               #가장 위의 인형을 뽑았으므로 반복을 끝낸다.
    i = 1                 #이전 값과 비교할 바구니의 인덱스 값이므로 (i-1)의 연산을 수행해야 하기 때문에 1부터 시작한다.
    check = len(basket)   #바구니의 배열 길이만큼 반복한다.
    while i < check:      #바구니보다 i 가 작을 때 반복한다.
      if basket[i] == basket[i - 1]:    #만약 i 와 i-1(이전값)이 일치 한다면
            answer += 2                 #answer += 2(2개의 인형이 사라짐)
            del basket[i]               #(i) 와 (i -1)의 값을 지운다.(지움으로서 양끝값이 만나 사라질 수 있기 때문에)
            del basket[i - 1]         
            i = 1                       #값을 지움으로서 또다른 인형이 서로 만날 수 있으므로 i를 1로 하고 처음부터 다시 반복 한다.
            check = len(basket)         #값을 지워 바구니의 크기도 줄어들었으므로 새로 길이를 잰다.
      i += 1                            #i ++
    print(answer)                       #최종적으로 사라진 인형의 개수를 반환한다.


#인형을 빼고 0(빈칸)으로 변경
#값 지우고 다시 돌리기
#len(b)의 값이 줄어듦

b = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2],
     [3, 5, 1, 3, 1]]
d = [1, 5, 3, 5, 1, 2, 1, 4]

solution(b, d)
