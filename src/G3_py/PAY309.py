# 舉例：
# 假設您存款$10,000，年收益為5.75%。
# 過了一個月，存款會是：10000 + 10000 * 5.75 / 1200 = 10047.92
# 過了兩個月，存款會是：10047.92 + 10047.92 * 5.75 / 1200 = 10096.06
# 過了三個月，存款將是：10096.06 + 10096.06 * 5.75 / 1200 = 10144.44
# 以此類推。

total=eval(input())
rate=float(input())
m=eval(input())

print("{:} \t  {:}".format("Month","Amount"))

for i in range(1,m+1):
    total+=(total*rate)/1200
    print("{:3d} \t {:.2f}".format(i,total))