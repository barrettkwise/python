def lengthOfLongestSubstring(self, s: str) -> int:
    last_seen = {}
    last = 0
    best = 0

    for i, c in enumerate(s):
        cur_len = min(i - last_seen.setdefault(c, -1), last + 1)
        last_seen[c] = i
        if cur_len > best:
            best = cur_len
        last = cur_len

        return best
