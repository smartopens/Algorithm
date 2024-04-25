#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int m_r, m_c;

char s_map[12][12];
char s_map_back[12][12];

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

int main()
{
	cin >> m_r >> m_c;
	string in_smap;
	for (int r = 0; r < m_r; r++)
	{
		cin >> in_smap;
		for (int c = 0; c < m_c; c++)
		{
			s_map[r][c] = in_smap[c];
		}
	}

	//memcpy(s_map_back, s_map, sizeof(s_map));

	for (int r = 0; r < m_r; r++)
	{
		for (int c = 0; c < m_c; c++)
		{
			s_map_back[r][c] = s_map[r][c];
		}
	}

	int near_gn = 0;
	for (int r = 0; r < m_r; r++)
	{
		for (int c = 0; c < m_c; c++)
		{
			if (s_map_back[r][c] == 'X')
			{
				int tr, tc;
				near_gn = 0;
				for (int di = 0; di < 4; di++)
				{
					tr = r + dr[di];
					tc = c + dc[di];

					if (0 > tr || m_r - 1 < tr || 0 > tc || m_c - 1 < tc) continue;
					if (s_map_back[tr][tc] == 'X')
					{
						near_gn += 1;
					}
				}

				if (near_gn < 2)
				{
					s_map[r][c] = '.';
				}
			}
		}
	}

	int min_r = 12;
	int min_c = 12;
	int max_r = -1;
	int max_c = -1;
	
	for (int r = 0; r < m_r; r++)
	{
		for (int c = 0; c < m_c; c++)
		{
			if (s_map[r][c] == 'X')
			{
				min_r = min(min_r, r);
				min_c = min(min_c, c);
				
				max_r = max(max_r, r);
				max_c = max(max_c, c);
			}
		}
	}

	for (int r = min_r; r < max_r+1; r++)
	{
		for (int c = min_c; c < max_c+1; c++)
		{
			cout << s_map[r][c];
		}
		cout << endl;
	}
	return 0;
}