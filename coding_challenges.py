def is_anagram(s1: str, s2: str) -> bool:
    f1 = [c.lower() for c in s1 if 'a' <= c.lower() <= 'z']  # letters only
    f2 = [c.lower() for c in s2 if 'a' <= c.lower() <= 'z']
    return sorted(f1) == sorted(f2)

# quick tests
print(is_anagram("Dormitory", "Dirty room"))          # True
print(is_anagram("The Morse Code", "Here come dots")) # True
print(is_anagram("Hello", "Ole!"))        

# lambda; use sparingly
reversed_words = lambda sentence: ' '.join(piece[::-1] for piece in sentence.split(' '))
print(reversed_words("The man in the automobile runs faster than light!"))