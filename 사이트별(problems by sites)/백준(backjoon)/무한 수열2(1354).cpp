#include <iostream>
#include <unordered_map>

using namespace std;

typedef long long ll;

ll n;
int p, q, x, y;

ll an;

//nv1, nv2, nv3, ... nv4, nv9, ...
//(2,4,3,10) , (5,2,8,...)
// 형변환 복습

unordered_map<ll, ll> an_reco;

ll get_num(ll a)
{
	if (a <= 0)
	{
		return 1;
	}

	if (an_reco[a] != 0)
	{
		return an_reco[a];
	}

	ll tar_an;
	tar_an = get_num((ll)a / p - x) + get_num((ll)a / q - y);

	return an_reco[a] = tar_an;
}

int main()
{
	cin >> n >> p >> q >> x >> y;
	an = get_num(n);

	cout << an << "\n";
	return 0;
}    