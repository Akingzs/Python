def fat(num):
    if num <= 1:
        return 1
    return num * fat(num - 1)
 
n = 5
print('O fatorial de', n, 'é', fat(n))