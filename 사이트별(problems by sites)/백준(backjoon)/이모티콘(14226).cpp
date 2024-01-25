#include <iostream>
#include <queue>

using namespace std;

int tar_en;

struct e_no
{
	int en;
	int cn;
	int add_n;
	int st_n;
};

int vi[2002][20][20];
int min_tm;

void make_emo()
{
	queue<e_no> eq = {};
	eq.push({ 1,0,0,0 });
	vi[1][0][0] = 1;

	while (!eq.empty())
	{
		e_no ev = eq.front();
		eq.pop();

		// 이모티콘 조작하기
		int to_en = 0;
		int now_en = ev.en;
		int now_cn = ev.cn;
		int now_add_n = ev.add_n;

		if (now_en == tar_en)
		{
			//cout << "cl" << endl;
			min_tm = vi[ev.en][ev.add_n][ev.st_n] - 1;
			return;
		}

		//cout << now_en << endl;
		// 화면 붙여넣기
		if (ev.cn != 0)
		{
			to_en = now_en + now_cn;

			if (to_en <= 2000)
			{
				//cout << to_en;
				if (vi[to_en][ev.add_n + 1][ev.st_n] == 0)
				{
					vi[to_en][ev.add_n + 1][ev.st_n] = vi[ev.en][ev.add_n][ev.st_n] + 1;
					eq.push({ to_en, now_cn, now_add_n + 1, ev.st_n });
				}
			}
		}
		// 클립 복사
		to_en = now_en;
		if (vi[to_en][ev.add_n][ev.st_n + 1] == 0)
		{
			vi[to_en][ev.add_n][ev.st_n + 1] = vi[ev.en][ev.add_n][ev.st_n] + 1;
			eq.push({ to_en, now_en, now_add_n ,ev.st_n + 1 });
		}

		// e 삭제
		to_en = now_en - 1;
		if (to_en >= 1)
		{
			if (vi[to_en][ev.add_n][ev.st_n] == 0)
			{
				vi[to_en][ev.add_n][ev.st_n] = vi[ev.en][ev.add_n][ev.st_n] + 1;
				eq.push({ to_en, now_cn, now_add_n ,ev.st_n });
			}
		}

	}
}

int main()
{
	cin >> tar_en;
	min_tm = 21e8;

	make_emo();
	cout << min_tm << endl;
	return 0;
}