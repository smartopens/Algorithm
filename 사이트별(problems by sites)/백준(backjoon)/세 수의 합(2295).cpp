#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <vector>

using namespace std;

int n;

long long nums[1002];
vector<long long> new_nums;
unordered_map<long long, int> g_num;

long long max_sn;

int main()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> nums[i];
		//g_num[nums[i]] = 1;
	}

	for (int nv = 0; nv < n; nv++)
	{
		for (int to_v = nv; to_v < n; to_v++)
		{
			new_nums.push_back({ nums[nv] + nums[to_v] });
		}
	}

	sort(nums, nums + n );
	sort(new_nums.begin(), new_nums.end());

	max_sn = -1;
	int new_n;
	int now_sn = 0;
	for (int nv = n-1; nv > -1; nv--)
	{
		for (int to_v = nv; to_v > -1; to_v--)
		{
			new_n = nums[nv] - nums[to_v];

			int l_id = 0;
			int r_id = new_nums.size() - 1;
			int mid;

			while (l_id <= r_id)
			{
				mid = (l_id + r_id) / 2;
				now_sn = new_nums[mid];

				if (new_n == now_sn)
				{
					if (nums[nv] > max_sn)
					{
						max_sn = nums[nv];
					}
					break;
				}
				// 10 , 15-10
				else if (new_n > now_sn)
				{
					l_id = mid+1;
				}
				else if (new_n < now_sn)
				{
					r_id = mid-1;
				}

			}
		}
	}

	cout << max_sn << endl;
	return 0;
}