#basic python
import sys

#int casting
a = int(13.9)
print(a)

#round
a = round(12.33333333, 2)
print(a)

#//
a = 8 // 3
print(a)

#list reset
a = [2] * 10
print(a)

a = [i for i in range(10)]
print(a)

#slicing
print(a[2:4])

a = [i for i in range(20) if i%2 == 1]
print(a)

#*2 array reset
a = [[1] * 10 for _ in range(10)]
print(a)

a = [[i for i in range(10)] for _ in range(10)]
a[0][0] = 99
print(a)

#same object
a = [[1] * 2] * 3
a[1][1] = 99
print(a)

#function
n = [i for i in range(10)]
n.append(4)
print(n)
n.sort(reverse = True)
print(n)
n.insert(3, 99)
print(n)
print(n.count(4))
n.remove(4)
print(n)

#rmove all
remove_set = {3, 4}
result = [i for i in n if i not in remove_set]
print(result)

remove_li = [99, 0]
result = [i for i in n if i not in remove_li]
print(result)

#string
a = 'helloworld'
print(a[0])

#char and tuple are not change
a = (2,3,4,5,3)
print(a[2:4])

a = ('key', 45)
print(a)

#dic
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

#set Data type
b = [i for i in range(10)]
b.append(3)
print(b)
d = set(b)
print(d)

d = {2,3,4,5,5,5,5,3}
print(d)

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

#union
print(a | b)
#lntersection
print(a & b)
#diffence
print(a - b)

a.add(9)
a.update([33, 44])
a.remove(2)
print(a)

#input output
#a = list(map(int, input().split()))
#print(a)

#map
#a, b, c = map(int, input().split())
#print(a,b,c)
#d = list(map(int, input().split()))
#print(d)

b = [3.44444, 3.22222, 4.99999]
d = list(map(str, b))
print(d)

#x = input().split()    
#m = map(int, x)       
#a, b = m
#print(m)    
#print(a)

#fast input
#d = sys.stdin.readline().rstrip()
#print(d)

#end
print(3, end = '')
print(str(4) + 'hello')
print(f'{3} no error')

#Operator
a = [1,2,3,4,5]
print(1 in a)
print(1 not in a)

#pass
if 2 in a:
  pass

#if one line
a = 10
if a <= 30: p = 'hello'
print(p)

q = 'hello' if a >= 30 else 'world'
print(q)

a = 20
if 10 < a < 30:
  print('wow')

#while
x = 0
while x < 5:
  x += 1
  print(x)

#range
a = range(0, 5)
print(a)
#range(0, 5)

a = [range(9)]
print(a)
#[range(0, 9)]

a = list(range(5))
print(a)

#for
for i in a:
  print(i)

for i in range(1, 10 + 1):
  print(i)

for i in range(10 + 1):
  print(i)

#continue / break
for i in range(10, 20 + 1):
  if(i%2 == 0): continue
  if(i == 17): break
  print(i)

#ex
scores = [22, 56, 77, 44]
cheating_student_list = [2, 3]

for i in range(len(scores)):
  if i + 1 in cheating_student_list:
    print('print')
    continue
  if scores[i] >= 10:
    print(i + 1, 'great!!')

#function
def add(a , b):
  print(a + b)

add(b = 4, a = 10)

#wide value
a = 10

def ex():
  global a
  print(a)

ex()
#inner value first refer

#unpacking
def ex2():
  return 3,4,5,6

a, b, c, d = ex2()
print(a, b, c, d)

def ex3():
  return [3, 4, 5]

a, b, c = ex3()
print(a, b, c)

def ex4():
  return (3, 4, 5)

a, b, c = ex4()
print(a, b, c)

#lambda
print((lambda a, b, c : a + b + c)(3, 4, 5))

#ex
a = [('kang', 30), ('jong', 20), ('ah', 10)]

def my_key(x):
  return x[1]

print(sorted(a, key = my_key))
print(sorted(a, key = lambda x : x[1]))

b = a[0]
print(b[0])

#ex
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]

r = map(lambda a, b : a + b, l1, l2)

print(list(r))

#inner function
print(sum([1, 2, 3]))
print(min([1, 2, 3]))
print(max(3, 4, 5))
print(eval('(2 + 4)'))

#permutations
from itertools import permutations
d = ['a', 'b', 'c']
r = list(permutations(d, 3))
print(r)

#combinations
from itertools import combinations
r = list(combinations(d, 2))
print(r)

#product / replacement
from itertools import product
r = list(product(d, repeat = 2))
print(r)

#combinations / replacement
from itertools import combinations_with_replacement
r = list(combinations_with_replacement(d, 2))
print(r)

#counter
from collections import Counter
c = Counter([2, 3, 3, 3, 2, 2, 5, 5, 5])
print(c)
print(c[2])

#g
import math

print((lambda a, b, c : a + b + c)(3, 4, 5))
print(math.gcd(21, 14))
print((lambda a, b : a * b // math.gcd(a, b))(21, 14))
