n = list(map(int,list(input())))
front = sum(n[:int(len(n)/2)])
back = sum(n[int(len(n)/2):])
if front == back:
  print('LUCKY')
else:
  print('READY')
