#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

// 트리가 하나있다. (max:10만)
// q개의 지점에서의 노드 수를 각각 구하기
// 특정 노드 tv: left, right
// tv1, tv2, tv3 ... 

int n, r, q;

vector<int> t_gp[100002];
int t_sub[100002];
int vi[100002];

void make_tree(int tv)
{
	int to_v;

	for (int s = 0; s < t_gp[tv].size(); s++)
	{
		to_v = t_gp[tv][s];
		if (vi[to_v] != 0) continue;

		vi[to_v] = 1;
		//t_gp2[tv].push_back(to_v);
		//t_gp2[to_v].push_back(tv);
		make_tree(to_v);
	}

}

int sn_store(int tv)
{
	if (t_sub[tv] != 0)
	{
		return t_sub[tv];
	}

	// 트리 구성하기
	t_sub[tv] = 1;
	int to_v;
	for (int s = 0; s < t_gp[tv].size(); s++)
	{
		to_v = t_gp[tv][s];
		if (vi[to_v] != 0) continue;
		
		vi[to_v] = 1;
		sn_store(to_v);
		t_sub[tv] += t_sub[to_v];
	}

	return t_sub[tv];
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> r >> q;
	int tv, to_tv;
	for (int i=0; i<n-1; i++)
	{
		cin >> tv >> to_tv;
		t_gp[tv].push_back({ to_tv });
		t_gp[to_tv].push_back({ tv });
	}

	vi[r] = 1;
	sn_store(r);

	int in_q;
	for (int i = 0; i < q; i++)
	{
		cin >> in_q;
		cout << t_sub[in_q] << "\n";
	}

	return 0;
}