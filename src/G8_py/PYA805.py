# 要求使用者輸入一個長度為6的字串
# 將此字串分別置於10個欄位的寬度的左邊、中間和右邊
# 並顯示這三個結果
# 左右皆以直線 |（Vertical bar）作為邊界。

in1 = input()

print("|{:<10}|".format(in1))
print("|{:^10}|".format(in1))
print("|{:>10}|".format(in1))