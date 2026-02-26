import sys
import copy

input = sys.stdin.readline

N = int(input())
board = [list(input().split()) for _ in range(N)]

teachers = []
for i in range(N):
    for j in range(N):
        if board[i][j] == "T":
            teachers.append([i,j])
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = False

def bfs():
    for teacher in teachers:
        for i in range(4):
            nx, ny = teacher
            while 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == "O":
                    break
                
                if board[nx][ny] == "S":
                    return False
                
                nx += dx[i]
                ny += dy[i]
    return True


def wall(count):
    global answer
    
    if count == 3:
        if bfs():
            answer = True
        return
    
    else:
        for i in range(N):
            for j in range(N):
                if board[i][j] == "X":
                    board[i][j] = "O"
                    wall(count+1)
                    board[i][j] = "X"
                
wall(0)
if answer:
    print("YES")
else:
    print("NO")