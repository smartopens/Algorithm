#include <iostream>
#include <string>
#include <cstring>
#include <map>

using namespace std;

// 같은 종류로 보는 경우가 있다.(문자 구성요소, 각 개수)
// 비슷한 단어로 보는 경우가 있다.(더하기, 빼기, 변환 고려)

int n;
int vi[10];

string t_st;
string now_st;

int t_sn;

int main()
{
	cin >> n;
	cin >> t_st;
	int now_sn;
	int ans_sn = 0;
	int t_map[30] = {};

	for (int i = 0; i < t_st.length(); i++)
	{
		t_map[t_st[i]-'A'] +=1;
	}

	//a_set = set();
	int t_s, n_s;
	bool is_ok = false;
	for (int i = 0; i < n - 1; i++)
	{
		memset(vi, 0, sizeof(vi));
		int s_map[30] = {};

		now_sn = 0;
		is_ok = false;
		cin >> now_st;
		//t_sn = max(t_st.length(), now_st.length());

		t_s = t_st.length();
		n_s = now_st.length();

		for (int s = 0; s < now_st.length(); s++)
		{
			s_map[now_st[s] - 'A'] += 1;
		}

		for (int s = 0; s < 30; s++)
		{
			now_sn += abs(t_map[s] - s_map[s]);
		}

		//cout << now_sn << endl;
		// 같거나 전환
		if (t_s == n_s)
		{
			if (now_sn <= 2)
			{
				is_ok = true;
			}
		}
		// 더하기
		else if (t_s - 1 == n_s)
		{
			if (now_sn == 1)
			{
				is_ok = true;
			}
			/*
			bool h_case = true;
			for (int s = 0; s < 30; s++)
			{
				if ((t_map[s] > 0 && s_map[s] == 0) ||
					(t_map[s] == 0 && s_map[s] > 0))
				{
					h_case = false;
				}
			}
			if (h_case == true)
			{
				is_ok = true;
			}*/

		}
		// 빼기
		else if (t_s + 1 == n_s)
		{
			if (now_sn == 1)
			{
				is_ok = true;
			}
		}
		if (is_ok == true)
		{
			ans_sn += 1;
		}
	}

	cout << ans_sn << endl;
	return 0;
}