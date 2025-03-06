def reverseWords(s: str) -> str:
    words = s.split()
    return " ".join(reversed(words))

s = "the sky is blue"
print(reverseWords(s))