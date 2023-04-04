from algo1 import *
from linkedlist import *

def enqueue (Q,element):
  add (Q,element)

def dequeue(Q):
  if Q.head==None:
    return
  else:
    nodeprox=Q.head
    nodeant=Q.head
    if nodeprox.nextNode==None:
      Q.head=None
      return nodeprox.value
    while nodeprox.nextNode!=None:
      nodeant=nodeprox
      nodeprox=nodeprox.nextNode
    nodeant.nextNode=None
    return nodeprox.value 