#define _CRT_SECURE_NO_WARNINGS

#include <cstring>
#include <cctype>
#include <iostream>

using namespace std;

int n;
int ground[20][20];
int visited[20][20];
int x;

// 활주로 가능 영역 탐색
int count_road() {
    int p_path = 0;

    // 가로 방향 탐색
    for (int r = 0; r < n; r++) {
        bool can_build = true;

        for (int c = 0; c < n - 1; c++) {
            // 높이 차이가 1이상인 경우
            if (abs(ground[r][c] - ground[r][c + 1]) > 1) {
                can_build = false;
                break;
            }
            // 높이 차이가 1일 경우
            else if (abs(ground[r][c] - ground[r][c + 1]) == 1) {
                // 현재 위치기준 앞 지대 높이가 더 클경우
                if (ground[r][c] < ground[r][c + 1]) {
                    // 지대를 넘어가는지 판단
                    if (0 > c - x + 1) {
                        can_build = false;
                        break;
                    }

                    // 경사로 짓는 공간 판단
                    // 1. 지금 위치와 높이가 같은지를 본다.
                    // 2. 이전에 경사로를 설치했는지를 확인한다.
                    for (int xi = 0; xi < x; xi++) {
                        if (ground[r][c] != ground[r][c-xi] || visited[r][c - xi] == 1)
                        {
                            can_build = false;
                            break;
                        }
                    }

                    // 경사로 기록
                    for (int xi = 0; xi < x; xi++) {
                        visited[r][c - xi] = 1;
                    }
                }

                // 지금 위치기준 앞 지대 높이가 더 작을 경우
                else if (ground[r][c] > ground[r][c + 1]) {
                    // 지대를 넘어가는지 판단
                    if (c + x > n - 1) {
                        can_build = false;
                        break;
                    }

                    // 경사로 짓는 공간 판단
                    // 1. 지금 위치와 높이가 같은지를 본다.
                    for (int xi = 1; xi < x; xi++) {
                        if (ground[r][c+1] != ground[r][c + 1 + xi])
                        {
                            can_build = false;
                            break;
                        }
                    }

                    // 경사로 기록
                    for (int xi = 0; xi < x; xi++) {
                        visited[r][c +1+ xi] = 1;
                    }
                }

            }
            // 그냥 가는 경우
        }
        if (can_build == true) {
            p_path += 1;

        }
    }

    memset(visited, 0, sizeof(visited));

    // 세로 방향 탐색
    for (int c = 0; c < n; c++) {
        bool can_build = true;

        for (int r = 0; r < n - 1; r++) {
            // 높이 차이가 1이상인 경우
            if (abs(ground[r][c] - ground[r+1][c]) > 1) {
                can_build = false;
                break;
            }
            // 높이 차이가 1일 경우
            else if (abs(ground[r][c] - ground[r+1][c]) == 1) {
                if (ground[r][c] < ground[r+1][c]) {
                    // 지대를 넘어가는지 판단
                    if (0 > r - x + 1) {
                        can_build = false;
                        break;
                    }

                    // 경사로 짓는 공간 판단
                    // 1. 지금 위치와 높이가 같은지를 본다.
                    // 2. 이전에 경사로를 설치했는지를 확인한다.
                    for (int xi = 0; xi < x; xi++) {
                        if (ground[r][c] != ground[r-xi][c] || visited[r-xi][c] == 1)
                        {
                            can_build = false;
                            break;
                        }
                    }
                    // 경사로 기록
                    for (int xi = 0; xi < x; xi++) {
                        visited[r-xi][c] = 1;
                    }
                }
                // 지금 위치기준 앞 지대 높이가 더 작을 경우
                else if (ground[r][c] > ground[r+1][c]) {
                    // 지대를 넘어가는지 판단
                    if (r + x > n - 1) {
                        can_build = false;
                        break;
                    }
                    // 경사로 짓는 공간 판단
                    // 1. 지금 위치와 높이가 같은지를 본다.
                    for (int xi = 1; xi < x; xi++) {
                        if (ground[r+1][c] != ground[r+1+xi][c])
                        {
                            can_build = false;
                            break;
                        }
                    }

                    // 경사로 기록
                    for (int xi = 0; xi < x; xi++) {
                        visited[r+1+xi][c] = 1;
                    }
                }

            }
            // 그냥 가는 경우
        }
        if (can_build == true) {
            p_path += 1;
        }
        memset(visited, 0, sizeof(visited));
    }


    return p_path;
}

int main() {
    // 가능한 경로 
    int t = 0;
    int p_path = 0;

    cin >> t;

    for (int ti = 0; ti < t; ti++) {
        cin >> n >> x;
        memset(ground, 0, sizeof(ground));
        
        // 절벽지대 정보 입력
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                cin >> ground[r][c];
            }
        }

        // 활주로 경로 고려
        p_path = count_road();

        cout << "#" << ti + 1 << " " << p_path << endl;
    }
    return 0;
}
