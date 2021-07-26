#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
workshop
"""

import math

n=17
m=n**2
z=math.floor(math.sqrt(m-1))
bin1=[z]
bin1_lag=[]

# find squaresum descending
while z>0:
    m=m-z**2
    z=math.floor(math.sqrt(m))
    #print(z)
    bin1.append(z) 
bin1.pop()

# find lag in the list - lag should be more than 0
for i in (range(len(bin1)+1)):
      while i < len(bin1)-1:
          print(bin1[i]**2, bin1[i],bin1[i+1], bin1[i] - bin1[i+1] )  
          x=(bin1[i] - bin1[i+1] )
          bin1_lag.append(x)
          break

#if lag more than zero print result === else: 


#find index of lag where value is zero or less 
bin1_lag.index(0)

#cut out value from bin1 list located as from the zero lag index value plus one
        
#power and decompose the value ***

#merge decomposed value with non decomposed values from bin1 ist

#find and print slution if exists === else: 
    
#cut first value from decomposed list *** end reapet next steps 







    
#check the square sum in the list
bin1_sum=sum([i**2 for i in bin1])
bin1_prod=math.prod(bin1_lag)
