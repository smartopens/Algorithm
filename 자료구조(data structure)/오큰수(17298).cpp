#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stack>

using namespace std;

int n;

struct no {
    int idx;
    int num;
};

stack<no> st_nums = {};
no nums[1000002];
int ans[1000002];

// 수열을 차례차례 본다. 동시에 스택에 해당 숫자와 idx를 저장한다.
// 가장 최근 숫자를 기준으로 다음 숫자가 크다면 이 수보다 작은 저장수들의 오큰수를 구할 수 있다.
// 반대의 경우, 아직 오큰수를 보지 못했으므로 스택에 저장한다.
// 마지막까지 보고난 후 스택에 남아있는 수는 오큰수가 없다.
void solve()
{
    // 수열 저장하기
    st_nums.push( nums[1] );
    
    for (int i = 2; i < n + 1; i++)
    {
        no now = st_nums.top();

        // 마지막 스택수보다 다음수가 작은 경우
        if (now.num >= nums[i].num) {
            st_nums.push({ nums[i] });
        }

        // 마지막 스택수보다 다음수가 큰 경우
        else {
            while (!st_nums.empty() && st_nums.top().num < nums[i].num)
            {
                ans[st_nums.top().idx] = nums[i].num;
                st_nums.pop();

            }
            st_nums.push({ nums[i] });
        }
    }
    // 오큰수가 없는 경우
    while (!st_nums.empty())
    {
        no now = st_nums.top();
        ans[now.idx] = -1;
        st_nums.pop();
    }
};

int main() {
    cin >> n;

    // 수열을 입력받는다.
    for (int i = 1; i < n+1; i++)
    {
        int num;
        cin >> num;
        nums[i] = { i,num };
    }

    // 특정 수를 기준으로 커지는 가장 왼쪽 지점의 수를 본다.
    // 없을 경우 -1이 출력되야 한다.
    solve();

    // 오큰수들을 출력한다.
    for (int i = 1; i < n + 1; i++)
    {
        cout << ans[i] << " ";
    }
    return 0;
}
