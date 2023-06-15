import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

if __name__=="__main__":
    n,m,k,x = map(int,input().split())
    graph = [ [] for _ in range(n+1)]
    distance = [INF]*(n+1)
    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append((b,1))
    dijkstra(x)
    if not k in distance:
        print(-1)
    else:
        for idx, val in enumerate(distance):
            if val==k:
                print(idx)
