# kanjinumbers.com


## URL
[作成したWebAPIサービス](http://ec2-3-112-175-24.ap-northeast-1.compute.amazonaws.com/)
## 概要
- 領収書や小切手に記載するような「壱万五千」のような漢数字表記を取り扱うサービス 
- 漢数字からアラビア数字，アラビア数字から漢数字へ変換を行う

    <!-- 
    | アラビア数字 | 漢数字 |
    | :---: | :---: |
    | 0 | 零 |
    | 1 | 壱 |
    | 2 | 弐 |
    | 3 | 参 |
    | 4 | 四 |
    | 5 | 五 |
    | 6 | 六 |
    | 7 | 七 |
    | 8 | 八 |
    | 9 | 九 |
    | 10 | 拾 |
    | 100 | 百 |
    | 1000 | 千 |
    | 10000 | 万 |
    | 100000000 | 億 |
    | 1000000000000 | 兆 |
     -->
  
    | 入力 | 出力 |
    | :---: | :---: |
    | 0 | 零 |
    | 1 | 壱 |
    | 2 | 弐 |
    | 3 | 参 |
    | 4 | 四 |
    | 5 | 五 |
    | 6 | 六 |
    | 7 | 七 |
    | 8 | 八 |
    | 9 | 九 |
    | 10 | 壱拾 |
    | 101 | 壱百壱 |
    | 1010 | 壱千壱拾 |
    | 10947 | 壱万九百四拾七 |
    
- 取り扱い可能な数字は，0以上，9999兆9999億9999万9999以下の整数値
- APIのエンドポイント
    - アラビア数字から漢数字： /v1/number2kanji/{アラビア数字}
    - 漢数字からアラビア数字： /v1/kanji2number/{漢数字}
- 変換できない入力の場合は，HTTPのステータスコード204を返す
- WebAPI経由で他のシステムから利用されることを想定しているが，サービス理解のためのUIも提供

## 使い方
