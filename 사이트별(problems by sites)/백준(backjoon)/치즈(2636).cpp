#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

int n, m;
int board[102][102];
int b_air[102][102];

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };
int vi[102][102];

int t_time;

struct node {
    int r;
    int c;
};

// 공기구역:치즈에 둘러쌓인 공기로 이루어진 구역

// 치즈 그룹들을 살핀다.
// 동시에 치즈이면서 다음 방문 공간이 공기구역이 아닌 공기라면 기록한다.
void m_chesse(int sr, int sc)
{

    queue<node> q = {};
    q.push({ sr,sc });

    vi[sr][sc] = 1;

    while (!q.empty())
    {
        node now = q.front();
        q.pop();

        int nr, nc;
        for (int i = 0; i < 4; i++)
        {
            nr = now.r + dr[i];
            nc = now.c + dc[i];

            if (0 > nr || n - 1 < nr || 0 > nc || m - 1 < nc) continue;
            if (vi[nr][nc] != 0) continue;

            // 치즈이면서 다음 방문 공간이 공기구역이 아닌 공기이다.
            if (board[nr][nc] == 0 && b_air[nr][nc] == 0) {
                vi[now.r][now.c] = 2;
            }
            if (board[nr][nc] == 0) continue;

            vi[nr][nc] = 1;
            q.push({ nr,nc });

        }
    }

}

// 녹는 치즈 블록을 기록한다.
void f_chesse()
{
    memset(vi, 0, sizeof(vi));
    for (int r = 1; r < n - 1; r++)
    {
        for (int c = 1; c < m - 1; c++)
        {
            if (vi[r][c] != 0) continue;
            if (board[r][c] == 0) continue;
            m_chesse(r, c);
        }
    }
    return;
};

// 공기 구역 기록하기
// 가장자리로 갈 수 있다면 공기 구역이 아니다.
// 공기 구역이라면 b_air에 기록한다.
void a_record(int sr, int sc)
{
    queue<node> q = {};
    q.push({ sr,sc });

    queue<node> tmp = {};
    tmp.push({ sr,sc });

    vi[sr][sc] = 1;
    bool is_air = true;

    while (!q.empty())
    {
        node now = q.front();
        q.pop();

        int nr, nc;
        for (int i = 0; i < 4; i++)
        {
            nr = now.r + dr[i];
            nc = now.c + dc[i];

            // 가장자리로 올 수 있다면 공기 구역이 아니다.
            if (0 == nr || n <= nr - 1 || 0 == nc || m == nc - 1)
            {
                is_air = false;
            }
            if (0 > nr || n - 1 < nr || 0 > nc || m - 1 < nc) continue;
            if (board[nr][nc] == 1) continue;
            if (vi[nr][nc] != 0) continue;

            vi[nr][nc] = 1;
            tmp.push({ nr,nc });
            q.push({ nr,nc });

        }
    }

    // 공기구역이라면 b_air에 기록하기
    if (is_air == true)
    {
        while (!tmp.empty())
        {
            node now = tmp.front();
            tmp.pop();
            b_air[now.r][now.c] = 1;
        }
    }
    return;
}

// 치즈로 쌓여진 공기 구역 찾기
// 치즈가 아닌 구역을 기준으로 찾는다.
void a_find()
{
    memset(vi, 0, sizeof(vi));
    memset(b_air, 0, sizeof(b_air));
    for (int r = 1; r < n-1; r++)
    {
        for (int c = 1; c < m-1; c++)
        {
            if (vi[r][c] != 0) continue;
            if (board[r][c] == 1) continue;
            a_record(r,c);
        }
    }
    return;
}
int main() {
    cin >> n >> m;

    // 치즈 정보 입력받기
    // 가장자리는 치즈가 올 수 없다.
    // 치즈블록 개수 세기
    int t_chesse = 0;
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            cin >> board[r][c];
            if (board[r][c] == 1)
            {
                t_chesse += 1;
            }
        }
    }

    // 녹은 후 치즈 정보 기록
    int now_chesse = 0;
    while (t_chesse > 0)
    {
        // 치즈로 쌓여진 구역 찾기
        a_find();
        now_chesse = t_chesse;

        // 녹여야하는 치즈 구역 찾기
        // vi에 2로 기록한다.
        f_chesse();

        // 위에서 찾은 치즈를 녹이고 전체 치즈 개수를 갱신한다.
        for (int r = 1; r < n - 1; r++)
        {
            for (int c = 1; c < m - 1; c++)
            {
                if (vi[r][c] == 2)
                {
                    board[r][c] = 0;
                    t_chesse -= 1;
                }
            }
        }
        t_time += 1;
    }

    // 전체 시간, 모두 녹기 전 치즈 개수 출력
    cout << t_time << endl;
    cout << now_chesse << endl;
    return 0;
}
