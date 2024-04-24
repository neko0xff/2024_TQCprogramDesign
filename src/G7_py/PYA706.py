# 全字母句（Pangram）是英文字母表所有的字母都出現至少一次（最好只出現一次）的句子
# 請撰寫一程式，要求使用者輸入一正整數k（代表有k筆測試資料）
# 每一筆測試資料為一句子
# 程式判斷該句子是否為Pangram，並印出對應結果True（若是）或False（若不是）
# 提示：不區分大小寫字母

k = int(input())

for i in range(k):
    in1 = input().upper()
    set1 = set(in1)
    set1.remove(" ")
    if(len(set1) == 26): print(True)
    else: print(False)
