#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

  #  .Ho+20313   .Ho-3 +18351  .Ho+2204  .Ho+9226449   .Ho+20412   .Ho+9927447   .Ho+38477   .Ho+20313   t10  t12   t14  16  20 t22 t24
      #t10  t12   t14  16  20 t22 t24
n=17
step0=n
step1 =             (n) -2    
print(step1)
red1 =(n**2 - step1**2)
step2= math.floor(math.sqrt(red1))              #loop N1
print(step2)
red2 = (red1 - step2**2)
step3= math.floor(math.sqrt(red2))             #loop N2
print(step3)
red3 = (red2 - step3**2) 
step4= math.floor(math.sqrt(red3))           #loop N3
print(step4)
red4 = (red3 - step4**2) 
step5= math.floor(math.sqrt(red4))             #loop N4
print(step5)
red5 = (red4 - step5**2) 
step6= math.floor(math.sqrt(red5))             #loop N5
print(step6)
red6 = (red5 - step6**2)   
step7= math.floor(math.sqrt(red6))            #loop N6
print(step7)
red7 = (red6 - step7**2) 
step8= math.floor(math.sqrt(red7))             #loop N7
print(step8)
red8 = (red7 - step8**2) 
step9= math.floor(math.sqrt(red8))  
print(step9)
red9 = (red8 - step9**2) 
step99= math.floor(math.sqrt(red9)) 

print(16**2)
#[256, 144]