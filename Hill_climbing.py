#-------------------skip---------------------- 
hf = {
    'A':12,
    'B':4,
    'C':7,
    'D':3,
    'E':8,
    'F':2,
    'H':4,
    'I':9,
    'S':13,
    'G':0
}
graph = {
    'S': ['A','B'],
    'A': ['C','D'],
    'C':[],
    'D':[],
    'B':['E','F'],
    'E':['H'],
    'F':['I','G'],
    'H':[],
    'I':[],
    'G':[]

}

path = []
def BestFirstSearch(graph,hf,start):
    siblings = []
    open = []
    close = set()
   
    open.append(start)
    while open!=[]:
        print(1)
        n=open.pop()
        path.append(n)
        close.add(n)
        for i in graph[n]:
            siblings.append(i)
        min = 999
        global min_sib
        if min_sib ==[]:
            break
        for sn in siblings:
            if min>hf[sn]:
                min=hf[sn]
                min_sib = sn
        
        open.append(min_sib)
        

    

BestFirstSearch(graph,hf,'S')

for i in path:
    print(i,end='->')





