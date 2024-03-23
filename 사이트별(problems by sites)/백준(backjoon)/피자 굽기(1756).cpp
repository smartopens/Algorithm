#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

// ���� ������ ���쿡 �ֱ�
// ����: D���� ������ �̷���� (���� ��)
// ���� �ֻ�� ������ ���̸� ���ϱ�

int d, n;

vector<int> p_oven;
queue<int> p_oven_tmp;
vector<int> p_info;

int vi[300002];

int main()
{
	cin >> d >> n;
	int p_in;
	for (int i = 0; i < d; i++)
	{
		cin >> p_in;
		p_oven.push_back(p_in);

		if (i == 0) continue;
		if (p_in > p_oven[i - 1])
		{
			p_oven[i] = p_oven[i - 1];
		}
	}

	int p_r;
	for (int s = 0; s < n; s++)
	{
		cin >> p_r;
		p_info.push_back(p_r);
	}

	// ��: �ݴ�
	int o_id = d - 1;
	int p_id = 0;
	while (o_id > -1)
	{
		// ���ڰ� ���캸�� Ŭ ���
		if (p_info[p_id] > p_oven[o_id])
		{
			o_id -= 1;
		}
		// ���ڰ� ���쿡 ���� ���
		else
		{
			p_id += 1;
			o_id -= 1;
		}

		// ��� ���ڸ� ä�� ���
		if (p_id == n)
		{
			o_id += 1;
			break;
		}
	}

	bool p_ok = false;

	if (p_id >= n)
	{
		p_ok = true;
	}

	if (p_ok == false)
	{
		cout << 0 << endl;
	}
	else
	{
		cout << o_id+1 << endl;
	}

	return 0;
}