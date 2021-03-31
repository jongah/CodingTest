
def Dna (d, m):
  l = []
  count = 0
  new = list(map(list, zip(*d)))

  for i in range(len(new)):
    a = max(new[i], key=new.count)
    count += m - new[i].count(a)
    l.append(a)
  print(''.join(l), count)

dna = ['ACGTACGTAC', 'CCGTACGTAG', 'GCGTACGTAT', 'TCGTACGTAA']
Dna(dna, 4)
