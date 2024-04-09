#include <iostream>
#include <math.h>

using namespace std;

int n;
int max_n;

int tar_n[250002];
int p_n;

void prime_count()
{
	for (int fv = 2; fv < sqrt(max_n)+1; fv++)
	{
		// 소수라고 생각되는 경우를 보기
		if (tar_n[fv] == 0) continue;
		for (int sv = 2; sv < max_n + 1; sv++)
		{
			if (fv * sv > max_n) break;
			tar_n[fv * sv] = 0;
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	max_n = 250000;
	for (int tv = 1; tv < max_n + 1; tv++)
	{
		tar_n[tv] = 1;
	}

	prime_count();

	//for (int tv = 1; tv < 50; tv++)
	//{
	//	if (tar_n[tv] == 0) continue;
	//	cout << tv << " ";
	//}
	while (true)
	{
		cin >> n;
		if (n == 0) break;

		p_n = 0;
		for (int tv = n+1; tv < 2 * n + 1; tv++)
		{
			if (tar_n[tv] != 0)
			{
				p_n += 1;
			}
		}

		cout << p_n << endl;
	}
	return 0;
}