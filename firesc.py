import sys
sys.setrecursionlimit(10**8)
def fire_escape():

    n,m=map(int,input().split())
    graph={}

    for i in range(1,n+1):
        graph[i]=[]

    for i in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False]*(n+1)
    components=[]
    for i in range(1,n+1):
        if visited[i]==False:
            component=[]
            dfs(i,graph,component,visited)
            components.append(component)

    ways=1
    routes=len(components)
    mod=(10**9)+7
    for component in components:
        ways = (ways*len(component))%mod

    print(routes,ways)

def dfs(node,graph,component,visited):
    visited[node]=True
    component.append(node)
    for neighbour in graph[node]:
        if visited[neighbour]==False:
            dfs(neighbour,graph,component,visited)

t=int(input())
for loop in range(t):
    fire_escape()
            
