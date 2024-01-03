#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

// 톱니바퀴 T개가 있다. (톱니바퀴: 8방향, 각 2개의 상태)
// 특정 톱니를 회전시킬때 양옆과 맞닿는 극을 고려한다.
// 차례대로 회전을 하는지, 극의 상태를 본다.

int t;
int k;

vector<int> ball[1002];
int c_vi[1002];

void rotate(int b_id, int sdi)
{
	if (sdi == 1) {
		ball[b_id].insert(ball[b_id].begin(), ball[b_id][ball[b_id].size() - 1]);
		ball[b_id].pop_back();
	}
	else
	{
		ball[b_id].insert(ball[b_id].end(), ball[b_id][0]);
		ball[b_id].erase(ball[b_id].begin());
	}
}

void b_cycle(int b_id, int sdi)
{
	memset(c_vi, 0, sizeof(c_vi));

	c_vi[b_id] = sdi;
	int di = sdi;
	for (int i = b_id+1; i < t+1; i++)
	{
		if(ball[i-1][2] == ball[i][6]){
			break;
		}
		else if (ball[i-1][2] != ball[i][6])
		{
			di *= -1;
			c_vi[i] = di;
		}
	}

	di = sdi;
	for (int i = b_id -1; i > 0; i--)
	{
		if (ball[i + 1][6] == ball[i][2]) {
			break;
		}
		else if (ball[i + 1][6] != ball[i][2])
		{
			di *= -1;
			c_vi[i] = di;
		}
	}

	for (int bv = 1; bv < t + 1; bv++)
	{
		if (c_vi[bv] == 0) continue;
		rotate(bv, c_vi[bv]);
	}
}

int main()
{
	cin >> t;
	string in_ball;
	for (int bv = 1; bv < t+1; bv++)
	{
		cin >> in_ball;
		for (int i = 0; i < 8; i++)
		{
			ball[bv].push_back(in_ball[i]-'0');
		}
	}
	
	cin >> k;
	int bv, di;
	while (k > 0)
	{
		cin >> bv >> di;
		b_cycle(bv, di);
		k -= 1;
	}

	int s_num = 0;
	for (int bv = 1; bv < t + 1; bv++)
	{
		s_num += ball[bv][0];
	}

	/*vector<int> tmp = { 1,2,3 };
	tmp.insert(tmp.end(), 10);
	cout << tmp[3];*/

	cout << s_num << endl;
	return 0;
}