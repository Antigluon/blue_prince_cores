import itertools as it

def decode_letter(letter):
    return ord(letter.upper()) - ord("A") + 1 

def encode_letter(number):
    if number < 1 or number > 26:
        return "?"
    if number != int(number):
        return "?"
    return chr(number + ord("A") - 1)

def decode_word(word):
    return [decode_letter(letter) for letter in word]

def encode_word(numbers):
    return [encode_letter(n) for n in numbers]

def core(a, b, c, d):
    v1 = ((a - b) * c) / d 
    v2 = ((a - b) / c) * d 
    v3 = ((a * b) - c) / d 
    v4 = ((a * b) / c) - d 
    v5 = ((a / b) - c) * d 
    v6 = ((a / b) * c) - d 
    values = (v1,v2,v3,v4,v5,v6)

    return min([int(v) for v in values if v > 0 and v == int(v)], default=0)

with open("wordlist.txt") as f:
    wordlist = sum((
        line.strip().split() for line in f.readlines()
    ), [])

cores = [core(*decode_word(word)) for word in wordlist]
print("Numerical cores:")
for batch in it.batched(cores, 5):
    print("\t".join((
        f"{n:>2}" for n in batch
    )))
print()
print("They spell:")
for batch in it.batched(cores, 5):
    print(" ".join(encode_word(batch)))
