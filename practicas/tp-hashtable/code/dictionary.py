
class dictionaryNode:
    value=None
    key=None

def hash_table(m):
    tabla=[None]*m
    return tabla

def insert(D,key,value):
    hash=fun_hash(key,len(D))
    newNode=dictionaryNode()
    newNode.key=key
    newNode.value=value
    if D[hash]==None:
        L=[]
        L.append(newNode)
        D[hash]=L
    else:
        D[hash].append(newNode)
    return D 



def search(D,key):
    hash=fun_hash(key,len(D))
    if D[hash]==None: return None
    else:
        nodo=buscar_nodo(D[hash],key)
        if nodo==None: return None
        else: return nodo.value         




def delete(D,key):
    hash=fun_hash(key,len(D))
    if D[hash]==None: return None
    if len(D[hash])==1:
        if D[hash][0].key==key:
            D[hash]=None
        else: return None 
    else:
        nodo=buscar_nodo(D[hash],key)
        if nodo!=None:
            D[hash].remove(nodo)
        else: return None 
    return D



def fun_hash(key,m):
    return (key%m)


##busca el nodo de determiana de key en una lista y devuelve el nodo, en caso de no encontrarlo devuelve None 
def buscar_nodo(L,key):
    if L==None: return None
    for i in range (0,len(L)):
        if L[i].key==key: return L[i]
    return None 