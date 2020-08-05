for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i*j}',end='\t') #Note: f' means formatting strings
        #Note: print('%d*%d=%d' % (i,j,i*j), end='\t') also works, but it's complicated.
    print()
