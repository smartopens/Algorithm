#include <iostream>
#include <vector>

using namespace std;

int n, m;
int gp[502][502];
int g_vi[502];

int g_num;

//void f_count(int now_f, int fd)
//{
//	int to_f;
//	for (int i = 0; i < gp[now_f].size(); i++)
//	{
//		to_f = gp[now_f][i];
//
//		if (g_vi[to_f] != 0) continue;
//		if (fd + 1 > 2) continue;
//
//		cout << to_f << endl;
//		g_num += 1;
//		g_vi[to_f] = 1;
//		f_count(to_f, fd+1);
//	}
//	return;
//}

int main()
{
	cin >> n;
	cin >> m;

	for (int i = 1; i < n+1; i++)
	{
		for (int j = 1; j < n+1; j++)
		{
			gp[i][j] = 3e8;
			if (i == j)
			{
				gp[i][j] = 0;
			}
		}
	}

	int f1, f2;
	for (int i = 0; i < m; i++)
	{
		cin >> f1 >> f2;
		gp[f1][f2] = 1;
		gp[f2][f1] = 1;
	}

	for (int k = 1; k < n+1; k++)
	{
		for (int i = 1; i < n+1; i++)
		{
			for (int j = 1; j < n+1; j++)
			{
				if(gp[i][k] != 3e8 && gp[k][j]!= 3e8 )
				{ 
					gp[i][j] = min(gp[i][j], gp[i][k] + gp[k][j]);
				}
			}
		}
	}

	//g_vi[1] = 1;
	//f_count(1, 0);

	for (int i = 2; i < n + 1; i++)
	{
		if (gp[1][i] < 3) g_num += 1;
	}
	cout << g_num << endl;
	return 0;
}
