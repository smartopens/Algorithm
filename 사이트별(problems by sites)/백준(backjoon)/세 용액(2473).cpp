#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
long long w_val[5002];
long long l_v;
long long m_v;
long long r_v;

int main()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> w_val[i];
	}

	sort(w_val, w_val+n);

	l_v = 0;
	m_v = 0;
	r_v = 0;
	
	//int l_id = 0;
	int m_id = 0;
	int r_id = n-1;
	long long tar_sn = 31e8;
	long long now_sn = 0;

	for (int l_id = 0; l_id < n - 2; l_id++)
	{
		m_id = l_id + 1;
		r_id = n - 1;

		while (m_id < r_id)
		{
			now_sn = w_val[l_id] + w_val[m_id] + w_val[r_id];
			
			if (abs(now_sn) < tar_sn)
			{
				tar_sn = abs(now_sn);
				l_v = w_val[l_id];
				m_v = w_val[m_id];
				r_v = w_val[r_id];
			}

			if (now_sn >= 0)
			{
				r_id -= 1;
			}
			else
			{
				m_id += 1;
			}
		}
	}
	
	cout << l_v << " " << m_v << " " << r_v << endl;

	return 0;
}