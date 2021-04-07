def solution(participant, completion):
  answer = 'z'
  for i in participant:
    if participant.count(i) > 1:
      completion.remove(i)
    if i not in completion:
      answer = i
      break
  print(answer)

solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])