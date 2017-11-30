#!/usr/bin/python
def similarity(a,b):
    len_a = len(a)
    len_b = len(b)
    count = 0
    distance = 0
    lentotal = float(len_a + len_b)
    if len_a > len_b:
        dis_len = len_a - len_b
        while len_b > count: 
            if a[count] == b[count]:
                pass
            else:
                distance = distance + 1
            count= count + 1        
    else:
        while len_a > count: 
            if a[count] == b[count]:
                pass
            else:
                distance = distance + 1
            count= count + 1        
        dis_len = len_b - len_a
    distance = dis_len + distance
    similarity = (lentotal - distance)/lentotal*100
    return distance,similarity
similarity("apple","lepple")