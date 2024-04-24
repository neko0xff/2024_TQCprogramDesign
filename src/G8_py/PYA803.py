# 讓使用者輸入一個句子
# 至少有五個詞，以空白隔開
# 並輸出該句子倒數三個詞

in1 = input()
str1 = in1.split(" ")

print("{} {} {}".format(str1[-3],str1[-2],str1[-1]))
