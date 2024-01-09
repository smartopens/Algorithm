#include <iostream>
#include <string>
#include <vector>

using namespace std;

string whole_st;
string front_st;
string tar_st;

int n;

void boom_str()
{
	string now_st = "";
	int n_id = 0;
	for (int sv = 0; sv < n; sv++)
	{
		front_st += whole_st[sv];

		if (whole_st[sv] == tar_st[tar_st.length() - 1])
		{
			if (front_st.length() >= tar_st.length())
			{
				bool is_tar = true;
				for (int s = 0; s < tar_st.length(); s++)
				{
					if (front_st[front_st.length() - 1-s] != tar_st[tar_st.length() -1- s])
					{
						is_tar = false;
						break;
					}
				}

				if (is_tar)
				{
					for (int s = 0; s < tar_st.length(); s++)
					{
						front_st.pop_back();
					}
				}
			}
		}
		//if (tar_st[n_id] == whole_st[sv])
		//{
		//	now_st += whole_st[sv];
		//	n_id += 1;
		//}
		//else
		//{
		//	now_st = "";
		//	n_id = 0;
		//	if (tar_st[n_id] == whole_st[sv])
		//	{
		//		now_st = whole_st[sv];
		//		n_id += 1;
		//	}
		//}
		

		//if (now_st == tar_st)
		//{
		//	front_st = front_st.substr(0, front_st.length() - tar_st.length());
		//	now_st = "";
		//	n_id = 0;

		//	// 전체 tar_st 길이만큼 본다.
		//	int s_id = front_st.length() - tar_st.length();
		//	string tmp_st = "";
		//	int t_size = tar_st.length();

		//	//cout << front_st << endl;
		//	// now_st 갱신하기
		//	while (s_id < 0)
		//	{
		//		s_id += 1;
		//		t_size -= 1;
		//	}

		//	if (s_id >= 0)
		//	{
		//		for (int s = s_id; s < front_st.length(); s++)
		//		{
		//			tmp_st = front_st.substr(s, front_st.length());

		//			//cout << tmp_st << endl;
		//			// now_st 갱신하기
		//			if (tmp_st == tar_st.substr(0, t_size))
		//			{
		//				now_st = tmp_st;
		//				n_id = t_size;
		//				/*cout << "c" << endl;
		//				cout << n_id << endl;
		//				cout << now_st << endl;*/
		//				break;
		//			}

		//			t_size -= 1;
		//		}
		//		s_id += 1;
		//	}
		//}
	}

}

int main()
{
	/*string tmp = "exact";
	string tmp2 = "act";

	cout << tmp.substr(0, tmp.length() - tmp2.length());*/
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> whole_st;
	cin >> tar_st;
	n = whole_st.length();

	boom_str();

	if (front_st.length() == 0)
	{
		cout << "FRULA" << endl;
	}
	else
	{
		cout << front_st << endl;
	}
	return 0;
}