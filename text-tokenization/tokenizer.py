import re


with open("sample_text.txt", "r") as file:
    text = file.read()

print("Original Text:\n")
print(text)

whitespace_tokens = text.split()

print("\nWhitespace Tokenization:")
print(whitespace_tokens)
regex_tokens = re.findall(r'\b\w+\b', text)

print("\nRegex Tokenization (Improved):")
print(regex_tokens)

clean_tokens = [token.lower() for token in regex_tokens]

print("\nLowercase Clean Tokens:")
print(clean_tokens)

print("\nTotal Tokens (Regex):", len(clean_tokens))
