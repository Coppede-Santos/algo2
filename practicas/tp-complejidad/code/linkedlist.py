from algo1 import *

class LinkedList:
  head=None

class Node:
  value=None
  nextNode=None
##add(L,element)
#Descripción: Agrega un elemento al comienzo de L, siendo L una LinkedList que representa el TAD secuencia. Entrada: La Lista sobre la cual se quiere agregar el elemento (LinkedList) y el valor del elemento (element) a agregar.
##Salida: No hay salida definida

def add(L,element):
  signode= Node()
  signode.value=element
  signode.nextNode=L.head
  L.head=signode
#search(L,element)
#Descripción: Busca un elemento de la lista que representa el TAD secuencia.
#Entrada: la lista sobre el cual se quiere realizar la búsqueda (Linkedlist) y el valor del elemento (element) a buscar.
#Salida: Devuelve la posición donde se encuentra la primera instancia del elemento. Devuelve None si el elemento no se encuentra.

def search (L,element):
  nodeprox=L.head
  compro=False
  cont=0
  while nodeprox != None:
    if nodeprox.value==element:
      posicion=cont
      compro=True
    cont+=1
    nodeprox=nodeprox.nextNode
  if compro:
    return posicion
##update(L,element,position)
##Descripción: Permite cambiar el valor de un elemento de la lista en una posición determinada
##Entrada: La lista (LinkedList) y la position sobre la cual se quiere asignar el valor de element.
##Salida:Devuelve None si no existe elemento para dicha posición. Caso contrario devuelve la posición donde pudo hacer el update.

def update (L,element,position):
  nodeprox=L.head
  cont=0
  while cont != position and nodeprox.nextNode!=None:
    nodeprox=nodeprox.nextNode
    cont+=1
  if cont==position:
    nodeprox.value=element
    return cont


def delete (L,element):
  cont=0
  if L.head == None or search(L,element)==None:
    return 
  nodeprox=L.head
  nodeant=L.head
  if search(L,element) != 0:
    while nodeprox.value != element and nodeprox.nextNode!= None:
      cont=cont+1
      nodeant=nodeprox
      nodeprox=nodeprox.nextNode
    if nodeprox.value==element:
      nodeant.nextNode=nodeprox.nextNode
      return cont
  else:
    L.head=L.head.nextNode
    return 0 

#length(L)
#Descripción: Calcula el número de elementos de la lista que representa el TAD secuencia.
#Entrada: La lista sobre la cual se quiere calcular el número de elementos.
#Salida: Devuelve el número de elementos.


def length(L):
  nodeprox=L.head
  cont=0
  while nodeprox != None:
    nodeprox=nodeprox.nextNode
    cont+=1
  return cont 

#access(L,position)
#Descripción: Permite acceder a un elemento de la lista en una posición determinada.
#Entrada: La lista (LinkedList) y la position del elemento al cual se quiere acceder.
#Salida: Devuelve el valor de un elemento en una position de la lista, devuelve None si no existe elemento para dicha posición.

def access (L,position):
  if position>length(L):
    return 
  nodeprox=L.head
  cont=0
  while cont != position and nodeprox.nextNode!= None:
    cont+=1
    nodeprox=nodeprox.nextNode
  if cont==position:
    return nodeprox.value
      
#insert(L,element,position)
#Descripción: Inserta un elemento en una posición determinada de la lista que representa el TAD secuencia.
#Entrada: la lista sobre el cual se quiere realizar la inserción (Linkedlist) y el valor del elemento (element) a insertar y la posición (position) donde se quiere insertar.
#Salida: Si pudo insertar con éxito devuelve la posición donde se inserta el elemento. En caso contrario devuelve None. Devuelve None si la posición a insertar es mayor que el número de elementos en la lista.

def insert(L,element,position):
  if position==0:
    add(L,element)
    return 0
  elif L.head==None:
    return 
  nodeprox=L.head
  nodeant=L.head
  cont=0
  while cont!=position and nodeprox!=None:
    nodeant=nodeprox
    nodeprox=nodeprox.nextNode
    cont+=1
  if cont==position:
    signode= Node()
    signode.value=element
    signode.nextNode=nodeprox
    nodeant.nextNode=signode
    return cont