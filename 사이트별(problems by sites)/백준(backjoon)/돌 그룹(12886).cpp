#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

vector<int> d_size;
int d_pair[3002][3002];

int d_selected[2];

bool can_s;

bool next_c;
int c_dv1, c_dv2;

void d_divide()
{
	vector<int> d_size_back = {};
	d_size_back = d_size;
	next_c = false;

	if(d_size[0] == d_size[1] && d_size[1] == d_size[2])
	{
		can_s = true;
		return;
	}
	
	for (int fs = 0; fs < 3; fs++)
	{
		for (int ss = fs+1; ss < 3; ss++)
		{
			c_dv1 = min(d_size[fs], d_size[ss]);
			c_dv2 = max(d_size[fs], d_size[ss]);

			c_dv2 -= c_dv1;
			c_dv1 *= 2;

			if (d_pair[c_dv1][c_dv2] == 0)
			{
				d_pair[c_dv1][c_dv2] = 1;
				d_pair[c_dv2][c_dv1] = 1;

				d_size[fs] = c_dv1;
				d_size[ss] = c_dv2;

				d_divide();

				d_size = d_size_back;
				if (can_s == true) return;
			}
		}
	}
}

int main()
{
	int in_a, in_b, in_c;
	cin >> in_a >> in_b >> in_c;
	d_size.push_back(in_a);
	d_size.push_back(in_b);
	d_size.push_back(in_c);

	d_pair[in_a][in_b] = 1;
	d_pair[in_b][in_c] = 1;
	d_pair[in_a][in_c] = 1;
	d_pair[in_b][in_a] = 1;
	d_pair[in_c][in_b] = 1;
	d_pair[in_c][in_a] = 1;

	can_s = false;
	d_divide();

	if (can_s == false)
	{
		cout << 0 << "\n";
	}
	else
	{
		cout << 1 << "\n";
	}
	return 0;
}
