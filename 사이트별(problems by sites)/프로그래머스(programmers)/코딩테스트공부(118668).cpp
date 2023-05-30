#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

// 목표 알고력과 코딩력 설정
// 기록 dp 설정
int t_alg;
int t_co;
int n;
int dp[152][152];

// 문제들
vector<vector<int>> pros;

// 문제의 경우 탐색하기
int dfs(int alg, int co, int lvl)
{
    // 목표 능력치를 얻은 경우
    // 더 볼필요가 없다.
    if (alg >= t_alg && co >= t_co)
    {
        return 0;
    }

    // 최대 알고력과 코딩력에 도달하는 경우
    // 더 이상 각각의 알고력, 코딩력을 고려할 필요가 없다.
    // 다만, 최대치에 제한을 두지 않으면 경우가 너무 많아진다. (알고력과 코딩력은 각각 45000까지 커질 수 있다.)
    if (alg > t_alg) {
        alg = t_alg;
    }
    if (co > t_co) {
        co = t_co;
    }

    // 이미 기록된 경우
    if (dp[alg][co] != 0) {
        return dp[alg][co];
    }

    dp[alg][co] = 21e8;

    // 해당 문제를 푸는 경우
    for (int i = 0; i < n; i++)
    {
        if (alg < pros[i][0] || co < pros[i][1]) continue;
        dp[alg][co] = min(dp[alg][co], dfs(alg + pros[i][2], co + pros[i][3], lvl + 1) + pros[i][4]);
    }

    // 알고력과 코딩력 각각 문제를 풀 경우
    dp[alg][co] = min(dp[alg][co], dfs(alg + 1, co, lvl + 1) + 1);
    dp[alg][co] = min(dp[alg][co], dfs(alg, co + 1, lvl + 1) + 1);

    return dp[alg][co];
}

bool b_cmp(vector<int> a, vector<int> b) {
    if (a[1] > b[1])
    {
        return true;
    }
    return false;
}

bool a_cmp(vector<int> a, vector<int> b) {
    if (a[0] > b[0])
    {
        return true;
    }
    return false;
}

// 초기 알고력, 코딩력, 문제들이 주어진다.
int solution(int alg, int co, vector<vector<int>> problems) {

    // 전역 변수로 사용하기
    pros = problems;

    // 목표 알고력과 코딩력을 계산한다.
    vector<vector<int>> s_cop_pro = problems;
    vector<vector<int>> s_alg_pro = problems;
    sort(s_cop_pro.begin(), s_cop_pro.end(), b_cmp);
    sort(s_alg_pro.begin(), s_alg_pro.end(), a_cmp);

    t_alg = s_alg_pro[0][0];
    t_co = s_cop_pro[0][1];

    n = problems.size();

    // 기록 저장소dp 초기화
    for (int r = 0; r < 152; r++)
    {
        for (int c = 0; c < 152; c++)
        {
            dp[r][c] = 0;
        }
    }

    // 모든 코딩테스트 연습의 경우를 고려한다.
    // 이 때 알고력(alg), 코딩력(co)을 기준으로 기록한다.
    // 해당 경우에서의 시간을 고려해 정답을 구한다.
    int ans_time = dfs(alg, co, 0);

    return ans_time;
}
