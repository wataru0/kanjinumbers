suji = {
    "零":0,
    "壱":1,
    "弐":2,
    "参":3,
    "四":4,
    "五":5,
    "六":6,
    "七":7,
    "八":8,
    "九":9
}

kugiri = {
    "拾":10,
    "百":100,
    "千":1000
}

keta = {
    "万":10000,
    "億":100000000,
    "兆":1000000000000
}

def kanji2number(kansuji):
    number = 0
    tmp = 0
    for kanji in kansuji:
        if kanji in kugiri:
            number += tmp*kugiri[kanji]
            tmp = 0
        elif kanji in keta:
            number += tmp
            number *= keta[kanji]
            tmp = 0
        else:
            tmp += suji[kanji]

    number += tmp
    return number

# # 入力 
# kansuji = input()
# # 出力
# print(kanji2number(kansuji))