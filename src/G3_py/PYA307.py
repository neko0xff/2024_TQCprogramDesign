n = eval(input())

# 每項運算式需進行格式化排列整齊
# 每個運算子及運算元輸出的欄寬為2
# 每項乘積輸出的欄寬為4
# 皆靠左對齊不跳行
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:<2}* {:<2}= {:<4}".format(j, i, i*j), end='')
    print()