#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

int m_r, m_c;

vector<string> st_info;
vector<string> st_table;
set<string> d_check;

int c_n;

int main()
{
	cin >> m_r >> m_c;
	string in_t_st;
	for (int r = 0; r < m_r; r++)
	{
		cin >> in_t_st;
		st_info.push_back(in_t_st);
	}

	for (int c = 0; c < m_c; c++)
	{
		string new_st = "";
		for (int r = m_r-1; r > -1; r--)
		{
			new_st += st_info[r][c];
		}
		
		st_table.push_back(new_st);
	}

	bool is_double = false;
	c_n = 0;
	while (true)
	{
		d_check.clear();
		is_double = false;
		for (int sc = 0; sc < m_c; sc++)
		{
			st_table[sc].pop_back();
			//cout << st_table[sc] << "\n";
			auto st_id = d_check.find(st_table[sc]);
			
			// 중복되는 경우
			if (st_id != d_check.end())
			{
				is_double = true;
				break;
			}
			else
			{
				d_check.insert(st_table[sc]);
			}
		}

		if (is_double == true || st_table[0].length() == 0)
		{
			break;
		}
		else
		{
			c_n += 1;
		}
	}

	cout << c_n << "\n";

	return 0;
}