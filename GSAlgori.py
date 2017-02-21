#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C),2014-2016, YTC, BJFU, www.bjfulinux.cn
Created on 2017/2/21 08:31

@author: Gaoxiang Yang, ytc, recessburton@gmail.com
@version: 0.1
"""

"""
@discription:
G-S 稳定匹配算法的实现,模拟男女配对问题.
采用最朴素的算法,时间复杂度O(n²).
"""

manPreferenceList = [[2,3,1,0],
                     [2,1,3,0],
                     [0,2,3,1],
                     [1,3,2,0]]

womanPreferenceList = [[0,3,2,1],
                       [0,1,2,3],
                       [0,2,3,1],
                       [1,0,3,2]]

bachelors = [0,1,2,3]
spinsters = [0,1,2,3]

def getRank(i, prefer):
        return womanPreferenceList[i].index(prefer)

def getBachelorIndex(bachelor):
    return bachelors.index(bachelor)

def getSpinsterIndex(spinster):
    return spinsters.index(spinster)

engaged = []

def findFiance(girl):
    for peer in engaged:
        if girl in peer:
            return peer[0]

def flushFiance(girl, boy):
    for peer in engaged:
        if girl in peer:
            bachelors.append(peer[0])                             #return her ex to bachelors... poor guy
            peer[0] = boy
            bachelors.pop(getBachelorIndex(boy))                  #this guy's never single
            return

while bachelors.__len__():
    """
    tip: CANNOT use for...in here  for bachelors list will change in a loop.
    """
    bachelor = bachelors[0]
    for preferGirl in manPreferenceList[bachelor]:
        if preferGirl in spinsters:
            engaged.append([bachelor, preferGirl])                #add to engaged set
            bachelors.pop(getBachelorIndex(bachelor))             #delete from bachelors list
            spinsters.pop(getSpinsterIndex(preferGirl))           #delete from spinsters list
            break                                                 #end for this boy
        else:
            currentRank = getRank(preferGirl, bachelor)
            competitorRank = getRank(preferGirl, findFiance(preferGirl))
            if currentRank < competitorRank:
                flushFiance(preferGirl, bachelor)                 #change her fiance...
                break                                             #end for this boy

print engaged
#should be [[0, 2], [1, 1], [2, 0], [3, 3]]




