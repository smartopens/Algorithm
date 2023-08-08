#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <unordered_map>
#include <queue>

using namespace std;

struct max_v {
    int v;
    bool operator < (max_v now)const
    {
        if (v < now.v)
        {
            return true;
        }
        if (v > now.v)
        {
            return false;
        }
        return false;
    }
};

struct min_v {
    int v;
    bool operator < (min_v now)const
    {
        if (v > now.v)
        {
            return true;
        }
        if (v < now.v)
        {
            return false;
        }
        return false;
    }
};

priority_queue<max_v> g_pq = {};
priority_queue<min_v> l_pq = {};
unordered_map<int, int> um_vi = {};

int t;
int k;

int main() {
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> k;

        // 자료구조 초기화
        while (!g_pq.empty())
        {
            g_pq.pop();
        }
        while (!l_pq.empty())
        {
            l_pq.pop();
        }
        um_vi.clear();

        // 한번의 테스트케이스당 최대 100만개의 연산이 있다.
        // 고로, 힙자료구조를 사용해서 효율을 높인다.
        // 최댓값과 최솟값이 중요하므로, 삭제를 하고나서 각 자료구조를 본다.
        // 자료구조의 중요 위치별 존재 유무를 판단한다.
        char com = '\0';
        int in_v = 0;
        int top_n = 0;
        for (int ki = 0; ki < k; ki++)
        {
            cin >> com >> in_v;

            if (com == 'I')
            {
                g_pq.push({ in_v });
                l_pq.push({ in_v });
                um_vi[in_v] += 1;
            }
            else {
                if (in_v > 0)
                {
                    if (!g_pq.empty())
                    {
                        top_n = g_pq.top().v;
                        um_vi[top_n] -= 1;
                        g_pq.pop();
                    }
                }
                else {
                    if (!l_pq.empty())
                    {
                        top_n = l_pq.top().v;
                        um_vi[top_n] -= 1;
                        l_pq.pop();
                    }
                }
                while (!g_pq.empty() && um_vi[g_pq.top().v] == 0)
                {
                    g_pq.pop();
                }
                while (!l_pq.empty() && um_vi[l_pq.top().v] == 0)
                {
                    l_pq.pop();
                }
            }
        }

        // 정답 출력하기
        if (g_pq.empty() || l_pq.empty())
        {
            cout << "EMPTY" << endl;
        }
        else {
            cout << g_pq.top().v << " " << l_pq.top().v << endl;
        }
    }
    return 0;
};
