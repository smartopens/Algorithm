#define _CRT_SECURE_NO_WARNINGS
#include <map>
#include <vector>
#include <iostream>

using namespace std;
int max_n = -21e8;
int min_n = 21e8;
int n;
int nums[12];
int num;
vector<int> answers;

//
//map<char, int> o_nums;
//char operators[4] = { '+', '-', '*', '/' };
int operators[4] = {};

int calcurate(int o_num, int a, int b) {
    if (o_num == 0) return a + b;
    if (o_num == 1) return a - b;
    if (o_num == 2) return a * b;
    if (o_num == 3) return a / b;
}

void dfs(int idx) {
    if (idx >= n) {
        if (num > max_n) max_n = num;
        if (num < min_n) min_n = num;

        return;
    }

    for (int i = 0; i < 4; i++) {
        if (operators[i] == 0) continue;
        
        operators[i] -= 1;
        int ori_num = num;
        num = calcurate(i,num, nums[idx]);
        dfs(idx + 1);
        num = ori_num;
        operators[i] += 1;
    }

}
int main() {
    int tc;
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cin >> n;
        for (int i = 0; i < 4; i++) {
            cin >> operators[i];
        }
        max_n = -21e8;
        min_n = 21e8;

        for (int i = 0; i < n; i++) {
            cin >> nums[i];
        }
        num = nums[0];

        dfs(1);
        cout << "#" << t + 1 << " " << max_n - min_n << endl;

        
    }
    return 0;
}
