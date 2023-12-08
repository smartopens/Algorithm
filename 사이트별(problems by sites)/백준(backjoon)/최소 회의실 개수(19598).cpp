#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

// n개의 회의(max: 10만)
// 회의: 시작시간-종료시간

int n;

struct m_no
{
	int st;
	int et;
};

struct pq_no
{
	int st;
	int et;

	bool operator < (pq_no now) const {
		if (now.et < et)
		{
			return true;
		}
		if (now.et > et)
		{
			return false;
		}
		return false;
	}
};

bool cmp(m_no a, m_no b)
{
	if (a.st < b.st)
	{
		return true;
	}
	if (a.st > b.st)
	{
		return false;
	}
	return false;
}
vector<m_no> meetings;
int min_mn;

int main()
{
	cin >> n;

	int in_s, in_e;
	for (int i = 0; i < n; i++)
	{
		cin >> in_s >> in_e;
		meetings.push_back({ in_s, in_e });
	}

	sort(meetings.begin(), meetings.end(), cmp);
	priority_queue<pq_no> pq;

	pq.push({ meetings[0].st, meetings[0].et });
	min_mn = 1;
	pq_no now_m;
	for (int s = 1; s < meetings.size(); s++)
	{
		now_m = pq.top();
		//cout << now_m.st << "!" << endl;
		//cout << meetings[s].st << endl;
		if (now_m.et > meetings[s].st)
		{
			min_mn += 1;
			pq.push({ meetings[s].st, meetings[s].et });
		}
		else {
			pq.pop();
			pq.push({ meetings[s].st, meetings[s].et });
		}
	}

	//while(!pq.empty())
	//{
	//	cout << pq.top().st  << " "<< pq.top().et << endl;
	//	pq.pop();
	//}
	
	cout << min_mn << endl;
	return 0;
}