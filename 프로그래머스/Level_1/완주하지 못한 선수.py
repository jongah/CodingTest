#정렬 후 하나씩 비교하다 다른것이 나오면 리턴한다. 
#만약 끝까지 나오지 않는다면 participant의 마지막 값을 리턴

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    return participant[-1]
  
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

#다른사람 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
  
  
