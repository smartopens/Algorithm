#include <iostream>
#include <string>

using namespace std;

int n, m;

int git_info[10][50];
int play_list[10];

int max_pn;
int min_gn;

void get_max_play()
{
	int can_play[50] = {};
	int now_pn = 0;
	int now_gn = 0;
	for (int gv = 0; gv < n; gv++)
	{
		if (play_list[gv] == 0) continue;
		//cout << gv << " ";
		for (int s = 0; s < m; s++)
		{
			if (git_info[gv][s] == 1)
			{
				can_play[s] = 1;
			}
		}
		now_gn += 1;
	}
	//cout << endl;

	for (int s = 0; s < m; s++)
	{
		if(can_play[s] == 1)
		{
			now_pn += 1;
		}
	}

	if (max_pn < now_pn)
	{
		max_pn = now_pn;
		min_gn = now_gn;
	}
	else if (max_pn == now_pn)
	{
		if (min_gn > now_gn)
		{
			min_gn = now_gn;
		}
	}
}

void play_count(int a, int idx)
{
	get_max_play();
	if (a > n - 1)
	{
		return;
	}
	for (int s = idx; s < n; s++)
	{
		play_list[s] = 1;
		play_count(a + 1, s + 1);
		play_list[s] = 0;
	}
}

int main()
{
	cin >> n >> m;
	string in_git, in_song;
	for (int gv = 0; gv < n; gv++)
	{
		cin >> in_git >> in_song;
		for (int sv = 0; sv < m; sv++)
		{
			if (in_song[sv] == 'N') continue;
			git_info[gv][sv] = 1;
		}
	}

	max_pn = 0;
	min_gn = 21e8;
	play_count(0,0);

	if (max_pn <= 0)
	{
		cout << -1 << endl;
	}
	else
	{
		cout << min_gn << endl;
	}

	return 0;
}