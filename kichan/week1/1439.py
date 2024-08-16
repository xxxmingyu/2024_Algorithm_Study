n = input()
cnt = 0

for i in range(0,len(n)-1):
    if n[i] != n[i+1]:
        cnt += 1

print((cnt+1)//2)

'''
cnt : 변화한 횟수
인풋으로 받은 숫자를
처음부터 뒷 숫자와 다르면 cnt + 1

0 -> 0 -> 0
01 -> 1 -> 1
010 -> 2 -> 1
0101-> 3 -> 2
01010 -> 4 -> 2
010101 -> 5 -> 3
'''