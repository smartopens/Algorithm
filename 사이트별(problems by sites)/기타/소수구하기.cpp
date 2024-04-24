#include <iostream>
#include <math.h>

using namespace std;

int p_nums[1002];

void p_reco(int max_n)
{
	int mn;
	for (int fv = 2; fv < sqrt(max_n) + 1; fv++)
	{
		// 자기 자신을 제외한 배수 기록하기
		if (p_nums[fv] == 0) continue;
		mn = 2;
		while(mn*fv < max_n+1)
		{
			p_nums[fv * mn] = 0;
			mn += 1;
		}
	}
}

int main()
{
	for (int s = 2; s < 1001; s++)
	{
		p_nums[s] = 1;
	}

	p_reco(1000);

	for (int s = 2; s < 1001; s++)
	{
		if (p_nums[s] == 0) continue;
		cout << s << " ";
	}
	return 0;
}