#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int k;
int w, h;
int forest[202][202];
int vi[202][202][32] = {};

int dr[12] = { -2,-1,1,2,2,1,-1,-2 ,-1,0,1,0};
int dc[12] = { 1,2,2,1,-1,-2,-2,-1,0,1,0,-1 };

bool possible = false;
int min_a = 21e8;

struct node {
    int r;
    int c;
    int pk;
};

// 원숭이는 말 점프와 보통 이동을 할 수 있다.
// bfs 특성 상 최소 경로 지점을 찾을 수 있다.
// 다만, 말 점프의 경우 어느 지점에서 하는 것이 최적인지 알기 힘들다.
// 고로, 방문기록에서 말 점프의 경우를 추가한다.
// 특정 위치에서 말 점프를 몇번했는지를 기록하기 때문에 말점프와 보통점프의 여러 조합을 고려할 수 있다.
void bfs(int r, int c)
{
    vi[r][c][0] = 1;
    queue<node> q = {};
    q.push({ r,c,0 });

    while (!q.empty())
    {
        node now = q.front();
        q.pop();

        int r, c;
        r = now.r;
        c = now.c;

        if (r == h - 1 && c == w - 1)
        {
            min_a = vi[now.r][now.c][now.pk] - 1;
            possible = true;
            return;
        }
        int nr, nc, npk;
        for (int i = 0; i < 12; i++)
        {
            nr = r + dr[i];
            nc = c + dc[i];

            // 말 점프를 하는 경우
            if (0 <= i && i < 8)
            {
                if (0 > nr || h - 1 < nr || 0 > nc || w - 1 < nc) continue;
                if (forest[nr][nc] == 1) continue;
                if (now.pk >= k) continue;
                if (vi[nr][nc][now.pk+1] != 0) continue;

                vi[nr][nc][now.pk + 1] = vi[r][c][now.pk] + 1;
                q.push({ nr,nc, now.pk + 1 });
            }
            // 그냥 점프를 하는 경우
            else {
                if (0 > nr || h - 1 < nr || 0 > nc || w - 1 < nc) continue;
                if (forest[nr][nc] == 1) continue;
                if (vi[nr][nc][now.pk] != 0) continue;

                vi[nr][nc][now.pk] = vi[r][c][now.pk] + 1;
                q.push({ nr,nc, now.pk});
            }
        }
    }
}

int main() {
    // 말 점프 가능 횟수: k
    // 격자 세로, 가로: h, w
    cin >> k;
    cin >> w >> h;

    // 보드 정보 입력 받기
    for (int r = 0; r < h; r++)
    {
        for (int c = 0; c < w; c++)
        {
            cin >> forest[r][c];
        }
    }

    // 원숭이가 출발한다.
    // 도착 지점 h-1, w-1까지의 최소 경로를 구한다.
    bfs(0, 0);

    // 도착할 수 없다면 -1, 
    // 가능하면 최소 경로 출력
    if (possible == false)
    {
        cout << -1 << endl;
    }
    else {

        cout << min_a << endl;
    }
    return 0;
}
