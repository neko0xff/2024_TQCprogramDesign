# 某次選舉有兩位候選人，分別是No.1: Nami、No.2: Chopper。
# 請撰寫一程式，輸入五張選票，
# 輸入值如為1即表示針對1號候選人投票；
# 輸入值如為2即表示針對2號候選人投票，
# 如輸入其他值則視為廢票。
# 每次投完後需印出目前每位候選人的得票數，最後印出最高票者為當選人；
# 如最終計算有相同的最高票數者或無法選出最高票者，顯示【=> No one won the election.】
# 註: 請注意輸出格式(尤其是空格)

runtime=5
vote_1=0
vote_2=0
vote_other=0

for i in range(1,runtime+1):
    in1=eval(input())
    if(in1==1):
        vote_1+=1
    elif(in1==2):
        vote_2+=1
    else:
        vote_other+=1
        
    print("Total votes of No.1: Nami =  {}".format(vote_1))
    print("Total votes of No.2: Chopper =  {}".format(vote_2))
    print("Total null votes =  {}".format(vote_other))

if(vote_1>vote_2):
    print("=> No.1 Nami won the election.")
elif(vote_1<vote_2):
    print("=> No.2 Chopper won the election.")
else:
    print("=> No one won the election.")
