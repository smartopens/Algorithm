#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

char un_h_word[102];
int w_s;
int tar_idx[12];

int tar_s;
int h1_check[256];

char to_alpha[3] = { 'C','L','A' };

long long h_n;

bool h_check(int ws)
{
	int h1_n = 0;
	int h2_n = 0;
	for (int i = ws; i < ws + 3; i++)
	{
		if (i > w_s - 1) continue;
		if (un_h_word[i] == '_')
		{
			continue;
		}

		if (un_h_word[i] == 'A')
		{
			h1_n += 1;
		}
		else if (un_h_word[i] == 'C' || un_h_word[i] == 'L')
		{
			h2_n += 1;
		}
	}

	if (h1_n == 3)
	{
		return false;
	}

	if (h2_n == 3)
	{
		return false;
	}

	return true;
}

void make_happy(int a, long long now_h)
{
	if (a > tar_s - 1)
	{
		bool h3_ok = false;
		for (int s = 0; s < w_s; s++)
		{
			if (un_h_word[s] == 'L')
			{
				h3_ok = true;
				break;
			}
		}
		if (h3_ok == true)
		{
			h_n += now_h;
		}

		return;
	}
	int now_id = tar_idx[a];
	bool h_ok = true;
	char to_c = '\0';
	for (int i = 0; i < 3; i++)
	{
		h_ok = true;
		to_c = to_alpha[i];
		un_h_word[now_id] = to_c;
		for (int ws = now_id - 2; ws < now_id + 1; ws++)
		{
			if (ws < 0) continue;
			if (h_check(ws) == false)
			{
				h_ok = false;
			}
		}
		// L 아닌 자음
		if (h_ok == true && i == 0)
		{
			make_happy(a + 1, now_h * 20);
		}
		// L인 자음
		else if (h_ok == true && i == 1)
		{
			make_happy(a + 1, now_h);
		}
		// 모음
		else if (h_ok == true && i == 2)
		{
			make_happy(a + 1, now_h * 5);
		}
		un_h_word[now_id] = '_';
	}

}

int main()
{
	string in_word = "";
	cin >> in_word;
	w_s = in_word.length();
	tar_s = 0;
	h_n = 0;
	for (int s = 0; s < in_word.length(); s++)
	{
		if (in_word[s] == '_')
		{
			tar_idx[tar_s] = s;
			tar_s += 1;
			un_h_word[s] = '_';
		}
		else if (in_word[s] == 'A' || in_word[s] == 'E' || in_word[s] == 'I' ||
			in_word[s] == 'O' || in_word[s] == 'U')
		{
			un_h_word[s] = 'A';
		}
		else if (in_word[s] == 'L')
		{
			un_h_word[s] = 'L';
		}
		else
		{
			un_h_word[s] = 'C';
		}
	}

	bool un_happy = false;
	for (int s = 0; s < w_s - 2; s++)
	{
		if (w_s < 0) continue;
		if (h_check(s) == false)
		{
			h_n = 0;
			un_happy = true;
		}
	}

	if (un_happy == false)
	{
		make_happy(0, 1);
	}

	cout << h_n << endl;

	//cout << pow(6, 10);
	return 0;
}