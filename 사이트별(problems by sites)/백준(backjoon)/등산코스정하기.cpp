#include <algorithm>
#include <queue>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int n;

// 우선순위큐(min heap) 설정하기
struct p_node {
    int cost;
    int to;

    bool operator < (p_node now) const
    {
        if (cost > now.cost)
        {
            return true;
        }
        if (cost < now.cost)
        {
            return false;
        }
        return false;
    }
};

// 그래프와 거리 정보
priority_queue<p_node> pq;
vector<p_node> graph[50002];
int dists[50002];

int sum_vi[50002];

// 최소 intensity, 등산지점
int min_i = 21e8;
int min_v = 21e8;

// 가능한 모든 등산 경로를 고려한다.
// 등산 경로 중 가장 긴 intensity를 기록한다.
// 각 등산 경로는 최소 intensity를 목표로 한다.
void dikstra(vector<int>& gates)
{
    // 거리 정보 초기화
    for (int i = 0; i < n + 1; i++)
    {
        dists[i] = 21e8;
    }

    // 시작 지점 설정
    for (int g : gates)
    {
        dists[g] = 0;
    }

    // 등산 경로를 본다.
    while (!pq.empty())
    {
        p_node now = pq.top();
        pq.pop();
        int now_v = now.to;
        int cost = now.cost;

        if (dists[now_v] < cost) continue;

        // 등산 지점에 도착한 경우이다.
        // 가장 최소 intensity, 등산지점을 기록한다.
        // 등산 지점에 도착하고 나서는 더 고려하지 않는다.
        if (sum_vi[now_v] == 1)
        {
            if (min_i >= dists[now_v]) {

                if (min_v > now_v) {
                    min_i = dists[now_v];
                    min_v = now_v;
                }
            }
            continue;
        }

        // 등산 경로에서 intensity를 기록한다.
        // 이 때, intensity는 가장 긴 시간이다.
        for (int s = 0; s < graph[now_v].size(); s++)
        {
            p_node next = graph[now_v][s];
            int n_cost = max(cost, next.cost);

            if (dists[next.to] <= n_cost) continue;
            dists[next.to] = n_cost;
            pq.push({ n_cost, next.to });
        }
    }
    return;
}

vector<int> solution(int n_size, vector<vector<int>> paths, vector<int> gates, vector<int> summits) {
    vector<int> answer;

    n = n_size;

    // 등산 연결 정보 입력 받기
    // 등산로는 양방향이다.
    for (vector<int> v : paths)
    {
        graph[v[0]].push_back({ v[2],v[1] });
        graph[v[1]].push_back({ v[2],v[0] });
    }

    // 여러 출발지에서 가능한 등산 경로를 본다.
    // 우선순위 큐에 같이 넣어준다.
    for (int g : gates)
    {
        pq.push({ 0,g });
    }

    // 등산 도착지점 설정하기
    for (int s : summits)
    {
        sum_vi[s] = 1;
    }

    // 모든 등산 경로에서 최소 intensity값을 고려한다.
    dikstra(gates);
    answer = { min_v, min_i };
    return answer;
}
