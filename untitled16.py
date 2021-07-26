#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import time
start = time.time()
###################################### decomposiotion to int list to make sqrt
n=17
box=[]
zzz=range(1,n**2-4)
for i in zzz:
     a=math.sqrt(i)
     b=math.floor(math.sqrt(i))
     if a/b ==1:
         box.append(i)
box=box[::-1]
print(box)
######################################  

####################### algorithm to find sum of int from list 

gsum=289
#98554203937809
17**2
#list1=[121,100,81,64,49,36,25,16,9,4,1]
list1=[256, 225, 196, 169, 144, 121, 100, 81, 64, 49, 36, 25, 16, 9, 4, 1]
#list4=[336722500, 36481,  196, 169, 144, 121, 100, 81, 64, 49, 36, 25, 16, 9, 4, 1]
#sum(list4) 
##########***********************************
list2=[]
bin1=0
counter=0
w_couneter=0
while gsum != bin1:
    
    if not list1:
        print ('no solution')
        break
    else:
        for i in range(len(list1)):
                    w_couneter=w_couneter+1
                    if  [i] != len(list1) and list1[i] <= (gsum-bin1) and counter != [i]:  #should print out index not value
                        bin1=bin1 + list1[i]
                        print(bin1)
                        list2.append(list1[i])
                        print(list2)
                        counter = counter +1
                        print(counter)
        if  gsum != bin1:
            list2.clear()
            list1.pop(0)
            bin1=0
            counter=0
            i=0
        

print(w_couneter)
#############################
end = time.time()
print(end - start)














import itertools
result = list(itertools.combinations(list4,12))
sum(result)

for i in result:
    sum(result(i))
    
    
    
    
    
list4=[336722500, 36481,  196, 169, 144, 121, 100, 81, 64, 49, 36, 25, 16, 9, 4, 1]
sum(list4) 

bin1_lag=[]
sum(bin1_lag) 
##########**********find lag in the list - elements should not be equal
math.sqrt(81-64)
for i in (range(len(list4)+1)):
      while i < len(list4)-1:
          print(list4[i]**2, list4[i],list4[i+1], list4[i] - list4[i+1] )  
          x=(list4[i] - list4[i+1] )
          bin1_lag.append(x)
          break
sum(bin1_lag) 