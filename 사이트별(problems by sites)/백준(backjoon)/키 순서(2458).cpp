#include <iostream>
#include <vector>

using namespace std;

int n, m;

vector<int> taller[502];
vector<int> smaller[502];

int t_vi[502][502];
int s_vi[502][502];

int main()
{
	cin >> n >> m;
	
	// 키 대소 비교 입력받기
	int s_n = 0;
	int s_in = 0;
	int b_in = 0;
	for (int i = 0; i < m; i++)
	{
		cin >> s_in >> b_in;
		taller[s_in].push_back(b_in);
		smaller[b_in].push_back(s_in);
		t_vi[s_in][b_in] = 1;
		s_vi[b_in][s_in] = 1;
	}

	// 플로이드 워셜 문제중 하나이다.
	// 대소 관계를 각각의 자료구조에 저장한다.
	// 모든 노드를 돌면서 각 노드보다 큰경우, 작은 경우 모두
	// 확립해준다.
	int tr_v = 0;
	int sr_v = 0;
	for (int v = 1; v < n + 1; v++)
	{
		for (int s = 0; s < taller[v].size(); s++)
		{
			tr_v = taller[v][s];
			for (int k = 0; k < taller[tr_v].size(); k++)
			{
				if (t_vi[v][taller[tr_v][k]] != 1)
				{
					taller[v].push_back(taller[tr_v][k]);
					t_vi[v][taller[tr_v][k]] = 1;
				}
			}
		}

		for (int s = 0; s < smaller[v].size(); s++)
		{
			sr_v = smaller[v][s];
			for (int k = 0; k < smaller[sr_v].size(); k++)
			{
				if (s_vi[v][smaller[sr_v][k]] != 1)
				{
					smaller[v].push_back(smaller[sr_v][k]);
					s_vi[v][smaller[sr_v][k]] = 1;
				}
			}
		}
	}

	// 최종적으로 노드마다 크거나 작은 경우가 n-1개로 확립
	// 된다면 해당 노드의 순서를 알 수 있다.
	for (int v = 1; v < n + 1; v++)
	{
		if (smaller[v].size() + taller[v].size() == n - 1)
		{
			s_n += 1;
		}
	}

	cout << s_n << endl;
	return 0;
}
