# 要求使用者輸入一字串
# 顯示該字串每個字元的對應ASCII碼及其總和

in1 = input()
total = 0

for i in in1:
    ascii_code = ord(i)
    print("ASCII code for '{}' is {}".format(i,ascii_code))
    total+=ascii_code

print(total)