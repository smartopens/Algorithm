#include <string>
#include <vector>

using namespace std;

int min_ans_len, n;

vector<int> solution(vector<int> seq, int k) {
    vector<int> ans = { 0,0 };
    n = seq.size();
    min_ans_len = seq.size() + 1;

    int s_id = 0;
    int e_id = 0;
    int now_sn = seq[0];

    while (s_id <= n - 1 && e_id <= n - 1)
    {
        if (now_sn < k)
        {
            e_id += 1;
            now_sn += seq[e_id];
        }
        else if (now_sn >= k)
        {
            if (now_sn == k)
            {
                if (min_ans_len > e_id - s_id + 1)
                {
                    ans = { s_id, e_id };
                    min_ans_len = e_id - s_id + 1;
                }
            }

            now_sn -= seq[s_id];
            s_id += 1;
        }
    }
    return ans;
}