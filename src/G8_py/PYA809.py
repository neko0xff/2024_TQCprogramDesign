# 要求使用者輸入一個密碼（字串）
# 檢查此密碼是否符合規則
# 密碼規則如下：
# a. 必須至少八個字元。
# b. 只包含英文字母和數字。
# c. 至少要有一個大寫英文字母。
# d. 若符合上述三項規則，程式將顯示檢查結果為【Valid password】，否則顯示【Invalid password】

in1 = input()
rule_time = 0
a = 0
b = 0
c = 0
words = 8

for i in range(len(in1)):
    if(len(in1)>=words):
        a = 1
    if(in1[i].isupper() == True):
        b = 1
    if(in1[i].isalnum() == True):
        c = 1

rule_time = a+b+c

if(rule_time < 3):
    print("Invalid password")
else:
    print("Valid password")