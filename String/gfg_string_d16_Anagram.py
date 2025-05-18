def areAnagrams(s1, s2):
    return sorted(s1) == sorted(s2)
s1, s2 = "geeks", "kseeg"
print("true" if areAnagrams(s1, s2) else "false")
