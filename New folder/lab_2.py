from string import ascii_lowercase
def panagram(s):
    for i in ascii_lowercase:
        for i in range (len(s)):
            