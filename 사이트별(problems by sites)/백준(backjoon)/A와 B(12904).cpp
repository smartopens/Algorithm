#include <iostream>
#include <string>

using namespace std;

string in_s;
string t;

bool can_convert;

int main()
{
	cin >> in_s;
	cin >> t;

	can_convert = false;

	string res_t;
	
	while (t.length() != in_s.length())
	{
		if (t.back() == 'A')
		{
			t.pop_back();
		}
		else
		{
			t.pop_back();
			res_t = "";
			for (int s = t.length() - 1; s > -1; s--)
			{
				res_t = res_t + t[s];
			}
			t = res_t;
		}
	}

	if (t != in_s)
	{
		cout << 0 << "\n";
	}
	else
	{
		cout << 1 << "\n";
	}
	return 0;
}