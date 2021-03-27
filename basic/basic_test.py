data = {}
data1 = dict()

data['key1'] = 'hello'
data1['key1'] = 'hello'
print(data, data1)

if 'key1' in data:
  print(True)

data = {'1' : 'hello',
        '2' : 'world',
        '3' : '?'}

key_list = data.keys()
value_list = data.values()

print(key_list)
print(value_list)

for k in key_list:
  print(data[k])

#list casting
print(list(key_list))

##only values list
print(list(data.values()))

# #input output
# a = list(map(int, input().split()))
# print(a)

# #Is input().split() list?
# a = input().split()
# print(type(a))
# #is list

# a = input()
# print(type(a))
#if you use split(), it's a list

#use if only one line
a = 10
if a <= 30: abcde = 'hello'
print(abcde)

q = 'hello' if a >= 30 else 'world'
print(q)

a = 'week' if a >= 5 else 'wow'
print(a)

a = 0
if a >= 10 : a = 'algorithms'
print(a)

#range in list
print(list(range(5)))

#modify checking the student
scores = [22, 56, 77, 44, 44, 55, 66]
cheating_student_list = [2, 3]

#i for i in n if i not in remove_li
a = list('greate' for i in range(len(scores)) if i not in cheating_student_list)
print(a)