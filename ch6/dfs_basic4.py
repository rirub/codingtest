import sys

def DFS(L,sum):
 # L : index 번호 ( 트리의 level을 뜻함. 트리의 레벨 별로 원소 유무 갈라짐 )
 # L 인덱스에 원소를 사용하면 sum에 인덱스 값을 더해주기
    if sum>total//2:
        return
    if L == n:
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
            # 프로그램 전체 종료
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a)
    DFS(0,0)
    print("NO")