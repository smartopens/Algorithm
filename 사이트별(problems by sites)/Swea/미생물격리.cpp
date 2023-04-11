#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

// 상 하 좌 우
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };
int c_di[4] = {1, 0, 3, 2 };

int n;
int m;
int k;
int tc;
int cnt;

// num: 미생물 수, di: 미생물 방향
struct Node {
    int num = 0;
    int di = 0;
};

int main() {

    cin >> tc;
     
    for (int t = 0; t < tc; t++) {
        cin >> n >> m >> k;
        Node board[100][100] = { {} };
        cnt = 0;

        // 미생물 입력
        // Node: 미생물 수, 방향
        for (int i = 0; i < k; i++) {
            int r, c, num, di;
            cin >> r >> c >> num >> di;
            Node tmp;
            tmp.num = num;
            tmp.di = di-1;
            board[r][c] = tmp;
        }

           
        while (m > 0) {
            // 미생물 중 가장 군집이 큰 미생물 방향을 위해 max_cnt 사용
            Node new_board[100][100]= {{}};
            int max_cnt[100][100] = {{}};

            // 미생물 탐색
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {

                    if (board[r][c].num == 0) continue;

                    // 미생물 이동 설정
                    int nr, nc, di;
                    di = board[r][c].di;
                    nr = r + dr[di];
                    nc = c + dc[di];

                    // 가지치기
                    if (0 > nr || nr >= n || 0 > nc || nc >= n) continue;

                    // 미생물 방향 설정
                    // 미생물들이 한곳에 모일 경우
                    if (max_cnt[nr][nc] > 0) {
                        int new_di = new_board[nr][nc].di;
                        if (max_cnt[nr][nc] < board[r][c].num)
                        {
                            new_di = board[r][c].di;
                            max_cnt[nr][nc] = board[r][c].num;
                        }


                        new_board[nr][nc].num += board[r][c].num;
                        new_board[nr][nc].di = new_di;
                        continue;
                    }

                    // 빨간 영역에 가는 경우
                    if (0 == nr || nr == n - 1 || 0 == nc || nc == n - 1)
                    {
                        int new_num = board[r][c].num / 2;
                        if (new_num == 0) continue;
                        new_board[nr][nc].num = new_num;
                        new_board[nr][nc].di = c_di[board[r][c].di];
                        continue;
                    }

                    // 미생물이 빈 영역으로 가는 경우
                    new_board[nr][nc].num = board[r][c].num;
                    max_cnt[nr][nc] = board[r][c].num;
                    new_board[nr][nc].di = board[r][c].di;

                }
                
            }
            // 미생물 이동 후 배열 설정
            copy(&new_board[0][0], &new_board[0][0] + 100*100, &board[0][0]);
            m -= 1;
        }

        // 미생물 수 세기
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                cnt += board[r][c].num;
            }
        }
        cout << "#" << t+1 << " " << cnt << endl;

    }


    return 0;
}
