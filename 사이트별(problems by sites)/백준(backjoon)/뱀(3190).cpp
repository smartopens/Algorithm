#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <queue>

using namespace std;

int n;
int k;
int a_n;
int forest[102][102];

int hr, hc;
int tr, tc;
int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

struct s_info {
    int t;
    char c_di;
};

struct s_p {
    int r;
    int c;
};

s_info coms[102];
queue<s_p> snake;

int main() {
    // 시간, 처음 방향
    int s_t = 0;
    int s_di = 1;

    // 초기 뱀 머리, 꼬리 위치
    hr = 1;
    hc = 1;
    tr = 1;
    tc = 1;

    cin >> n;

    // 숲의 가장자리 지역을 벽으로 지정한다.
    for (int r = 0; r < n + 2; r++)
    {
        forest[r][0] = -1;
        forest[r][n + 1] = -1;
    }

    for (int c = 0; c < n + 2; c++)
    {
        forest[0][c] = -1;
        forest[n + 1][c] = -1;
    }

    // 사과를 입력받는다.
    // 사과 : 2
    cin >> k;
    for (int i = 0; i < k; i++)
    {
        int r, c;
        cin >> r >> c;

        forest[r][c] = 2;
    }
    
    // 명령 정보(L: 좌측 회전, D:우측 회전) 입력 받기
    cin >> a_n;
    for (int i = 0; i < a_n; i++)
    {
        int c;
        char com;
        cin >> c >> com;
        coms[i] = { c,com };
    }

    // 뱀의 위치 정보를 queue에 저장한다.
    // 길이가 줄어들지 않는 경우 꼬리 부분만 제거해주면 된다.
    // FIRST IN FIRST OUT
    forest[hr][hc] = 1;
    snake.push({ hr,hc });

    // 다음 머리 위치 정보
    // 명령어 ID
    int n_hr, n_hc;
    int c_id = 0;

    // 시간이 흐른다.
    while (true)
    {
        n_hr = hr + dr[s_di];
        n_hc = hc + dc[s_di];
        
        bool a_eat = false;

        // 가장자리로 갔거나 본인 위치로 온 경우
        if (forest[n_hr][n_hc] == -1 || forest[n_hr][n_hc] == 1) {
            s_t += 1;
            break;
        }
        
        // 사과를 먹은 경우
        if (forest[n_hr][n_hc] == 2)
        {
            a_eat = true;
        }

        // 뱀이 앞으로 나아간다.
        forest[n_hr][n_hc] = 1;
        snake.push({ n_hr,n_hc });

        // 사과를 먹지 않은 경우
        // 뱀이 이동한다.
        // 길이가 줄어들지 않는다.
        if (a_eat == false)
        {
            s_p now = snake.front();
            snake.pop();

            tr = now.r;
            tc = now.c;
            forest[tr][tc] = 0;
        }

        // 명령 정보 시간에 다다를 경우
        // L:좌회전, D:우회전
        s_t += 1;
        if (coms[c_id].t == s_t)
        {
            if (coms[c_id].c_di == 'L')
            {
                s_di -= 1;
                if (s_di < 0)
                {
                    s_di = 3;
                }
            }
            else {
                s_di = (s_di + 1) % 4;
            }
            c_id += 1;
        }

        // 다음 위치 정보 갱신하기
        hr = n_hr;
        hc = n_hc;
    }
    
    cout << s_t << endl;
    return 0;
}
