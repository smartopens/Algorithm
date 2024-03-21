#include <iostream>
#include <queue>

using namespace std;

struct t_no
{
	int v;
	t_no* Left;
	t_no* Right;
};

t_no* tv_create(int t_data)
{
	t_no* new_tv = new t_no();
	new_tv->v = t_data;
	new_tv->Left = NULL;
	new_tv->Right = NULL;

	return new_tv;
}

void tv_insert(t_no* b_tree, int data)
{
	t_no* new_tv = tv_create(data);
	t_no* tmp_ptr = NULL;
	t_no* now_ptr = b_tree;

	while (now_ptr != NULL)
	{
		tmp_ptr = now_ptr;
		if (new_tv->v < now_ptr->v)
		{
			now_ptr = now_ptr->Left;
		}
		else
		{
			now_ptr = now_ptr->Right;
		}
	}

	if (new_tv->v < tmp_ptr->v)
	{
		tmp_ptr->Left = new_tv;
	}
	else
	{
		tmp_ptr->Right = new_tv;
	}
}

void post_order(t_no * b_tree)
{
	if (b_tree == NULL) return;

	post_order(b_tree->Left);
	post_order(b_tree->Right);
	cout << b_tree->v << endl;
}

int main()
{
	int tv;
	queue<int> t_info = {};
	while (cin >> tv)
	{
	/*	if (tv == -100)
		{
			break;
		}*/

		t_info.push(tv);
	}

	int r_no = t_info.front();
	t_info.pop();
	
	t_no* b_tree = tv_create(r_no);
	
	int t_data;
	while (!t_info.empty())
	{
		t_data = t_info.front();
		t_info.pop();

		tv_insert(b_tree, t_data);
	}

	post_order(b_tree);
	return 0;
}