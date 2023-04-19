#define _CRT_SECURE_NO_WARNINGS

#include <cstring>
#include <cctype>
#include <iostream>

int n;
int tc;
int costs[4];
int m_plan[12];
int path[12];
int visited[12];
int cost;
int answer = 21e8;

using namespace std;

void dfs(int idx, int n) {
    if(idx >= n){
    if(idx == n && cost < answer) answer = cost;
        return;
    }

    if (idx == 0) {
        cost += costs[3];
        dfs(12, n);
        cost -= costs[3];
    }

    cost += costs[2];
    dfs(idx + 3, n);
    cost -= costs[2];

    if (m_plan[idx] == 0) { dfs(idx + 1, n); return; }

    cost += costs[0] * m_plan[idx];
    dfs(idx + 1, n);
    cost -= costs[0] * m_plan[idx];

    cost += costs[1];
    dfs(idx + 1, n);
    cost -= costs[1];

}

int main() {
    cin >> tc;

    for (int t = 0; t < tc; t++) {
        for (int i = 0; i < 4; i++) cin >> costs[i];
        for (int i = 0; i < 12; i++) cin >> m_plan[i];

        cost = 0;
        answer = 21e8;
        dfs(0, 12);
        cout << "#"<< t+1 << " " << answer << endl;

    }
    
    return 0;
}
