# -*- coding: UTF-8 -*-
__author__ = 'waveli'

# from datatag import checkSentenceEntity
#
# dictionary = ['word_ch','中国','日本']
# sentence = '中国是个有着悠久历史的国家，则没有'
#
# print checkSentenceEntity(sentence,dictionary)

# import jieba
# jieba.add_word("中国美")
# print('/'.join(jieba.cut("中国美日本差")))

# from datatag import addEntitiesRelations
#
# addEntitiesRelations()

# print str(float(3)/float(2)*100) + "%"

fo = file(r'E:/financeXML\\090924687496_1158.txt', "a+")
fo.write(str('E:/JinTong/finance\\090924687496_1158.txt') + "\n")
fo.close()