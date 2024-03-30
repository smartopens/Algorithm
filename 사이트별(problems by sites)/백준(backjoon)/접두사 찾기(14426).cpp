#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_set>

using namespace std;

int n, m;

string m_str[10002];
unordered_set<string> str_case;

int main()
{
	cin >> n >> m;
	string in_ori, in_m;
	string in_str;
	for (int i = 0; i < n; i++)
	{
		cin >> in_ori;
		in_str = "";

		for (int s = 0; s < in_ori.length(); s++)
		{
			in_str += in_ori[s];
			str_case.insert(in_str);
		}
	}

	for (int i = 0; i < m; i++)
	{
		cin >> in_m;
		m_str[i] = in_m;
	}

	int ans = 0;
	for (int ms = 0; ms < m; ms++)
	{
		auto ori_s = str_case.find(m_str[ms]);
		if (ori_s != str_case.end())
		{
			ans += 1;
		}
	}

	cout << ans << endl;
	return 0;
}