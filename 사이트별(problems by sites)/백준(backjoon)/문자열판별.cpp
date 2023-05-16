#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <algorithm>

// 목표 문자열의 크기를 설정한다.
// 만들 수 있는지를 기록해 트리거로 활용한다.
int n, t_size;
bool can_make = false;
int dp[102];

using namespace std;

// 문자열 제작 가능한지 보기
// 만약 최종적으로 t_size만큼 탐색한다면 제작가능하다.
// 제작 가능하지 않다면 0을 return한다.
int dfs(int t_id, string t_word, string i_words[102])
{   
    // 최종적으로 제작이 가능하다.
    // 이 경우 트리거를 true로 저장한다.
    if (t_id == t_size) {
        can_make = true;
        return 1;
    }

    if (dp[t_id] != -1)
    {
        return dp[t_id];
    }

    dp[t_id] = 0;

    // 트리거를 활용했다.
    // 이미 가능한 경우가 나왔으므로 다른 경우에서 기록할 필요가 없다.
    if (can_make == true) return 1;
    
    // 현재 t_id를 기준으로 재료문자열들을 더할 수 있을지를 본다.
    // 가능하다면 다음 t_id를 갱신해 더한다.
    for (int i = 0; i < n; i++)
    {
        string t_part = t_word.substr(t_id, i_words[i].length());

        if (t_part != i_words[i]) continue;
        dp[t_id] = max(dp[t_id],dfs(t_id + t_part.length(), t_word, i_words));
    }
    return dp[t_id];
}

int main() {
    // 목표 문자, 재료 문자들 저장
    string t_word;
    string i_words[102];

    cin >> t_word >> n;
    
    // 목표 문자 크기
    t_size = t_word.length();
    for (int i = 0; i < n; i++)
    {
        cin >> i_words[i];
    }

    // 문자열 제작 가능 저장소 dp 초기화 하기
    for (int i = 0; i < t_size; i++)
    {
        dp[i] = -1;
    }

    // 목표 문자열을 index기준으로 탐색한다.
    // 현재 t_id기준으로 재료문자열 크기만큼을 비교한다.
    dfs(0, t_word, i_words);

    // 가능한 경우
    if (can_make != true) {
        cout << 0 << endl;
    }
    // 불가능한 경우
    else if (can_make == true) {
        cout << 1 << endl;
    }

    return 0;
}
