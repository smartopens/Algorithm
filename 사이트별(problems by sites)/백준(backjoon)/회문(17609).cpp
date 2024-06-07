#include <iostream>
#include <string>

using namespace std;

int t;

int main()
{
	cin >> t;
	for (int tc = 0; tc < t; tc++)
	{
		string now_com;
		cin >> now_com;

		bool c_ok = true;
		int c_num = 0;
		int ls = 0;
		int rs = now_com.length() - 1;

		while (ls < rs)
		{
			if (now_com[ls] != now_com[rs])
			{
				if (c_num == 0)
				{
					// 정방향이 다를 경우
					if (now_com[ls + 1] == now_com[rs])
					{
						c_num += 1;
						ls += 1;
					}
					else if (now_com[ls] == now_com[rs-1])
					{
						c_num += 1;
						rs -= 1;
					}
					/*else if (now_com.length()%2 == 1 && ls == now_com.length() / 2-1)
					{
						c_num = 1;
						break;
					}*/
					else
					{
						c_num = 2;
						break;
						// se esu
					}
				}
				else
				{
					c_ok = false;
					break;
				}
			}
			else
			{
				ls += 1;
				rs -= 1;
			}
		}

		if (c_ok == true && c_num == 0)
		{
			cout << 0 << "\n";
		}
		else if (c_ok == true && c_num == 1)
		{
			cout << 1 << "\n";
		}
		else
		{
			cout << 2 << "\n";
		}
	}
	return 0;
}