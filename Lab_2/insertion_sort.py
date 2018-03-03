def default_compare(a, b):
  if a < b:
    return -1
  elif a > b:
    return 1
  return 0

def sort(array, compare=default_compare):
  for i in range(0, len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
      if compare(array[j], array[min_index]) < 0:
        min_index = j
    if min_index != i:
      array[i], array[min_index] = array[min_index], array[i]
  return array