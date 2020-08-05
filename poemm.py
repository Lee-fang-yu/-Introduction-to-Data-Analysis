# coding: utf-8
from numpy.random import randint
from numpy.random import choice
#之所以會用''' '''是由於一般字串只能寫成一行沒辦法這樣分行
words='''
我
我的
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
回首
吹過
思念
靈魂
思慕
停止
頃城
踟躕
依戀
木神
巧目盼兮
心扉
椎間盤'''
phrase = words.split('\n')
#整首詩長度
l = randint(3, 6)

for i in range(l):
    
    #某句話有幾個字(此處為5-7個字)
    ll = randint(5, 8)
    
    #選詞
    egg =  choice(phrase , ll)
    ham = ' '.join(egg)
    print(ham)
