def maximizedNumber(num):
    s = list(str(num))
    for i in range(len(s)):
        maxi = int(s[i])
        idx = i
        for j in range(i + 1, len(s)):
            if ((maxi % 2 == 0) and (int(s[j]) % 2 == 0)):
                if (int(s[j]) > maxi):
                    maxi = int(s[j])
                    idx = j
            elif ((maxi % 2 == 1) and (int(s[j]) % 2 == 1)):
                if (int(s[j]) > maxi):
                    maxi = int(s[j])
                    idx = j
        s[i], s[idx] = s[idx], s[i]
    return ''.join(s)
N = int(input())
print(maximizedNumber(N))