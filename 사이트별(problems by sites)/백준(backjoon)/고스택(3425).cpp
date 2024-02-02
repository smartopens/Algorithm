#include <iostream>
#include <vector>
#include <string>

using namespace std;

// 스택과 연산(10가지 종류)가 있다.
// 나누기를 할때 부호 규칙이 있다.

struct s_no
{
	string pro;
	long long p_n;
};

vector<s_no> pros;
vector<long long> go_st;
int n;

bool is_err;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	string now_p;
	while (true)
	{
		cin >> now_p;
		while (true)
		{
			//cout << now_p << endl;
			if (now_p == "QUIT")
			{
				break;
			}

			else if (now_p == "END")
			{
				cin >> n;
				long long in_n;
				for (int i = 0; i < n; i++)
				{
					is_err = false;
					cin >> in_n;
					go_st.clear();
					go_st.push_back(in_n);
					string run_p = "";
					long long f_n = 0;
					long long s_n = 0;
					long long to_n = 0;
					// 프로그램 실행
					for (int s = 0; s < pros.size(); s++)
					{
						run_p = pros[s].pro;
						if (run_p == "NUM")
						{
							go_st.push_back(pros[s].p_n);
						}
						else if (run_p == "POP")
						{
							if (go_st.size() < 1)
							{
								is_err = true;
								break;
							}
							go_st.pop_back();
						}
						else if (run_p == "INV")
						{
							if (go_st.size() < 1)
							{
								is_err = true;
								break;
							}

							f_n = go_st.back();
							go_st.pop_back();
							go_st.push_back(-f_n);
						}
						else if (run_p == "DUP")
						{
							f_n = go_st.back();
							go_st.push_back(f_n);
						}
						else if (run_p == "SWP")
						{
							if (go_st.size() < 2)
							{
								is_err = true;
								break;
							}

							f_n = go_st.back();
							go_st.pop_back();
							s_n = go_st.back();
							go_st.pop_back();

							go_st.push_back(f_n);
							go_st.push_back(s_n);
						}
						else if (run_p == "ADD")
						{
							if (go_st.size() < 2)
							{
								is_err = true;
								break;
							}

							f_n = go_st.back();
							go_st.pop_back();
							s_n = go_st.back();
							go_st.pop_back();


							to_n = f_n + s_n;
							if (abs(to_n) > 1e9)
							{
								is_err = true;
								break;
							}

							go_st.push_back(to_n);
						}
						else if (run_p == "SUB")
						{
							if (go_st.size() < 2)
							{
								is_err = true;
								break;
							}

							f_n = go_st.back();
							go_st.pop_back();
							s_n = go_st.back();
							go_st.pop_back();

							to_n = -f_n + s_n;
							if (abs(to_n) > 1e9)
							{
								is_err = true;
								break;
							}
							go_st.push_back(to_n);

						}
						else if (run_p == "MUL")
						{
							if (go_st.size() < 2)
							{
								is_err = true;
								break;
							}

							f_n = go_st.back();
							go_st.pop_back();
							s_n = go_st.back();
							go_st.pop_back();

							to_n = f_n * s_n;
							if (abs(to_n) > 1e9)
							{
								is_err = true;
								break;
							}
							go_st.push_back(to_n);
						}
						else if (run_p == "DIV")
						{
							if (go_st.size() < 2)
							{
								is_err = true;
								break;
							}

							f_n = go_st.back();
							go_st.pop_back();
							s_n = go_st.back();
							go_st.pop_back();

							if (f_n == 0)
							{
								is_err = true;
								break;
							}

							to_n = abs(s_n) / abs(f_n);
							if ((f_n < 0 && s_n >= 0) || (f_n >= 0 && s_n < 0))
							{
								go_st.push_back(-to_n);
							}
							else
							{
								go_st.push_back(to_n);
							}

						}
						else if (run_p == "MOD")
						{
							if (go_st.size() < 2)
							{
								is_err = true;
								break;
							}

							f_n = go_st.back();
							go_st.pop_back();
							s_n = go_st.back();
							go_st.pop_back();

							if (f_n == 0)
							{
								is_err = true;
								break;
							}

							to_n = abs(s_n) % abs(f_n);
							if (s_n < 0)
							{
								go_st.push_back(-to_n);
							}
							else
							{
								go_st.push_back(to_n);
							}

						}
					}

					if (go_st.size() != 1)
					{
						is_err = true;
					}

					if (is_err == true)
					{
						cout << "ERROR\n";
					}
					else
					{
						cout << go_st.back() << "\n";
					}

				}

				pros.clear();
				cout << "\n";
				break;
			}
			else
			{
				long long p_in_n;
				if (now_p == "NUM")
				{
					cin >> p_in_n;
					pros.push_back({ now_p, p_in_n });
				}
				else {
					pros.push_back({ now_p,0 });
				}
			}

			//pros.push_back({ now_p,0 });
			cin >> now_p;
		}

		if (now_p == "QUIT")
		{
			break;
		}

	}
	return 0;
}