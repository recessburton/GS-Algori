#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C),2014-2016, YTC, BJFU, www.bjfulinux.cn, www.muheda.com
Created on 2017/2/21 16:00

@author: Gaoxiang Yang, ytc, yanggaoxiang@dtbpoint.com
@version: 0.1

@description

用简化的博弈思想实现的模拟男女匹配问题.

"""
from numpy import *
import numpy as np

manPreferenceList = [[2,3,1,0],
                     [2,1,3,0],
                     [0,2,3,1],
                     [1,3,2,0]]

womanPreferenceList = [[0,3,2,1],
                       [0,1,2,3],
                       [0,2,3,1],
                       [1,0,3,2]]


mangrades = []
womangrades = []

def getManGrade():
    """
    a.排位序号
    b.计算在每位男士心仪女士在女士心中的得分,处在index 0的为4分,1的为3分...
    形成元组(a,b)矩阵
    like this:[[(4, 4), (3, 3), (2, 4), (1, 4)],
                [(4, 1), (3, 3), (2, 4), (1, 1)],
                [(4, 2), (3, 3), (2, 1), (1, 2)],
                [(4, 1), (3, 2), (2, 2), (1, 3)]]
    """
    manid = -1
    for man in manPreferenceList:
        manid = manid+1
        mangrade=[]
        for p in man:
            mangrade.append((-man.index(p)+4, -womanPreferenceList[p].index(manid)+4))
        mangrades.append(mangrade)

def getWomanGrade():
    womanid = -1
    for woman in womanPreferenceList:
        womanid = womanid+1
        womangrade=[]
        for p in woman:
            womangrade.append((-woman.index(p)+4, -manPreferenceList[p].index(womanid)+4))
        womangrades.append(womangrade)

getManGrade()
getWomanGrade()

manEvalu = []
womanEvalu = []

def getmanA():
    """
    计算mangrade中每个元组的乘积,作为得分(a*b)
    like this:[[16, 9, 8, 4],
                [4, 9, 8, 1],
                [8, 9, 2, 2],
                [4, 6, 4, 3]]
    """
    for l in mangrades:
        manEvalu.append([t1*t2 for (t1, t2) in l])

def getwomanA():
    for l in womangrades:
        womanEvalu.append([t1*t2 for (t1, t2) in l])

getmanA() #like this:
getwomanA()
gradeMat =  mat(manEvalu)+mat(womanEvalu)
"""
评价函数,男女心仪对象在对方心中得分的和,若相互心仪,则得分最高。
男女双方博弈,评价函数得分最高者被选取。
[[20 12 16  5]
 [12 18 10  5]
 [24 18  6  6]
 [12 15 10  5]]
 比如第一轮选24,打印24的index(2,0),表示男2和女0,删除第2行,第0列(此处使用分数置0代替);
 第二轮选18,打印18的index(1,1),表示男2和女0,第1行和第1列全部置0
 ...
 直到矩阵中元素最大值为0

"""
while True:
    raw, column = gradeMat.shape
    _position = np.argmax(gradeMat)
    max_r, max_c = divmod(_position, column)
    max = gradeMat[max_r, max_c]
    if max == 0:
        break
    print (max_r, max_c)
    grades = gradeMat.tolist()
    grades[max_r] = [0]*column
    for row in grades:
        row[max_c] = 0
    gradeMat = mat(grades)

"""
output like this:
(2, 0)
(1, 1)
(0, 2)
(3, 3)
"""



