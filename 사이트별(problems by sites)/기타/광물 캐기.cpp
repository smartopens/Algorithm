#include <string>
#include <vector>
#include <math.h>

using namespace std;

int min_co;
// 0:dia, 1: iron, 2:stone
int picks[3];
int minerals[50];

int n;

// ¹Ì³×¶ö ¼ø¼­, °î±ªÀÌ »óÅÂ, °î±ªÀÌ Á¾·ù, ÇÇ·Îµµ
void get_mineral(int a, int p_tm, int now_p, int co)
{
    // ¸ðµç ±¤¹°À» Äµ °æ¿ì
    if (a > n - 1)
    {
        if (min_co > co)
        {
            min_co = co;
        }
        return;
    }

    // °î±ªÀÌ ¼ÒÁøµÈ °æ¿ì
    if (p_tm == 0)
    {
        bool can_get = false;
        for (int s = 0; s < 3; s++)
        {
            if (picks[s] <= 0) continue;
            can_get = true;
        }

        if (can_get == true)
        {
            for (int s = 0; s < 3; s++)
            {
                if (picks[s] <= 0) continue;
                picks[s] -= 1;
                get_mineral(a, 5, s, co);
                picks[s] += 1;
            }
        }
        else
        {
            if (min_co > co)
            {
                min_co = co;
            }
            return;
        }

    }
    // °î±ªÀÌ »ç¿ë Áß
    else
    {
        int mn = 0;

        mn = now_p - minerals[a];
        if (mn < 0)
        {
            mn = 0;
        }

        if (min_co >= co + pow(5, mn))
        {
            get_mineral(a + 1, p_tm - 1, now_p, co + pow(5, mn));
        }

    }
}

int solution(vector<int> picks_vec, vector<string> minerals_vec) {
    min_co = 21e8;
    n = minerals_vec.size();

    for (int s = 0; s < 3; s++)
    {
        picks[s] = picks_vec[s];
    }

    for (int s = 0; s < n; s++)
    {
        if (minerals_vec[s] == "diamond")
        {
            minerals[s] = 0;
        }
        else if (minerals_vec[s] == "iron")
        {
            minerals[s] = 1;
        }
        else if (minerals_vec[s] == "stone")
        {
            minerals[s] = 2;
        }
    }

    get_mineral(0, 0, 0, 0);
    return min_co;
}