



class Trie:
  root=None 

class TrieNode:
  parent=None
  children=None
  key=None
  isEndOfWord=False

def insert(T,element):
  lista=list(element)
  if T.root==None:
    L=[]
    T.root=L
    insert_recursivo(L,T,lista)
  else:
    insert_recursivo(T.root,T,lista)

#insert rescursivo,
def insert_recursivo (L,parent,element):
  if not L:
    newnode=TrieNode()
    newnode.key=element[0]
    del element[0]
    newnode.parent=parent
    L.append(newnode)
    if element:
      Lista=[]
      newnode.children=Lista
      insert_recursivo(Lista,newnode,element)
      return 
    else:
      newnode.isEndOfWord=True
      return

  posicion=buscar_node(L,element[0])
  if posicion==None:
    newnode=TrieNode()
    newnode.key=element[0]
    del element[0]
    newnode.parent=parent
    L.append(newnode)
    if element:
      Lista=[]
      newnode.children=Lista
      insert_recursivo(Lista,newnode,element)
      return 
    else:
      newnode.isEndOfWord=True
      return
  else:
    if len(element)==1:
      L[posicion].isEndOfWord=True
    elif L[posicion].isEndOfWord==True:
      Lis=[]
      L[posicion].children=Lis
      del element[0]
      insert_recursivo(L[posicion].children,L[posicion],element)
    else:
      del element[0]
      insert_recursivo(L[posicion].children,L[posicion],element)
  
  
  
  ###buscar la key de un nodo, dentro de una lista de nodos. devuelve la posicion en la lista
def buscar_node(L,key):
  for i in range (0,len(L)):
    if L[i].key==key:
      return i
  return None 

def search(T,element):
  if T.root==None: return False
  lista=list(element)
  return search_recursivo(T.root,lista)
  


###search recursivo
def search_recursivo(L,element):
  indice=buscar_node(L,element[0])
  #en caso de que no se encuentre la letra con la que sigue la palabra en la lista, es False
  if indice==None:
    return False
  else:
    del element[0]
    if element:
      if L[indice].children==None:
        ##en caso de que la palabra tenga más letras pero el node no tenga más hijos, es False
        return False
      else:
        ##en caso de que a la palabra le queden letras y el node tenga hijos, se sigue buscando
        return search_recursivo(L[indice].children,element)
    else:
      #si la palabra se termino, se evalua si el nodo marca un EndOfWord
      if L[indice].isEndOfWord: return True
      else: return False 

def delete(T,element):
  if search(T,element):
    lista=list(element)
    
    delete_recursivo(T,lista,ultimo_node_recursivo(T.root,lista),0)
    return True
  else: return False 
  

###delete recursivo, recibe el trie,una lista con las letras que faltan borrar, el ultimo node, y el numero de iteraciones que se han echo 


def delete_recursivo(T,element,node,i):
  if node.children!=None:
    if len(element)==i:
      node.isEndOfWord=False
    
      return
    else:
      
      return
  else:
    if node.isEndOfWord==True and i!=0:
      
      return
    else:  
      element.pop
      newnode=node.parent
      if newnode==T:
        if len(T.root)==1:
          T.root=None
          return
        else:
          T.root.remove(node)
          
          return
      else:  
        if len(newnode.children)==1:
          newnode.children=None
          
        else:
          newnode.children.remove(node)
          
        delete_recursivo(T,element,newnode,i+1)
      
  


##devuelve el ultimo nodo de una palabra, en un trie
def ultimo_node_recursivo(L,element):
  caracter=element.pop(0)
  indice=buscar_node(L,caracter)
  if element:
    return ultimo_node_recursivo(L[indice].children,element)
  else:  
    return L[indice]


##ejercicio 4:
def palabra_p_n(T,p,n):
  pre=list(p)
  m=n-len(pre)
  current_lista=T.root
  if len(pre)==n:
    if search(T,p):
      print(pre)
    return
  while pre:
    current_letra=pre.pop(0)
    indice=buscar_node(current_lista,current_letra)
    current_lista=current_lista[indice].children
    if indice==None or current_lista==None:
      return
  
  for i in range(0,len(current_lista)):
  
    palabra_p_n_recursivo(T,current_lista[i],m,0)




def palabra_p_n_recursivo (T,node,n,i):
  if n==1:
    if node.isEndOfWord==True:
      L=[]
      while node!=T:
        L.insert(0,node.key)
        node=node.parent
      print(L)
    return
    
  if i==n-2:
    if node.children!=None:
      for j in range(0,len(node.children)):
        
        if node.children[j].isEndOfWord:
          current=node.children[j]
          L=[]
          while current!=T:
            L.insert(0,current.key)
            current=current.parent
          print(L)
          
      return

    else:
      return
  else:
    if node.children==None:
      return
    else:
      for k in range (0,len(node.children)):
        palabra_p_n_recursivo(T,node.children[k],n,i+1)
  



##ejercicio 5:
##orden de complejidad O(n^2)

def sub_arbol(T1,T2):
  if T1.root==None and T2.root==None:
    return True
  if T1.root==None or T2.root==None:
    return False
  return(sub_arbol_recursivo(T1.root,T2.root))



def sub_arbol_recursivo(La,Lb):
  if La and not Lb: return False
  if not La and not Lb: return True
    
  for i in range (0,len(La)):
    indice=buscar_node(Lb,La[i].key)
    if indice==None:
      
      return False
    else:
      if La[i].isEndOfWord==True and Lb[indice]==False:
        return False
      elif La[i].children!=None:
        if Lb[indice].children==None:
          return False
        else:
          if sub_arbol_recursivo(La[i].children,Lb[indice].children)==False: return False
  return True
      



###ejercicio 6:


def cadena_invertida(T):
  if not T.root: return False
  return cadena_invertida_rec(T,T.root)




def cadena_invertida_rec(T,L):
  for i in range (0,len(L)):
    if L[i].isEndOfWord:
      current=L[i]
      palabra=[]
      while current!=T:
        palabra.append(current.key)
        current=current.parent
      stri="".join(palabra)
      #print(palabra)
      if search(T,stri):
        return True
    else:
      if cadena_invertida_rec(T,L[i].children):
        return True
  return False




###ejercicio 7:


def autocompletado(T,p):
  pre=list(p)
  
  current_lista=T.root

  while pre:
    current_letra=pre.pop(0)
    indice=buscar_node(current_lista,current_letra)
    current_lista=current_lista[indice].children
    if indice==None or current_lista==None:
      return
  node=current_lista[indice].parent

  autocompletado_rec(T,current_lista,node)



def autocompletado_rec (T,L,node):
  for i in range (0,len(L)):
    if L[i].isEndOfWord:
      current=L[i]
      lista=[]
      while current!=node:
        lista.insert(0,current.key)
        current=current.parent
      print(lista)
    if L[i].children!=None:
      autocompletado_rec(T,L[i].children,node)
  
  