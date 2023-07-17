#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <set>

using namespace std;

//ex)
// 위의 수 nums1: 1,2,3,4 ...
// 아래 수 nums2: 1,4,5,10 ... 

//1,2,3, 4, 5, 6, 7, 8, ...
//1,4,5,10, 3, 1, 1, 1, 
//
//1, 2, 3, 4
//4, 2, 1, 3
//
//1, 2, 3, 4
//4, 3, 1, 2

int n;
set<int> r_nums;

int main() {
    cin >> n;

    int in_n = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> in_n;
        r_nums.insert(in_n);
    }

    cout << r_nums.size() << endl;
    for (int rn : r_nums) {
        cout << rn << "\n";
    }
    return 0;
};
