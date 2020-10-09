kansuji = {
    0:"零",
    1:"壱",
    2:"弐",
    3:"参",
    4:"四",
    5:"五",
    6:"六",
    7:"七",
    8:"八",
    9:"九",
    10:"拾",
    100:"百",
    1000:"千",
    10000:"万",
    100000000:"億",
    1000000000000:"兆"
}
kugiri = ["","拾","百","千"]
keta = ["","万","億","兆"]

def number2kanji(num):
    NumList = []
    kanji = ""
    # 下位からから4桁ずつ区切る
    for _ in range(len(num)//4+1):
        tmp = num[-4:]

        NumList.append(tmp)

        # 末尾の文字列を削除
        # num = num.rstrip(tmp) # この場合同じ数字が連続していると全部消える
        num = num[:-4]

        # print("num:",num)

    # リストを逆順にする
    NumList = NumList[::-1]
    print(NumList)

    # 零の処理
    if len(NumList) == 1 and NumList[0] == "0":
        kanji = "零"

    else:
        # 4桁ずつ処理していく
        for index,fourDigit in enumerate(NumList):
            tmp = ""
            # 区切りを追加
            for i in range(len(fourDigit)):
                if fourDigit[i] == "0":
                    continue
                else:
                    tmp += kansuji[int(fourDigit[i])]
                    tmp += kugiri[len(fourDigit)-i-1]

            # 桁を追加
            if fourDigit != "":
                digit = len(NumList)-index-1
                tmp += keta[digit] 
                kanji += tmp

    return kanji

# 入力str
num = input()

# 出力
print(number2kanji(num))