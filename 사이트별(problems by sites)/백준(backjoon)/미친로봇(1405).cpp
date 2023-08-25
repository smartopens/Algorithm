#define _CRT_SECURE_NO_WARNINGS

#include <iostream>

using namespace std;

int n;
double ep, wp, sp, np;
double mps[4];
double p_sum;

int vi[30][30];
int dr[4] = { 0,0,1,-1 };
int dc[4] = { 1,-1,0,0 };

// 로봇이 n번이동한다.
// 이동이 완료되면 그동안 경로의 확률을 더한다.
// 한번 이동한 경로는 이동하지 않게 한다.
void r_move(int a, int r, int c, double now_p)
{
    if (a > n-1)
    {
        p_sum += now_p;
        return;
    }

    int nr, nc;
    for (int i = 0; i < 4; i++)
    {
        nr = r + dr[i];
        nc = c + dc[i];

        if (vi[nr][nc] != 0) continue;

        vi[nr][nc] = 1;
        r_move(a + 1, nr, nc, now_p * mps[i]);
        vi[nr][nc] = 0;
    }

    return;
}

int main() {
    cin >> n;
    // 상대오차: 10-9까지 허용
    cout << fixed;
    cout.precision(9);

    // 로봇의 이동확률 입력받기
    // 동 서 남 북
    double in_p;
    for (int i = 0; i < 4; i++)
    {
        cin >> in_p;
        mps[i] = in_p / 100;
    }

    // 로봇 이동경로 기록
    vi[14][14] = 1;
    r_move(0, 14, 14, 1);

    cout << p_sum << endl;
    return 0;
};
