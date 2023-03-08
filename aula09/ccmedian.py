"""
Complete a função para devolver a mediana da lista de valores lst.
A função não deve modificar a lista.
Se a lista tiver um número ímpar de valores,
a mediana é o valor no meio da lista ordenada.
Se a lista tiver um número par de valores,
a mediana é a média dos dois valores no meio da lista ordenada.
"""

def median(lst):
   assert len(lst) > 0
   l2=sorted(lst)
   first=0
   last=len(l2)
   m=len(l2)
   if m%2==1:
      mid=(first+last)//2
      return l2[mid]
   elif m%2==0:
      mid=(first+last)//2
      k=((first+last)//2)-1
      med=(l2[mid]+l2[k])/2
      return med
      
      

def check(lst):
   backup = lst.copy()
   m = median(lst)
   return m, lst

