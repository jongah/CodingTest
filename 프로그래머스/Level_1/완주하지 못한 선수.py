#정렬 후 하나씩 비교하다 다른것이 나오면 리턴한다. 
#만약 끝까지 나오지 않는다면 participant의 마지막 값을 리턴

def solution(participant, completion):
    participant.sort() #정렬
    completion.sort()
    for i in range(len(completion)): #completion만큼 돌린다. 이때 participant를 넣으면
        if participant[i] != completion[i]: #여기서 리스트 범위 에러난다.
            answer = participant[i]
            return answer #더 돌지 말고 바로 리턴 시킨다.
    return participant[-1] #다 돌았는데 일치한다면 participant의 마지막 값이 답
  
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


#다른사람 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
  
  
