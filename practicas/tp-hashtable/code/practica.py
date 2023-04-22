from dictionary import*

### parte 2

###ejercicio 4


def permutaciones (S,P):
    D=[None]*27
    s_list=list(S)
    p_list=list(P)
    n_s=len(S)
    n_p=len(P)
    if n_s!=n_p: return False 
    for i in range (0,n_s):
        
        insert_permutaciones(D,ord(s_list[i]))
    

    for j in range (0,n_p):
        if search_permutaciones(D,ord(p_list[j]))==None: return False
    return True



###es un insert que en el campo value ingresa un una unidad y en caso de ingresar dos key iguales se suman
def insert_permutaciones (D,key):
    
    
    hash=fun_hash(key,len(D))

    newNode=dictionaryNode()
    newNode.key=key
    newNode.value=1

    if D[hash]==None:
        L=[]
        L.append(newNode)
        D[hash]=L
    else:
        nodo=buscar_nodo(D[hash],key)
        if nodo==None:
            D[hash].append(newNode)
        else:
            nodo.value+=1
    
    return D 



###busca el nodo de una key y en caso de encontrarlo le resta una unidad a su value, en el caso que sea cero el value, retorna none
def search_permutaciones(D,key):
    
    hash=fun_hash(key,len(D))
    if D[hash]==None: return None
    else:
        nodo=buscar_nodo(D[hash],key)
        if nodo==None: return None
        else: 
            if nodo.value>0:
                nodo.value-=1
                return nodo.value
            else:
                return None  

###ejercicio 5
def elementos_unicos(L):
    dic=[]
    for k in range (0,11):
        dic.append(None)
    
    n=len(L)
    for i in range(0,n):
        if search(dic,L[i])!=None:return False
        insert(dic,L[i],L[i])
    return True 


def primera_ocurrencia(S,P):
    D=hash_table(27)
    s_list=list(S)
    p_list=list(P)
    s_n=len(s_list)
    p_n=len(p_list)
    for i in range (0,s_n):
        key=ord(s_list[i])+ord(s_list[i+p_n])*100
        insert(D,key,i)
    


###ejercicio 7

def comprension (cadena):
    L=list(cadena)
    G=[]
    
    for i in range (0,len(L)):
        if i==0:
            G.append(L[0])
        else:
            if L[i]==L[i-1]:
                if G[-1]==L[i-1]:
                    G.append(2)
                else:
                    G[-1]+=1
            else:
                G.append(L[i])
    if len(G)==len(L):
        return cadena
    else:
        ca="".join(map(str,G))
        return ca 
    

###ejercicio 9
def subconjunto (S,T):
    D=[None]*27
    n_s=len(S)
    n_t=len(T)
    for i in range (0,n_t):
        
        insert_permutaciones(D,T[i])
    

    for j in range (0,n_s):
        if search_permutaciones(D,S[j])==None: return False
    return True


def subcadena (S,T):
    n=len(T)
    indice=0
    comprobante=False
    for i in range(0,n):
        print(T[i])
        if T[i]==S[indice]:
            #print(T[i])
            comprobante=True
            indice+=1
        else:
            comprobante=False
            indice=0
        if indice==len(S):
            return(i-indice+1)
        
