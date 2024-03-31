# 依照使用者輸入的n
# 畫出對應的等腰三角形
# 以 * 畫出等腰三角形（每列最後一個 * 的右方無空白）

n=eval(input())

for i in range(1,n+1):
    for j in range(0,n-i):
        print(' ', end='')
    for k in range(1,i*2):
        print('*', end='')
    print()