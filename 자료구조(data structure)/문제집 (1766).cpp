#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m;
int p_pros[32002];
vector<int> p_gp[32002];
vector<int> p_pa;

struct p_no {
    int pn;

    bool operator < (p_no now) const {
        if (pn > now.pn) {
            return true;
        }
        if (pn < now.pn) {
            return false;
        }
        return true;
    }
};

int main() {
    cin >> n >> m;
    int a, b;

    // 문제별 순서관계를 저장한다.
    // 문제별 미리 풀어야되는 문제 수를 저장한다.

    for (int i = 0; i < m; i++)
    {
        cin >> a >> b;
        p_gp[a].push_back(b);
        p_pros[b] += 1;
    }

    // 선행 문제 수가 없는 경우, 난이도가 쉬운것부터 나오도록 우선순위큐를 사용한다.
    priority_queue<p_no> pq = {};
    for (int i = 1; i < n + 1; i++)
    {
        if (p_pros[i] == 0)
        {
            pq.push({ i });
        }
    }

    // 쉬운 난이도 문제부터 풀고 기록한다.
    // 해당 문제를 푼 경우, 이 문제와 연관된 문제의 중요도를 감소시킨다.
    // 0이 되면 힙큐에 저장한다.
    int n_p;
    while (!pq.empty())
    {
        n_p = pq.top().pn;
        pq.pop();

        p_pa.push_back(n_p);
        int to_p;
        for (int i = 0; i < p_gp[n_p].size(); i++)
        {
            to_p = p_gp[n_p][i];
            p_pros[to_p] -= 1;
            if (p_pros[to_p] == 0) {
                pq.push({ to_p });
            }
        }
    }

    for (int i = 0; i < p_pa.size(); i++)
    {
        cout << p_pa[i] << " ";
    }

    return 0;
};
