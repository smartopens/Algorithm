#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

int n;
int room_n;

struct m_no
{
	int s_t;
	int e_t;

	bool operator  < (m_no now_v) const
	{
		if (e_t > now_v.e_t)
		{
			return true;
		}
		if (e_t < now_v.e_t)
		{
			return false;
		}
		return false;
	}
};

bool cmp(m_no a, m_no b)
{
	if (a.s_t < b.s_t)
	{
		return true;
	}
	if (a.s_t > b.s_t)
	{
		return false;
	}
	return false;
}

vector<m_no> meetings;

int main()
{
	cin >> n;

	int rn, st, et;
	for (int i = 0; i < n; i++)
	{
		cin >> rn >> st >> et;
		meetings.push_back({ st,et });
	}

	sort(meetings.begin(), meetings.end(), cmp);
	
	priority_queue<m_no> pq;
	pq.push(meetings[0]);

	room_n = 1;
	int ms, me, now_e;
	for (int s = 1; s < meetings.size(); s++)
	{
		ms = meetings[s].s_t;
		me = meetings[s].e_t;

		now_e = pq.top().e_t;

		if (now_e > ms)
		{
			room_n += 1;
		}
		else
		{
			pq.pop();
		}
		pq.push({ meetings[s] });
	}

	cout << room_n << endl;

	return 0;
}
