#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int n;
char forest[52][52];

struct t_no {
    int st;
    int d;
};

t_no vi[52][52][2];

struct q_no {
    int r;
    int c;
    int st;
};

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

// 처음 통나무 좌표, 상태
// 목표 통나무 좌표, 상태
int sr, sc, ss;
int er, ec, es;
int min_a = 21e8;

// 처음 나무를 목표 좌표까지 이동시킨다.
// 이 경우에서 나무는 누워있거나 서있다. --> 상태
// 고로, 경로중에서 어떤 상태인지를 기록했다.
// 또한 4가지 방향으로 이동하는 경우, 회전하는 경우에 맞게
// 다음 이동좌표와 장애물을 고려한다.
void t_go()
{
    queue<q_no> q = {};
    q.push({ sr,sc,ss });
    vi[sr][sc][ss].st = ss;
    vi[sr][sc][ss].d = 1;

    while (!q.empty())
    {
        q_no now = q.front();
        q.pop();
        
        // 목표에 도달한 경우이다.
        if (now.r == er && now.c == ec && now.st == es)
        {
            min_a = vi[now.r][now.c][now.st].d - 1;
            return;
        }
        int nr, nc, ns;

        // 네가지 방향으로 이동하는 경우
        for (int i = 0; i < 4; i++)
        {
            nr = now.r + dr[i];
            nc = now.c + dc[i];

            if (now.st == 0 && (0 > nr || n <= nr || 0 > nc || n - 2 <= nc)) continue;
            if (now.st == 1 && (0 > nr || n-2 <= nr || 0 > nc || n <= nc)) continue;

            bool c_go = true;
            if (now.st == 0)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (forest[nr][nc + j] == '1')
                    {
                        c_go = false;
                        break;
                    }
                }
            }
            else {

                for (int j = 0; j < 3; j++)
                {
                    if (forest[nr+j][nc] == '1')
                    {
                        c_go = false;
                        break;
                    }
                }
            }
            if (!c_go) continue;
            if (vi[nr][nc][now.st].d != 0) continue;
            
            q.push({ nr,nc,now.st });
            vi[nr][nc][now.st].d= vi[now.r][now.c][now.st].d + 1;
            vi[nr][nc][now.st].st = now.st;
        }

        // 회전하는 경우
        // 상태변화를 고려한다.

        // 가로  -> 세로
        if(now.st == 0)
        {
            nr = now.r - 1;
            nc = now.c + 1;

            if (now.st == 0 && (0 > nr || n - 2 <= nr || 0 > nc || n <= nc)) continue;
            
            bool c_go = true;
            for (int j = -1; j < 2; j++)
            {
                for (int k = 0; k < 3; k++)
                {
                    if (forest[nr + k][nc+j] == '1')
                    {
                        c_go = false;
                        break;
                    }

                }
            }
            if (!c_go) continue;

            if (vi[nr][nc][1].d != 0) continue;

            q.push({ nr,nc,1 });
            vi[nr][nc][1].d = vi[now.r][now.c][now.st].d + 1;
            vi[nr][nc][1].st= 1;

        }
        // 세로 --> 가로
        else {
            nr = now.r + 1;
            nc = now.c - 1;

            if (now.st == 1 && (0 > nr || n <= nr || 0 > nc || n - 2 <= nc)) continue;
            
            bool c_go = true;

            for (int j = -1; j < 2; j++)
            {
                for (int k = 0; k < 3; k++)
                {
                    if (forest[nr + j][nc + k] == '1')
                    {
                        c_go = false;
                        break;
                    }

                }
            }

            if (!c_go) continue;
            if (vi[nr][nc][0].d != 0) continue;

            q.push({ nr,nc,0 });
            vi[nr][nc][0].d= vi[now.r][now.c][now.st].d + 1;
            vi[nr][nc][0].st = 0;
        }
    }

    return;
}

int main() {
    cin >> n;
    
    // 처음과 목표 통나무 좌표 저장하기
    q_no b_tree[3];
    q_no e_tree[3];

    // 통나무와 숲의 정보를 입력받기
    int b_id = 0;
    int e_id = 0;
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < n; c++)
        {
            char tmp;
            cin >> tmp;

            if (tmp == 'B') {
                b_tree[b_id] = { r,c };
                b_id += 1;
                tmp = '0';
            }
            else if (tmp == 'E') {
                e_tree[e_id] = { r,c };
                e_id += 1;
                tmp = '0';
            }
            forest[r][c] = tmp;
            
        }
    }


    // 통나무의 처음 시작 좌표(r,c)와 상태(s)를 저장한다.
    // 상태 0: 가로, 1: 세로

    sr = b_tree[0].r;
    sc = b_tree[0].c;

    if (sr == b_tree[1].r)
    {
        ss = 0;
    }
    else {
        ss = 1;
    }

    // 통나무의 목표 시작 좌표(r,c)와 상태(s)를 저장한다.
    // 이는 나중에 나무의 이동시 좌표와 상태정보를 기반으로 목표까지 왔는지 판단할때 사용한다.
    // 또한, 탐색 과정에서의 경로에도 고려된다.
    er = e_tree[0].r;
    ec = e_tree[0].c;

    if (er == e_tree[1].r)
    {
        es = 0;
    }
    else {
        es = 1;
    }

    // 목표 위치까지 가는 최소 동작 수 구하기
    t_go();

    if (min_a == 21e8)
    {
        cout << 0 << endl;
    }
    else {
        cout << min_a << endl;
    }

    return 0;
}
