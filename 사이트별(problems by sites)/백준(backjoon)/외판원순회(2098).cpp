#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

// 도시 가중치 정보
// dp 저장소: 각 도시의 경로별 최소 비용
int n;
int city[18][18];
int dp[18][(1<<18)];

// 도시의 여러 순환 경로를 고려한다.
// 이 때, 시작 지점에서의 여러 경로를 본다.
// 위의 경로는 곧 도시 내에서 가능한 모든 경로를 의미한다.
int dfs(int now, int vi)
{
    // 해당 도시에서의 경로는 vi로 기록한다.
    // 모든 지점을 보았을 경우
    if (vi == ((1<<n)-1)){
        // 순환이 가능하지 않을 경우
        if (city[now][0] == 0) {
            return 10e8;
        }
        // 순환이 가능한 경우
        else {
            return city[now][0];
        }
    }

    // 이미 최소값이 갱신된 상태
    if (dp[now][vi] != -1)
    {
        return dp[now][vi];
    }

    // 기록
    dp[now][vi] = 10e8;

    // 지금 지점에서 가능한 경로를 본다.
    // 갈 수 없는 경로일 경우와 이미 해당 지점을 방문한 경우는 볼 필요가 없다.
    for (int i = 0; i < n; i++)
    {
        if (city[now][i] == 0) continue;
        if ((vi & (1 << i)) == (1 << i)) continue;
        dp[now][vi] = min(dp[now][vi], dfs(i, vi | (1 << i)) + city[now][i]);
    }

    // 최소 경로
    return dp[now][vi];
}
int main() {
    cin >> n;

    // 도시별 가중치 입력받기
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < n; c++)
        {
            int w;
            cin >> w;
            city[r][c] = w;
        }
    }

    // dp 공간 초기화 하기
    memset(dp, -1, sizeof(dp));

    // 도시 최소 순환경로 구하기
    cout << dfs(0,1) << endl;

    return 0;
}
