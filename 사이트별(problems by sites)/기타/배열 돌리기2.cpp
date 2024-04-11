#include <iostream>
#include <vector>

using namespace std;

int n, m;
int cn;

int sr, sc;
int er, ec;

vector<vector<int>> arr_nums;
int init_nums[302][302];

int main()
{

	cin >> n >> m >> cn;

	sr = 0;
	sc = 0;
	er = n-1;
	ec = m-1;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cin >> init_nums[r][c];
		}
	}

	vector<int> arr_num = {};
	while (sr < er && sc < ec)
	{
		// 외곽부터 배열 숫자 기록하기
		// 상 우 하 좌
		arr_num.clear();
		for (int c=sc; c<ec; c++)
		{
			arr_num.push_back(init_nums[sr][c]);
		}
		for (int r = sr; r < er; r++)
		{
			arr_num.push_back(init_nums[r][ec]);
		}
		for (int c = ec; c > sc; c--)
		{
			arr_num.push_back(init_nums[er][c]);
		}
		for (int r = er; r > sr; r--)
		{
			arr_num.push_back(init_nums[r][sc]);
		}

		//for (int i = 0; i < arr_num.size(); i++)
		//{
		//	cout << arr_num[i] << " ";
		//}
		//cout << endl;
		arr_nums.push_back(arr_num);
		sr += 1;
		sc += 1;
		er -= 1;
		ec -= 1;
	}

	//cout << arr_nums.size() << endl;
	//for (int s = 0; s < arr_nums.size(); s++)
	//{
	//	for (int i = 0; i < arr_nums[s].size(); i++)
	//	{
	//		cout << arr_nums[s][i] << " ";
	//	}
	//	cout << endl;
	//}

	int num_s = 0;
	int now_cn;
	for (int s = 0; s < arr_nums.size(); s++)
	{
		num_s = arr_nums[s].size();
		now_cn = cn % num_s;
		for (int i = 0; i < now_cn; i++)
		{
			arr_nums[s].push_back(arr_nums[s][0]);
			arr_nums[s].erase(arr_nums[s].begin());
		}
	}

	sr = 0;
	sc = 0;
	er = n - 1;
	ec = m - 1;

	int a_id = 0;
	while (sr < er && sc < ec)
	{
		// 외곽부터 회전 후의 배열 숫자 기록하기
		// 상 우 하 좌
		int a_in_id = 0;
		for (int c = sc; c < ec; c++)
		{
			init_nums[sr][c] = arr_nums[a_id][a_in_id];
			a_in_id += 1;
		}
		for (int r = sr; r < er; r++)
		{
			init_nums[r][ec] = arr_nums[a_id][a_in_id];
			a_in_id += 1;
		}
		for (int c = ec; c > sc; c--)
		{
			init_nums[er][c] = arr_nums[a_id][a_in_id];
			a_in_id += 1;
		}
		for (int r = er; r > sr; r--)
		{
			init_nums[r][sc] = arr_nums[a_id][a_in_id];
			a_in_id += 1;
		}

		sr += 1;
		sc += 1;
		er -= 1;
		ec -= 1;
		a_id += 1;
	}

	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cout << init_nums[r][c] << " ";
		}
		cout << endl;
	}
	return 0;
}