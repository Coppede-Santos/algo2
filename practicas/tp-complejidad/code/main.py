from binarytree import * 
from linkedlist import add, length 


def contiene_suma (A,n):
  if A.head==None: return False
  B=BinaryTree()
  current=A.head
  while current!=None:
    insert(B,current.value,current.value)
    current=current.nextNode
  comprobante=False
  current=A.head
  while comprobante==False and current!=None:
    complementario=n-current.value
    if search(B,complementario)!=None:
      comprobante=True
    current=current.nextNode
  return comprobante



lista=LinkedList()
add(lista,5)
add(lista,1)
add(lista,1)
add(lista,1)
add(lista,-2)
add(lista,9)
add(lista,7)
add(lista,8)
add(lista,1)


print(contiene_suma(lista,5))
lista=[1,5,8,4,2,7,3,9,0,11,13,67,43,-1,12]


def ordenamiento_mitad(L):
  n=len(L)
  L.sort()
  num=L[round(n/2)]

  for i in range (0,round(n/4)):
    temporal=L[i]
    L[i]=L[n-i-1]
    L[n-i-1]=temporal
  print (L)

ordenamiento_mitad(lista)
