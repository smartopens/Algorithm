#include <iostream>
#include <math.h>
#include <string>

using namespace std;

int k;

int main()
{
	int fv = 0;
	int now_v = 0;
	int mn = 1;
	
	cin >> k;
	// 2, 4, 8, ...
	// 자리수 맞춰주기
	while (true)
	{
		fv += pow(2,mn);

		if (fv >= k) break;
		mn += 1;
	}

	fv -= pow(2, mn);
	now_v = k - fv-1;

	string s_num = "";
	for (int s = 0; s < mn; s++)
	{
		s_num = s_num + '4';
	}

	int s_id = mn - 1;
	while (now_v != 0)
	{
		if (now_v % 2 == 0)
		{
			s_num[s_id] = '4';
		}
		else
		{
			s_num[s_id] = '7';
		}

		now_v /= 2;
		s_id -= 1;
		/*if (now_v < pow(2, mn) || now_v <= 1)
		{
			s_num = s_num + '4';
		}
		else
		{
			s_num = s_num + '7';
			now_v -= pow(2, mn);
		}

		if (mn == 0) break;
		mn -= 1;*/

	}
	
	cout << s_num << "\n";
	return 0;
}