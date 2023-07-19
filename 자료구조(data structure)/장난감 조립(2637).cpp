#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

// 필요한 정보
// 현재 부품 번호, 곱하는 수

int n, m;
int pros_t[102];

struct p_no {
    int to;
    int cnt;
};

vector <p_no> p_gp[102];
vector <int> base_ts;
queue <int> ts_com;

int base_ca[102][102];
int base_num[102];
int base_vi[102];

int main() {
    // 부품번호, 관계 수
    cin >> n;
    cin >> m;

    // 부품 x에 y가 k개 들어간다.
    // 이 때 y와 x와의 관계 그래프, x부품의 중요도 수를 기록한다.

    for (int i = 0; i < m; i++)
    {
        int x, y, k;
        cin >> x >> y >> k;
        p_gp[y].push_back({ x,k });
        pros_t[x] += 1;
    }

    // base_ts: 기본 부품을 저장한다.
    for (int i = 1; i < n + 1; i++)
    {
        if (pros_t[i] == 0) {
            base_ts.push_back(i);
        }
    }

    // 각 부품별로 기본 부품 수들의 목록을 사용한다.
    // 기본 부품 수 저장하기
    for (int j = 0; j < base_ts.size(); j++)
    {
        base_ca[base_ts[j]][base_ts[j]] = 1;
    }

    // 위상 정렬
    // 기본 부품부터 해당 부품으로 채울 수 있는 부품들을 찾아간다.
    // 해당 부품의 기본 부품수를 기록하고 중요도수를 감소시킨다.
    // 중요도수가 0이 되면 해당 부품을 고려한다.

    while (!ts_com.empty())
    {
        int n_t = ts_com.front();
        ts_com.pop();

        int to_t = 0;
        int to_cnt = 0;

        for (int i = 0; i < p_gp[n_t].size(); i++)
        {
            to_t = p_gp[n_t][i].to;
            to_cnt = p_gp[n_t][i].cnt;

            for (int j = 0; j < base_ts.size(); j++)
            {
                if (base_ca[n_t][base_ts[j]] == 0) continue;
                base_ca[to_t][base_ts[j]] += base_ca[n_t][base_ts[j]] * to_cnt;
                
            }
            pros_t[to_t] -= 1;

            if (pros_t[to_t] == 0) {
                ts_com.push(to_t);
            }
        }

    }

    // 완제품의 기본 품목수 저장하기
    for (int i = 0; i < base_ts.size(); i++)
    {
        base_num[base_ts[i]] = base_ca[n][base_ts[i]];
    }

    // 부품번호 작은것부터 수 출력하기
    for (int i = 1; i < 102; i++)
    {
        if (base_num[i] == 0) continue;
        cout << i << " " << base_num[i] << "\n";
    }

    return 0;
};
