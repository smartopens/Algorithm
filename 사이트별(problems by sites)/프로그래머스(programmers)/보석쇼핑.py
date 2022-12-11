def solution(gems):
    res = []
    start = 0
    end = 0

    s_gems = set(gems)
    gem_num = len(s_gems)
    max_gem = len(gems)
    gem_dict = {gems[0]: 1}
    answer = [0, max_gem]

    while end != max_gem and start != max_gem:

        if len(gem_dict) < gem_num:
            end += 1
            if end >= max_gem:
                break
            gem_dict[gems[end]] = gem_dict.get(gems[end], 0) + 1
        else:
            if end - start < (answer[1] - answer[0]):
                answer = [start, end]

            if gem_dict[gems[start]] == 1:
                del gem_dict[gems[start]]
            else:
                gem_dict[gems[start]] -= 1

            start += 1

    answer[0] += 1
    answer[1] += 1
    return answer