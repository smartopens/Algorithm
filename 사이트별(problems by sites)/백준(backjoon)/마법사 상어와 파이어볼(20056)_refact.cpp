#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

// 파이어볼들이 대기하고 있다. (방향, 속도, 질량)
// 파이어볼은 방향, 속도를 고려해 이동한다.

// 이동 후: 파이어볼이 합쳐지고 나뉜다.
// 나뉘는 조건
// 질량- 질량합/5, 속력- 속력합/볼개수
// 방향: 파이어볼의 기존 방향 고려

int n, m, k;

struct f_no
{
	int r;
	int c;
	int fm;
	int fs;
	int di;
};

vector<f_no> f_map[52][52];
vector<f_no> f_map_back[52][52];
vector<f_no> f_balls;

vector<f_no> f_map1[2][2];
vector<f_no> f_map_back1[52][52];

int dr[8] = {-1,-1,0,1,1,1,0,-1};
int dc[8] = {0,1,1,1,0,-1,-1,-1};

int f_sum;
void f_magic()
{
	// 파이어볼 이동
	for (int r = 1; r < n + 1; r++)
	{
		for (int c = 1; c < n + 1; c++)
		{
			f_map[r][c].clear();
		}
	}

	int to_r, to_c;
	int fm, fs, fdi;
	for (int s = 0; s < f_balls.size(); s++)
	{
		// 이동
		// 유의할점!
		fs = f_balls[s].fs;
		fdi = f_balls[s].di;
		fm = f_balls[s].fm;

		int to_fs = fs%n;
		to_r = f_balls[s].r + dr[fdi] * to_fs;
		to_c = f_balls[s].c + dc[fdi] * to_fs;

		if (1 > to_r)
		{
			to_r = n + to_r;
		}
		if (1 > to_c)
		{
			to_c = n + to_c;
		}
		if (n < to_r)
		{
			to_r -= n;
		}
		if (n < to_c)
		{
			to_c -= n;
		}

		//if (0 > to_r || n-1 < to_r || 0 > to_c || n-1 < to_c) continue;
		f_map[to_r][to_c].push_back({ to_r,to_c,fm,fs,fdi });
		f_balls[s].r = to_r;
		f_balls[s].c = to_c;
	}

	//for (int r = 1; r < n + 1; r++)
	//{
	//	for (int c = 1; c < n + 1; c++)
	//	{
	//		f_map[r][c].clear();
	//		for (int s = 0; s < f_map_back[r][c].size(); s++)
	//		{
	//			f_map[r][c].push_back(f_map_back[r][c][s]);
	//		}
	//		//f_map[r][c] = f_map_back[r][c];
	//	}
	//}
	
	// 파이어볼 융합
	vector<f_no> f_balls_back = {};
	int fm_sum, fs_sum;
	int f_on, f_en, f_size;
	for (int r = 1; r < n + 1; r++)
	{
		for (int c = 1; c < n + 1; c++)
		{
			if (f_map[r][c].size() == 1)
			{
				f_balls_back.push_back(f_map[r][c][0]);
			}
			else if (f_map[r][c].size() > 1)
			{
				fm_sum = 0;
				fs_sum = 0;
				f_on = 0;
				f_en = 0;
				bool all_odd = true;
				bool all_even = true;
				f_size = f_map[r][c].size();
				for (int s = 0; s < f_size; s++)
				{
					fm_sum += f_map[r][c][s].fm;
					fs_sum += f_map[r][c][s].fs;
					fdi = f_map[r][c][s].di;

					if (fdi % 2 == 0)
					{
						all_odd = false;
						f_en += 1;
					}
					else if (fdi % 2 == 1)
					{
						all_even = false;
						f_on += 1;
					}
				}

				fm_sum /= 5;
				fs_sum /= f_size;

				//f_map[r][c].clear();
				if (fm_sum > 0)
				{
					// 상하좌우
					if(all_even == true  || all_odd == true)
					{
						for (int i = 0; i < 8; i += 2)
						{
							f_balls_back.push_back({ r,c, fm_sum, fs_sum, i });
						}
					}
					//대각선
					else
					{
						for (int i = 1; i < 8; i += 2)
						{
							f_balls_back.push_back({ r,c,fm_sum, fs_sum, i });
						}
					}
				}
				
			}
		}
	}
	f_balls = f_balls_back;
}

int main()
{
	cin >> n >> m >> k;
	int r, c, fm, s, d;
	for (int i = 0; i < m; i++)
	{
		cin >> r >> c >> fm >> s >> d;
		/*r -= 1;
		c -= 1;*/

		//f_map[r][c].push_back({ r,c, fm,s,d });
		f_balls.push_back({ r,c, fm,s,d });
	}

	while (k > 0)
	{
		f_magic();
		k -= 1;
	}

	f_sum = 0;
	for (int s = 0; s < f_balls.size(); s++)
	{
		f_sum += f_balls[s].fm;
	}

	cout << f_sum << endl;

	/*f_map1[0][0].push_back({ 1,1,1 });
	f_map_back1[0][0] = f_map1[0][0];
	f_map_back1[0][0].clear();
	f_map_back1[0][0] = f_map1[0][0];
	cout << f_map_back1[0][0][0].fm << " "<< f_map_back1[0][0][0].fs << " "<< f_map_back1[0][0][0].di << endl;*/
	return 0;
}