#include <iostream>
#include <queue>

using namespace std;

int n;
struct q_no
{
	int v;

	bool operator < (q_no now) const
	{
		if (v < now.v)
		{
			return true;
		}
		if (v > now.v)
		{
			return false;
		}
		return false;
	}
};

priority_queue<q_no> max_q;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> n;
	int in_n = 0;
	int p_n = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> in_n;

		if (in_n > 0)
		{
			max_q.push({ in_n });
		}
		else if (in_n == 0)
		{
			if (!max_q.empty())
			{
				p_n = max_q.top().v;
				cout << p_n << "\n";
				max_q.pop();
			}
			else
			{
				cout << 0 << "\n";
			}
		}
	}
	return 0;
}
