#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;

struct n_no
{
	vector<int> n_info;
	int co;
};

vector<n_no> meal;
int m_neu[4];

int min_co;
vector<int> now_meal;
vector<int> final_meal;
vector<int> m_num;

int final_co;

void m_count(int cn, int a, int m_id)
{
	if (a > cn - 1)
	{
		bool n_ok = true;
		for (int s = 0; s < 4; s++)
		{
			if (m_neu[s] > now_meal[s])
			{
				n_ok = false;
				break;
			}
		}

		//cout << cn << "\n";
		//for (int s = 0; s < m_num.size(); s++)
		//{
		//	cout << m_num[s] << " ";
		//}
		//cout << "\n";

		bool m_change = true;
		if (n_ok == true && min_co >= now_meal[4])
		{
			if (min_co > now_meal[4])
			{
				final_meal.clear();
				final_meal = m_num;
				min_co = now_meal[4];
			}
			else
			{
				/*for (int s = 0; s < m_num.size(); s++)
				{
					if (final_meal[s] < m_num[s])
					{
						m_change = false;
						break;
					}
					else if (final_meal[s] == m_num[s])
					{
						continue;
					}
					else
					{
						break;
					}
				}*/

				if (final_meal > m_num)
				{
					final_meal.clear();
					final_meal = m_num;
				}

			}
		}
		return;
	}
	vector<int> now_meal_back = {};
	now_meal_back = now_meal;

	vector<int> m_num_back = {};
	m_num_back = m_num;

	for (int s = m_id; s < n; s++)
	{
		for (int i = 0; i < 4; i++)
		{
			now_meal[i] += meal[s].n_info[i];
		}

		m_num.push_back(s);
		now_meal[4] += meal[s].co;

		m_count(cn, a + 1, s + 1);

		now_meal = now_meal_back;
		m_num.pop_back();
	}
}

int main()
{
	cin >> n;
	for (int i = 0; i < 4; i++)
	{
		cin >> m_neu[i];
	}

	int n1, n2, n3, n4, co;
	vector<int> in_neu;
	for (int mv = 0; mv < n; mv++)
	{
		in_neu.clear();
		for (int i = 0; i < 4; i++)
		{
			cin >> n1;
			in_neu.push_back(n1);
		}
		cin >> co;
		meal.push_back({ in_neu,co });
	}

	min_co = 21e8;
	for (int cn = 1; cn < n + 1; cn++)
	{
		now_meal = { 0,0,0,0,0 };
		m_count(cn,0,0);
	}

	if (min_co == 21e8)
	{
		cout << -1 << "\n";
	}
	else
	{
		sort(final_meal.begin(), final_meal.end());
		cout << min_co << "\n";
		for (int s = 0; s < final_meal.size(); s++)
		{
			cout << final_meal[s]+1 << " ";
		}
		cout << "\n";

	}
	
	return 0;
}