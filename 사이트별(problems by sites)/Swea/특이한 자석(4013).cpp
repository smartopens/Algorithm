#define _CRT_SECURE_NO_WARNINGS
#include <cstring>
#include <iostream>

using namespace std;

// 자석 선언
int n;
int magnetics[5][8];

int main() {
    int t = 0;
    int k = 0;

    cin >> t;
    for (int ti = 0; ti < t; ti++) {
        cin >> k;
        int scores = 0;

        // 자석 정보 입력
        for (int i = 1; i < 5; i++) {
            for (int j = 0; j < 8; j++) {
                cin >> magnetics[i][j];
            }
        }

        for (int ki = 0; ki < k; ki++) {

            // 회전 정보 
            int cycles[5] = {};
            int idx, c;
            cin >> idx >> c;

            // 자석 정보
            // 좌:6 우:2

            // 처음 자석 회전
            cycles[idx] = c;

            // 첫 자석 기준 우측 방향 회전 정보 갱신
            int ori_c = c;
            for (int i = idx; i < 4; i++) {
                if (magnetics[i][2] != magnetics[i + 1][6]) {
                    if (c == -1) {
                        cycles[i + 1] = 1;
                        c = 1;
                    }
                    else if (c == 1) {
                        cycles[i + 1] = -1;
                        c = -1;
                    }
                }
                else {
                    break;
                }
            }

            c = ori_c;

            // 첫 자석 기준 좌측 방향 회전 정보 갱신
            for (int i = idx; i > 1; i--) {
                if (magnetics[i][6] != magnetics[i - 1][2]) {
                    if (c == -1) {
                        cycles[i - 1] = 1;
                        c = 1;
                    }
                    else if (c == 1) {
                        cycles[i - 1] = -1;
                        c = -1;
                    }
                }
                else {
                    break;
                }
            }

            // 회전 정보에 맞게 자석들 회전시키기
            for (int i = 1; i < 5; i++) {
                // 시계 
                if (cycles[i] == -1) {
                    int tmp = magnetics[i][0];

                    for (int j = 0; j < 7; j++) {
                        magnetics[i][j] = magnetics[i][j + 1];
                    }
                    magnetics[i][7] = tmp;

                }
                // 반시계 
                else if (cycles[i] == 1) {
                    int tmp = magnetics[i][7];

                    for (int j = 7; j > 0; j--) {
                        magnetics[i][j] = magnetics[i][j - 1];
                    }
                    magnetics[i][0] = tmp;

                }
            }
        }

        // 최종 점수 계산
        for (int i = 1; i < 5; i++) {
            if (magnetics[i][0] == 1) {
                int score = 1;
                for (int j = 0; j < i - 1; j++) {
                    score *= 2;
                }
                scores += score;
            }
        }

        cout << "#" << ti+1 << " " << scores << endl;
    }

    return 0;
}
