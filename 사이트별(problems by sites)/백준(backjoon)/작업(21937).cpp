#include <iostream>
#include <vector>

using namespace std;

int n, m;
int wx;

vector<int> wr_gp[100002];
int vi[100002];

int pre_wn;

void w_count(int wv)
{
	int to_v;
	for (int s = 0; s < wr_gp[wv].size(); s++)
	{
		to_v = wr_gp[wv][s];
		if (vi[to_v] != 0) continue;

		pre_wn += 1;
		vi[to_v] = 1;
		w_count(to_v);
	}
}

int main()
{
	cin >> n >> m;
	int wa, wb;
	for (int i = 0; i < m; i++)
	{
		cin >> wa >> wb;
		wr_gp[wb].push_back(wa);
	}

	cin >> wx;
	pre_wn = 0;
	vi[wx] = 1;
	w_count(wx);

	cout << pre_wn << endl;

	return 0;
}