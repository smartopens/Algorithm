#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

int n;
// 만들 수 있는 수
vector<int> p_info[2002];
int p_num[2002];

int s_num;
int c_num[2];

int gn_cnt;

int main()
{
	cin >> n;
	int in_pn;
	for (int i = 1; i < n+1; i++)
	{
		cin >> in_pn;
		p_num[i] = in_pn;
	}

	sort(p_num+1, p_num + n+1, greater<int>());

	for (int i = 1; i < n + 1; i++)
	{
		cout << p_num[i];
	}
	s_num = 0;
	gn_cnt = 0;
	int t_n = 0;
	int l_id, r_id, now_sn;
	for (int i = 1; i < n + 1; i++)
	{
		t_n = p_num[i];
		l_id = 1;
		r_id = n;
		
		while (l_id < r_id)
		{
			now_sn = p_num[l_id] + p_num[r_id];
			if (now_sn == t_n)
			{
				if (i == r_id)
				{
					r_id -= 1;
				}
				else if (i == l_id)
				{
					l_id += 1;
				}
				else {
					gn_cnt += 1;
					break;
				}
			}
			else if (now_sn > t_n)
			{
				r_id -= 1;
			}
			else if (now_sn < t_n)
			{
				l_id += 1;
			}
		}
	}

	cout << gn_cnt << endl;
	return 0;
}