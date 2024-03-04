#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int n, k;
// 2 ~ 20 ����
vector<int> stu_sco[22];

long long to_f_n;

int main()
{
	cin >> n >> k;
	string f_in;
	for (int i = 0; i < n; i++)
	{
		cin >> f_in;
		stu_sco[f_in.length()].push_back(i + 1);
	}

	to_f_n = 0;
	for (int nv = 2; nv < 21; nv++)
	{
		if (stu_sco[nv].size() == 0) continue;

		queue<int> sco_q = {};
		sco_q.push(stu_sco[nv][0]);

		for (int s = 1; s < stu_sco[nv].size(); s++)
		{
			int f_n = 0;
			// ģ���� �� �� ���� ���
			while (sco_q.size() > 0 && sco_q.front() < stu_sco[nv][s] - k)
			{
				// ���� �� ���ϱ�
				to_f_n += (sco_q.size() - 1);
				sco_q.pop();
			}

			// ģ���� �� �� �ִ� ���
			sco_q.push(stu_sco[nv][s]);
		}

		// ������ ���
		while (sco_q.size() > 0)
		{
			// ���� �� ���ϱ�
			to_f_n += (sco_q.size() - 1);
			sco_q.pop();
		}
	}

	cout << to_f_n << endl;
	return 0;
}