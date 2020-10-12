#Recursive Brute Force

def Brute(String, length, set):
    if len(String) == length:
        return
    for char in set:
        temp = String + char
        print(temp)
        Brute(temp, length, set)

Brute("", 3, 'abcdefg')