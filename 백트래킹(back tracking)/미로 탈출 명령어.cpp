#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <stdio.h>

using namespace std;

string s_path = "";
int m_k, sr, sc, er, ec, n, m;
bool can_go = true;
bool pa_find = false;

int dr[4] = { 1,0,0,-1 };
int dc[4] = { 0,-1,1,0 };
char pa_c[4] = { 'd','l','r','u', };

// 갈 수 있는 경로 중 사전 순으로 가장 빨라야 한다.
// d -> l -> r -> u 로 이동해 먼저 찾는 경로를 구한다.

void m_run(int r, int c, string pa, int ck) {
    if (pa_find)
    {
        return;
    }

    if (ck == m_k && r == er && c == ec)
    {
        s_path = pa;
        pa_find = true;
        return;
    }

    int nr, nc;

    // 목표 지점 까지의 거리가 남은 이동 수보다 커지는 경우
    // 가지치기를 해준다.
    if ((abs(r - er) + abs(c - ec)) > m_k - ck)
    {
        return;
    }

    for (int i = 0; i < 4; i++)
    {
        nr = r + dr[i];
        nc = c + dc[i];


        // k번의 이동수를 모두 소진한 경우
        // 가지치기
        if (1 > nr || n < nr || 1 > nc || m < nc) continue;
        if (ck + 1 > m_k) continue;

        m_run(nr,nc,pa + pa_c[i], ck + 1 );
    }
}

string solution(int a, int b, int x, int y, int r, int c, int k) {
    m_k = k;
    n = a;
    m = b;
    sr = x;
    sc = y;
    er = r;
    ec = c;

    // 목표 지점까지 갈수 없는 경우
    // :현재 - 목표까지의 거리가 이동가능 수보다 작다.
    if (abs(r - x) + abs(c - y) > k) {
        can_go = false;
    }

    // 현재 위치에서 목표위치까지 가고 남은 이동 수를 사용해도 갈 수 없는 경우
    // k만큼의 이동 수를 써야하므로 이동 수 - 목표까지의 거리가 홀 수 이면 갈 수 없다.
    if ((k - (abs(r - x) + abs(c - y))) % 2 != 0) {
        can_go = false;
    }

    // 현재위치부터 목표위치까지 고려하기
    if (can_go)
    {
        m_run(sr, sc, "", 0);
    }

    if (can_go)
    {
        return s_path;
    }
    else {
        return "impossible";
    }
}
