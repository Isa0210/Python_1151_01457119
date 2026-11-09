H,W= input().split()
H= int(H)
W= int(W)
maze= [list(input()) for i in range(0,H)]
mem = [[0 for i in range(0,W)] for j in range(0,H)]
dir= [(0,1),(0,-1),(-1,0),(1,0)]
ny,nx=0,0
queue=list()
queue.append((ny,nx,0))
while True:
    if not len(queue):
            print(-1)
            break
    ny,nx,step=queue.pop(0)
    if maze[ny][nx]=='T':
        print(step)
        break
    for dy, dx in dir:
        if 0<=ny+dy<H and 0<=nx+dx<W and maze[ny+dy][nx+dx]!='#' and mem[ny+dy][nx+dx]==0:
            queue.append((ny+dy,nx+dx,step+1))
            mem[ny+dy][nx+dx]=1
