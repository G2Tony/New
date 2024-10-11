def word_length(s):
    words = s.split()
    return min(len(i) for i in words)

print(word_length("hello world"))