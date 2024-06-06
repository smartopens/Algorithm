#include <iostream>
#include <vector>

using namespace std;

// 해설 참조

int n;

int pro_nums[100002];

// 0: a , 1:b, 2:c, d:3
vector<vector<int>> n_store(4);
bool c_ok;

void c_count(int a)
{
	if (a > n - 1)
	{
		c_ok = true;
		return;
	}
	int st_id = 0;
	int em_st_id = 0;
	bool is_empty = false;
	int max_n = -1;
	bool can_order = false;

	for (int sv = 0; sv < 4; sv++)
	{
		if (n_store[sv].empty())
		{
			if (max_n < 0)
			{
				max_n = 0;
				st_id = sv;
				can_order = true;
			}
		}
		else if (pro_nums[a] > n_store[sv].back() && max_n < n_store[sv].back())
		{
			st_id = sv;
			max_n = n_store[sv].back();
			can_order = true;
		}
	}

	if (can_order == true)
	{
		n_store[st_id].push_back(pro_nums[a]);

		//for (int s = 0; s < 4; s++)
		//{
		//	cout << s + 1 << " :";
		//	for (int i = 0; i < n_store[s].size(); i++)
		//	{
		//		cout << n_store[s][i] << " ";
		//	}
		//	cout << "\n";
		//}

		c_count(a + 1);
	}

}
int main()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> pro_nums[i];
	}

	c_ok = false;
	//for (int s = 0; s < 4; s++)
	//{
	//	n_store.push_back({});
	//}

	c_count(0);

	if (c_ok == false)
	{
		cout << "NO\n";
	}
	else
	{
		cout << "YES\n";
	}

	return 0;
}