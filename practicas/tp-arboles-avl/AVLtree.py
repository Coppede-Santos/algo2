class AVLTree:
  root=None

class AVLNode:
  parent=None
  leftnode=None
  rightnode=None
  key=None
  Value=None
  bf=None
  h=None 

def rotateRight(Tree,avlnode):
  newRoot = avlnode.leftnode
  avlnode.leftnode = newRoot.rightnode

  if newRoot.rightnode != None:
    newRoot.rightnode.parent=avlnode
  newRoot.parent=avlnode.parent
  if avlnode.parent==None:
    Tree.root=newRoot
  else:
    if avlnode.parent.rightnode==avlnode:
      avlnode.parent.rightnode=newRoot
    else:
      avlnode.parent.leftnode=newRoot
  newRoot.rightnode=avlnode
  avlnode.parent=newRoot
  return 

def rotateLeft(Tree,avlnode):
  newRoot = avlnode.rightnode
  avlnode.rightnode = newRoot.leftnode

  if newRoot.leftnode != None:
    newRoot.leftnode.parent=avlnode
  newRoot.parent=avlnode.parent
  if avlnode.parent==None:
    Tree.root=newRoot
  else:
    if avlnode.parent.leftnode==avlnode:
      avlnode.parent.leftnode=newRoot
    else:
      avlnode.parent.rightnode=newRoot
  newRoot.leftnode=avlnode
  avlnode.parent=newRoot
  return 


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
  newNode=AVLNode()
  newNode.value=element
  newNode.key=key
  newNode.bf=0
  if B.root==None:
    B.root=newNode
    newNode.parent=B.root
  else:
    insertr(B.root,newNode)
  update_bf(newNode)

def calculateBalance(AVLTree):
  if AVLTree.root!=None:
    calculatebalancerec(AVLTree.root)

def calculatebalancerec(node):
  if node!=None:
    calculatebalancerec(node.leftnode)
    calculatebalancerec(node.rightnode)
    update_bf(node)

def update_bf(node):
  if node != None:
    if node.leftnode != None and node.rightnode != None:
      node.h = 1 + max(node.leftnode.h,node.rightnode.h)
    elif node.leftnode != None:
      node.h= 1 + node.leftnode.h
    elif node.rightnode != None:
      node.h = 1 + node.rightnode.h
    else:
      node.h=0

  calculate_bf(node)

  #if node.bf < -1 or node.bf >1:
    #rebalancenode(node)
  #else:
    #update_bf(node.parent)

def calculate_bf(node):
  if node.leftnode != None and node.rightnode != None:
    node.bf = node.leftnode.h - node.rightnode.h
  else:
    node.bf=node.h

def reBalance(AVLTree):
  if AVLTree.root==None: return
  calculateBalance(AVLTree)
  Balancerec(AVLTree.root,AVLTree)


def Balancerec(node,AVLTree):
  if node!=None:
    Balancerec(node.leftnode,AVLTree)
    Balancerec(node.rightnode,AVLTree)
    balance(node,AVLTree)



def balance(node,AVLTree):
  if node.bf<-1:
    if node.rigthnide.bf > 0:
      rotateRight(AVLNode,node.rightnode)
      rotateLeft(AVLNode,node)
    else:
      rotateLeft(AVLNode,node)
  elif node.bf > 1:
    if node.leftnode.bf<0:
      rotateLeft(AVLNode,node.leftnode)
      rotateRight(AVLNode,node)
    else:
      rotateRight(AVLNode,node)


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
    reBalance(B)
    return key
  if access(B,key)==None:
    reBalance(B)
    return
  else:
    current=buscar(B.root,key)
    deleter(current)
    reBalance(B)
    return key