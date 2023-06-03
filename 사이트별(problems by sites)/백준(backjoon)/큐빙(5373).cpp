#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string.h>

using namespace std;

// 기존 큐브 설정
char ori_cube[12][9] =
{
    {'0','0','0','w','w','w','0','0','0'},
    {'0','0','0','w','w','w','0','0','0'},
    {'0','0','0','w','w','w','0','0','0'},
    {'g','g','g','r','r','r','b','b','b'},
    {'g','g','g','r','r','r','b','b','b'},
    {'g','g','g','r','r','r','b','b','b'},
    {'0','0','0','y','y','y','0','0','0'},
    {'0','0','0','y','y','y','0','0','0'},
    {'0','0','0','y','y','y','0','0','0'},
    {'0','0','0','o','o','o','0','0','0'},
    {'0','0','0','o','o','o','0','0','0'},
    {'0','0','0','o','o','o','0','0','0'},

};

// test case마다 기존 큐브 정보 불러온다.
char cube[12][9];

void front_cycle(int sr, int sc) {

    char tmp_square[3][3] = { {} };

    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
            tmp_square[r][c] = cube[sr + r][sc + c];
        }
    }

    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
            cube[sr + r][sc + c] = tmp_square[2-c][r];
        }
    }

};

// 큐브 돌리기
// 면 정보, 방향 정보
void c_cycle(char com, char di) {
    // 윗면
    if (com == 'U') {
        if (di == '+') {
            // 바라보는 면 회전
            front_cycle(0, 3);

            // 옆면 회전
            // 큐브 왼편 정보 저장하기
            char tmp[3];
            for (int m1 = 0; m1 < 3; m1++) {
                tmp[2-m1] = cube[3][2-m1];
            }

            // 큐브 회전 시작
            // 왼편부터 시계방향 순으로 정보를 저장한다.
            for (int m1 = 0; m1 < 3; m1++) {
                cube[3][2-m1] = cube[3][5-m1];
            }

            for (int m1 = 0; m1 < 3; m1++) {
                cube[3][5 - m1] = cube[3][8-m1];
            }
            for (int m1 = 0; m1 < 3; m1++) {
                cube[3][8 - m1] = cube[11][3+m1];
            }

            // 마지막 방향 큐브는 처음 저장한 정보로 갱신한다.
            for (int m1 = 0; m1 < 3; m1++) {
                cube[11][3 + m1] = tmp[2-m1];
            }

        }
        else if (di == '-') {

            // 반시계 방향일 경우 시계방향 회전을 3번해준다.
            for (int i = 0; i < 3; i++) {
                // 바라보는 면 회전
                front_cycle(0, 3);

                // 옆면 회전
                // 큐브 왼편 정보 저장하기
                char tmp[3];
                for (int m1 = 0; m1 < 3; m1++) {
                    tmp[2 - m1] = cube[3][2 - m1];
                }
                // 큐브 회전 시작
                // 왼편부터 시계방향 순으로 정보를 저장한다.
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[3][2 - m1] = cube[3][5 - m1];
                }

                for (int m1 = 0; m1 < 3; m1++) {
                    cube[3][5 - m1] = cube[3][8 - m1];
                }
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[3][8 - m1] = cube[11][3 + m1];
                }

                // 마지막 방향 큐브는 처음 저장한 정보로 갱신한다.
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[11][3 + m1] = tmp[2 - m1];
                }
            }
        }
    }
    // 오른쪽 면
    else if (com == 'R') {
        if (di == '+') {
            // 바라보는 면 회전
            front_cycle(3, 6);

            // 옆면 회전
            // 큐브 왼편 정보 저장하기
            char tmp[3];
            
            for (int m1 = 0; m1 < 3; m1++) {
                tmp[2 - m1] = cube[5-m1][5];
            }

            // 큐브 회전 시작
            // 왼편부터 시계방향 순으로 정보를 저장한다.
            for (int m1 = 0; m1 < 3; m1++) {
                cube[5 - m1][5] = cube[8-m1][5];
            }

            for (int m1 = 0; m1 < 3; m1++) {
                cube[8 - m1][5] = cube[11-m1][5];
            }
            for (int m1 = 0; m1 < 3; m1++) {
                cube[11-m1][5] = cube[2-m1][5];
            }

            // 마지막 방향 큐브는 처음 저장한 정보로 갱신한다.
            for (int m1 = 0; m1 < 3; m1++) {
                cube[2 - m1][5] = tmp[2 - m1];
            }
        }
        else if (di == '-') {
            // 반시계 방향일 경우 시계방향 회전을 3번해준다.
            for (int i = 0; i < 3; i++) {
                // 바라보는 면 회전
                front_cycle(3, 6);
                // 옆면 회전
                // 큐브 왼편 정보 저장하기
                char tmp[3];
                for (int m1 = 0; m1 < 3; m1++) {
                    tmp[2 - m1] = cube[5 - m1][5];
                }
                // 큐브 회전 시작
                // 왼편부터 시계방향 순으로 정보를 저장한다.
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[5 - m1][5] = cube[8 - m1][5];
                }

                for (int m1 = 0; m1 < 3; m1++) {
                    cube[8 - m1][5] = cube[11 - m1][5];
                }
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[11 - m1][5] = cube[2 - m1][5];
                }

                // 마지막 방향 큐브는 처음 저장한 정보로 갱신한다.
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[2 - m1][5] = tmp[2 - m1];
                }
            }
        }
    }
    // 정면
    // 위의 로직들이 아래로직과 동일하다.
    // 자세한 주석 생략
    else if (com == 'F') {
        if (di == '+') {
            // 바라보는 면 회전
            front_cycle(3, 3);

            char tmp[3];
            // store
            for (int m1 = 0; m1 < 3; m1++) {
                tmp[2 - m1] = cube[5 - m1][2];
            }

            // cycle
            for (int m1 = 0; m1 < 3; m1++) {
                cube[5 - m1][2] = cube[6][5-m1];
            }

            for (int m1 = 0; m1 < 3; m1++) {
                cube[6][5 - m1] = cube[3 + m1][6];
            }
            for (int m1 = 0; m1 < 3; m1++) {
                cube[3 + m1][6] = cube[2][3 + m1];
            }

            for (int m1 = 0; m1 < 3; m1++) {
                cube[2][3 + m1] = tmp[2 - m1];
            }
        }
        else if (di == '-') {
            for (int i = 0; i < 3; i++) {
                // 바라보는 면 회전
                front_cycle(3, 3);

                char tmp[3];
                // store
                for (int m1 = 0; m1 < 3; m1++) {
                    tmp[2 - m1] = cube[5 - m1][2];
                }

                // cycle
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[5 - m1][2] = cube[6][5 - m1];
                }

                for (int m1 = 0; m1 < 3; m1++) {
                    cube[6][5 - m1] = cube[3 + m1][6];
                }
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[3 + m1][6] = cube[2][3 + m1];
                }

                for (int m1 = 0; m1 < 3; m1++) {
                    cube[2][3 + m1] = tmp[2 - m1];
                }
            }
        }
    }
    else if (com == 'L') {
        if (di == '+') {
            // 바라보는 면 회전
            front_cycle(3, 0);

            char tmp[3];
            // store
            for (int m1 = 0; m1 < 3; m1++) {
                tmp[2 - m1] = cube[9 + m1][3];
            }

            // cycle
            for (int m1 = 0; m1 < 3; m1++) {
                cube[9 + m1][3] = cube[6+m1][3];
            }

            for (int m1 = 0; m1 < 3; m1++) {
                cube[6 + m1][3] = cube[3 + m1][3];
            }
            for (int m1 = 0; m1 < 3; m1++) {
                cube[3 + m1][3] = cube[m1][3];
            }

            for (int m1 = 0; m1 < 3; m1++) {
                cube[m1][3] = tmp[2 - m1];
            }
        }
        else if (di == '-') {
            for (int i = 0; i < 3; i++) {
                // 바라보는 면 회전
                front_cycle(3, 0);

                char tmp[3];
                // store
                for (int m1 = 0; m1 < 3; m1++) {
                    tmp[2 - m1] = cube[9 + m1][3];
                }

                // cycle
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[9 + m1][3] = cube[6 + m1][3];
                }

                for (int m1 = 0; m1 < 3; m1++) {
                    cube[6 + m1][3] = cube[3 + m1][3];
                }
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[3 + m1][3] = cube[m1][3];
                }

                for (int m1 = 0; m1 < 3; m1++) {
                    cube[m1][3] = tmp[2 - m1];
                }
            }
        }
    }
    else if (com == 'D') {
        if (di == '+') {
            // 바라보는 면 회전
            front_cycle(6, 3);

            char tmp[3];
            // store
            for (int m1 = 0; m1 < 3; m1++) {
                tmp[2 - m1] = cube[5][m1];
            }

            // cycle
            for (int m1 = 0; m1 < 3; m1++) {
                cube[5][m1] = cube[9][5-m1];
            }

            for (int m1 = 0; m1 < 3; m1++) {
                cube[9][5 - m1] = cube[5][6+m1];
            }
            for (int m1 = 0; m1 < 3; m1++) {
                cube[5][6 + m1] = cube[5][3+m1];
            }

            for (int m1 = 0; m1 < 3; m1++) {
                cube[5][3 + m1] = tmp[2 - m1];
            }
        }
        else if (di == '-') {
            for (int i = 0; i < 3; i++) {
                // 바라보는 면 회전
                front_cycle(6, 3);

                char tmp[3];
                // store
                for (int m1 = 0; m1 < 3; m1++) {
                    tmp[2 - m1] = cube[5][m1];
                }

                // cycle
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[5][m1] = cube[9][5 - m1];
                }

                for (int m1 = 0; m1 < 3; m1++) {
                    cube[9][5 - m1] = cube[5][6 + m1];
                }
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[5][6 + m1] = cube[5][3 + m1];
                }

                for (int m1 = 0; m1 < 3; m1++) {
                    cube[5][3 + m1] = tmp[2 - m1];
                }

            }
        }
    }
    else if (com == 'B') {
        if (di == '+') {
            // 바라보는 면 회전
            front_cycle(9, 3);

            char tmp[3];
            // store
            for (int m1 = 0; m1 < 3; m1++) {
                tmp[2 - m1] = cube[3+m1][0];
            }

            // cycle
            for (int m1 = 0; m1 < 3; m1++) {
                cube[3 + m1][0] = cube[0][5 - m1];
            }

            for (int m1 = 0; m1 < 3; m1++) {
                cube[0][5 - m1] = cube[5 - m1][8];
            }
            for (int m1 = 0; m1 < 3; m1++) {
                cube[5 - m1][8] = cube[8][3 + m1];
            }

            for (int m1 = 0; m1 < 3; m1++) {
                cube[8][3 + m1] = tmp[2 - m1];
            }

        }
        else if (di == '-') {
            for (int i = 0; i < 3; i++) {
                // 바라보는 면 회전
                front_cycle(9, 3);

                char tmp[3];
                // store
                for (int m1 = 0; m1 < 3; m1++) {
                    tmp[2 - m1] = cube[3 + m1][0];
                }

                // cycle
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[3 + m1][0] = cube[0][5 - m1];
                }

                for (int m1 = 0; m1 < 3; m1++) {
                    cube[0][5 - m1] = cube[5 - m1][8];
                }
                for (int m1 = 0; m1 < 3; m1++) {
                    cube[5 - m1][8] = cube[8][3 + m1];
                }

                for (int m1 = 0; m1 < 3; m1++) {
                    cube[8][3 + m1] = tmp[2 - m1];
                }

            }
        }
    }
};

int main() {
    // test 수
    int t;
    cin >> t;

    // 큐브 돌리기 진행
    for (int tc = 0; tc < t; tc++) {
        int n;
        cin >> n;
        
        // 큐브 정보 초기화하기
        memcpy(cube, ori_cube, 12 * 9*sizeof(ori_cube[0][0]));

        // n번의 큐브 회전 정보 입력
        // 큐브를 돌린다.
        for (int i = 0; i < n; i++) {
            char orders[3] = "";
            cin >> orders[0];
            cin >> orders[1];

            c_cycle(orders[0], orders[1]);

        }

        // 윗면 큐브 보기
        for (int r = 0; r < 3; r++) {
            for (int c = 3; c < 6; c++) {
                cout << cube[r][c];
            }
            cout << endl;
        }

    }
    return 0;
}
