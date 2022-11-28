
import math
def f(x): 
  return 3*math.sqrt(x)
  
areal_verdier = []
areal_trapes = []
start_verdi = 1
slutt_verdi = 2
ant_rek = 100
bredde_rek = (slutt_verdi-start_verdi)/ant_rek
rektangel_startpos = bredde_rek*0
## 0 = venstremetode, 0.5 = midt, 1= høyre

for i in range(ant_rek): ##rektangelmetode
  a = f(i*bredde_rek+rektangel_startpos+start_verdi)*bredde_rek
  areal_verdier.append(a)

for i in range (ant_rek): ##trapesmetode
    a= f(start_verdi+(i-1)*bredde_rek)*bredde_rek
    areal_trapes.append(a)
 




print(sum(areal_verdier))
print(sum(areal_trapes))
