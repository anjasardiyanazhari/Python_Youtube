#stacks
stacks = [1,2,3,4,5,6]
print('data sekarang:',stacks)

# memasukan data baru
stacks.append(7)
print('data masuk:',7)
print('data sekarang:',stacks)
stacks.append(8)
print('data masuk:',8)

print('data sekarang:',stacks)

out = stacks.pop()
print('dara sekarang:',stacks)
print('data keluar:',out)

print(50*'=')

#queues

from collections import deque

antrian = deque([1,2,3,4,5])
print('data sekarang:',antrian)

#menambahkan data
antrian.append(6)
print('data masuk:',6)
print('data sekarang:',antrian)

antrian.append(7)
print('data masuk:',7)
print('data sekarang:',antrian)

#mengurangi antrian
out = antrian.popleft()
print('data sekarang:',antrian)
print('data keluar:',out)