#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int c_board[5][5];
int max_a = 7;

int cids[25];
int c_go[5][5];
int now_g[7];

int o_vi[5][5];
int oc_n;
int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

int s_gn;

// 그룹인원끼리 연결하고 수로 확인한다.
void one_team(int vr, int vc)
{
    oc_n += 1;
    c_go[vr][vc] = 0;

    int to_r, to_c;
    for (int i = 0; i < 4; i++)
    {
        to_r = vr + dr[i];
        to_c = vc + dc[i];

        if (0 > to_r || 4 < to_r || 0 > to_c || 4 < to_c) continue;
        if (c_go[to_r][to_c] != 1) continue;
        
        one_team(to_r, to_c);
    }
}

// 7명씩 그룹이 만들어지는 경우이다.
// 조건1: 해당 그룹에서 4명 이상이 이다솜파인 경우를 고려한다.
// 조건2: 그룹이 한개로 뭉쳐있는지를 본다.
void g_check()
{
    bool som_g = true;
    memset(c_go, 0, sizeof(c_go));

    int to_r = 0;
    int to_c = 0;
    int s_num = 0;

    for (int i = 0; i < 7; i++)
    {
        to_r = now_g[i] / 5;
        to_c = now_g[i] % 5;

        c_go[to_r][to_c] = 1;
        if (c_board[to_r][to_c] == (int)'S')
        {
            s_num += 1;
        }
    }

    if (s_num < 4)
    {
        som_g = false;
        return;
    }

    int to_v = 0;
    oc_n = 0;

    to_r = now_g[0] / 5;
    to_c = now_g[0] % 5;
    if (c_go[to_r][to_c] != 0) {
        one_team(to_r, to_c);
    }

    if (oc_n != 7)
    {
        som_g = false;
    }

    if (som_g)
    {
        s_gn += 1;

    }
    return;
}

// 반 인원:25
// 그룹수 7
// 경우의수: 25C7 (40만)
void s_group(int a, int sid)
{
    if (a > max_a - 1)
    {
        g_check();
        return;
    }
    
    for (int i = sid; i < 25; i++)
    {
        now_g[a] = i;
        s_group(a + 1, i + 1);
    }

    return;
}

int main() {
    
    // 반 정보 입력 받기
    string in_st = "";
    for (int i = 0; i < 5; i++)
    {
        cin >> in_st;
        for (int j = 0; j < 5; j++)
        {
            c_board[i][j] = in_st[j];
        }
    }

    // 칠공주 그룹을 만들고 조건에 맞는지를 본다.
    // 조건에 맞으면 경우의 수를 더한다.
    s_group(0,0);
    cout << s_gn << endl;
    return 0;
};
