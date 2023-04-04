from algo1 import *
import linkedlist 
from myqueue import * 

class LinkedList:
  head=None

class Node:
  value=None
  nextNode=None

  
class BinaryTree:
  root=None

class BinaryTreeNode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None


#insert rescursivo  
def insertr(currentNode,newNode):
  if newNode.key<currentNode.key:
    if currentNode.leftnode==None:
      currentNode.leftnode=newNode
      newNode.parent=currentNode
    else:
      insertr(currentNode.leftnode,newNode)
  else:
    if currentNode.rightnode==None:
      currentNode.rightnode=newNode
      newNode.parent=currentNode
    else:
      insertr(currentNode.rightnode,newNode)


#insert final 
def insert(B,element,key):
  newNode=BinaryTreeNode()
  newNode.value=element
  newNode.key=key
  if B.root==None:
    B.root=newNode
    newNode.parent=B.root
  else:
    insertr(B.root,newNode)

    
#search recursivo 
def searchr(current,ele):
  if current==None:
    return 
  if current.value==ele:
    return current
  if current.rightnode!=None:
    rigth=searchr(current.rightnode,ele)
    if rigth!=None:
      return rigth
  if current.leftnode!=None:
    left=searchr(current.leftnode,ele)
    if left!=None:
      return left
      
#search final 
def search(B,element):
  if B.root==None:
    return
  else:
    node=searchr(B.root,element)
    if node==None:
      return
    else:
      return node.key

#devuelve el nodo menor de una rama
def menor(current):
  if current.leftnode==None:
    return current
  else:
    return menor(current.leftnode)

#devuelve el nodo de la key dada 
def buscar(current,key):
  if current==None: return 
    
  if current.key==key:
    return current
  elif current.key>key:
    return buscar(current.leftnode,key)
  else:
    return buscar(current.rightnode,key)
#reemplaza el nodo dado por algo
def remplazar(node,rempla):
  if node.parent.leftnode==node:
    if rempla!=None:
      deleter(rempla)
      rempla.leftnode=node.leftnode
      rempla.rightnode=node.rightnode
    node.parent.leftnode=rempla
  if node.parent.rightnode==node:
    if rempla!=None:
      deleter(rempla)
      rempla.leftnode=node.leftnode
      rempla.rightnode=node.rightnode
    node.parent.rightnode=rempla
    

def deleter(node):
  if node.rightnode==None:
    #eliminar una hoja
    if node.leftnode==None:
      remplazar(node,None)
      return 
    #eliminar un nodo con una sola rama
    else:
      remplazar(node,node.leftnode)
      return
  else:
    #eliminar un nodo con una sola ramaa
    if node.leftnode==None:
      remplazar(node,node.rightnode)
      return
    else:
      remplazar(node,menor(node.rightnode))
      return


def delete(B,element):
  if B.root==None:
    return
  if B.root.value==element:
    key=B.root.key
    node=menor(B.root.rightnode)
    remplazar(node,None)
    node.leftnode=B.root.leftnode
    node.rightnode=B.root.rightnode
    B.root=node
    return key
  key=search(B,element)
  if key==None:
    return
  else:
    current=buscar(B.root,key)
    deleter(current)
    return key 
def deleteKey(B,key):
  if B.root==None:
    return 
  if B.root.key==key:
    node=menor(B.root.rightnode)
    remplazar(node,None)
    node.leftnode=B.root.leftnode
    node.rightnode=B.root.rightnode
    B.root=node
    return key
  if access(B,key)==None:
    return
  else:
    current=buscar(B.root,key)
    deleter(current)
    return key
  

def access (B,key):
  if B.root==None:
    return
  current=buscar(B.root,key)
  if current!=None:
    return current.value


def update(B,element,key):
  if B.root == None:
    return
  current=buscar(B.root,key)
  if current!=None:
    current.value=element
    return current.key 

####Ejercicios 2#####
def orden_inverso(L):
  final=linkedlist.length(L)
  cont=0
  for i in range (0,final):
    val=L.head.value
    linkedlist.insert(L,val,final-cont)
    L.head=L.head.nextNode
    cont+=1

def traverseInOrder(B):
  L=LinkedList()
  inorden(B.root,L)
  return L


def inorden(current,L):
  if current!=None:
    inorden(current.rightnode,L)
    linkedlist.add(L,current.value)
    inorden(current.leftnode,L)

def traverseInPreOrder(B):
  L=LinkedList()
  preorden(B.root,L)
  orden_inverso(L)
  return L
  
def preorden(current,L):
  if current!=None:
    linkedlist.add(L,current.value)
    preorden(current.leftnode,L)
    preorden(current.rightnode,L)

def traverseInPostOrder(B):
  L=LinkedList()
  posorden(B.root,L)
  orden_inverso(L)
  return L

def posorden(current,L):
  if current!=None:
    posorden(current.leftnode,L)
    posorden(current.rightnode,L)
    linkedlist.add(L,current.value)


def traverseBreadFirst(B):
  L=linkedlist()
  cola=linkedlist()
  enqueue(cola,B.root)
  while cola.head != None:
    a=dequeue(cola)
    linkedlist.add(L,a)
    if a.rightnode!=None:
      enqueue(cola,a.rightnode)
    if a.leftnode!=None:
      enqueue(cola,a.leftnode)
  return orden_inverso(L)





  