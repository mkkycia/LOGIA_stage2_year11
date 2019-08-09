def ilep(s):
    wynik = 0
    for i in range(1, len(s)):
        for j in range(len(s)-i+1):
            print(s[j:])
            if s[j:][:i] == s[j:][:i][::-1]:
                wynik += 1
    if s == s[::-1]:
        wynik += 1
    return wynik

print(ilep('mama'))


        
