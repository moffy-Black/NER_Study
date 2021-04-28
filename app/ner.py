# -*- coding: utf-8 -*-
from pymagnitude import Magnitude
from sudachipy import tokenizer, dictionary
import pandas as pd


vectors = Magnitude("chive-1.2-mc5.magnitude")
text = "強くなれる理由を知った 僕を連れて進め 泥だらけの走馬灯に酔う こわばる心 震える手はつかみたいものがある それだけさ 夜の匂いに I'll spend all thirty nights 空睨んでも Staring into the sky 変わっていけるのは自分自身だけさ それだけさ 強くなれる理由を知った 僕を連れて進め どうしたって！ 消せない夢も 止まれない今も 誰かの強くなれるなら ありがとう 悲しみよ 世界に打ちのめされて 負ける意味を知った 紅蓮の華よ咲き誇れ！ 運命を照らして イナビカリの雑音が耳を指す 戸惑う心 優しいだけじゃ守れないものがある？ わかってるけど 水面下で絡まる善悪 透けて見える偽善に天罰 Tell me why, Tell me why, Tell me why,Tell me... I don't need you！ 逸材の花より　挑み続け咲いた一輪が美しい 乱暴に敷き詰められた トゲだらけの道も 本気の僕だけに現れるから 乗り超えてみせるよ 簡単に片づけられた 守れなかった夢も 紅蓮の心臓に根を生やし この血に宿って 人知れず儚い 散りゆく結末 無情に破れた 悲鳴の風吹く 誰かの笑う影 誰かの泣き声 誰もが幸せを願っている どうしたって！ 消せない夢も 止まれない今も 誰かのために強くなれるなら ありがとう 悲しみよ 世界に打ちのめされて 負ける意味を知った 紅蓮の花よ咲き誇れ！ 運命を照らして 運命を照らして"
df = pd.DataFrame()

tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.C
[
    print(
        m.surface(),
        m.dictionary_form(),
        m.reading_form(),
        m.part_of_speech(),
        vectors.similarity("私",m.dictionary_form())
    )
for m in tokenizer_obj.tokenize(text, mode)]

# print(df)