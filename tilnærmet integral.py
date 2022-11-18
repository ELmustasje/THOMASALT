# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
def f(x): 
  return 3*math.e**(-x**2/2)
  
areal_verdier = []
start_verdi = -2
slutt_verdi = 2
ant_rek = 50
bredde_rek = (slutt_verdi-start_verdi)/ant_rek
rektangel_startpos = 0* bredde_rek

for i in range (ant_rek):
  a = f(i*bredde_rek+rektangel_startpos+start_verdi)*bredde_rek
  areal_verdier.append(a)
 

  ##Test


print(sum(areal_verdier))
