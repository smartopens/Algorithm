#include <iostream>
#include <vector>

using namespace std;

// 파이프: 3방향
// 가로: 우앞, 대각앞 / 세로: 아앞, 대각앞 / 대각: 우앞, 아앞, 대각앞
// t1, t2, t3

int n;
int p_board[17][17];

int vr, vc, vs;

// (dr,dc,ns)
struct m_no {
	int dr;
	int dc;
	int ns;
};

vector<m_no> m_ref[3];

int mn;

void m_count(int vr, int vc, int vs){

	int to_r, to_c, to_s;
	
	if (vr == n && vc == n)
	{
		mn += 1;
		return;
	}

	for (int s = 0; s < m_ref[vs].size(); s++)
	{
		to_r = vr + m_ref[vs][s].dr;
		to_c = vc + m_ref[vs][s].dc;
		to_s = m_ref[vs][s].ns;

		if(to_s == 2)
		{
			if (1 > to_r || n < to_r || 1 > to_c || n < to_c) continue;
			if (1 > to_r-1 || n < to_r-1 || 1 > to_c || n < to_c) continue;
			if (1 > to_r || n < to_r || 1 > to_c-1 || n < to_c-1) continue;

			if (p_board[to_r][to_c] != 0) continue;
			if (p_board[to_r-1][to_c] != 0) continue;
			if (p_board[to_r][to_c-1] != 0) continue;

			m_count(to_r, to_c, to_s);
		}
		else{
			if (1 > to_r || n < to_r || 1 > to_c || n < to_c) continue;

			if (p_board[to_r][to_c] != 0) continue;
			m_count(to_r, to_c, to_s);
		}
	}
	return;
}

int main()
{
	cin >> n;
	for (int r = 1; r < n+1; r++)
	{
		for (int c = 1; c < n+1; c++)
		{
			cin >> p_board[r][c];
		}
	}

	vr = 1, vc = 2;
	vs = 0;

	// 가로, 세로, 대각
	
	// 가로
	m_ref[0].push_back({ 0,1,0 });
	m_ref[0].push_back({ 1,1,2 });

	// 세로
	m_ref[1].push_back({ 1,0,1 });
	m_ref[1].push_back({ 1,1,2 });

	// 대각
	m_ref[2].push_back({ 0,1,0 });
	m_ref[2].push_back({ 1,0,1 });
	m_ref[2].push_back({ 1,1,2 });

	m_count(1,2,0);

	cout << mn << endl;
	return 0;
}