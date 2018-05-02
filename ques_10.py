def sub_set(a):
  p_set = [[]]
  for item in a:
	p_set = p_set + [[item] + list(sset) for sset in p_set]
  return p_set[1:]
 
print(sub_set([1,2,3]))
