# 提示使用者輸入一個社會安全碼SSN
# 格式為ddd-dd-dddd，d表示數字。
# 若格式完全符合（正確的SSN）則顯示【Valid SSN】，否則顯示【Invalid SSN】

in1 = input()
num_str1 = in1.split("-")
out = num_str1[0]+num_str1[1]+num_str1[2]

if(out.isdigit() == True):
    print("Valid SSN")
elif(out.isdigit() == False):
    print("Invalid SSN")
else:
    print("Invalid SSN")
    