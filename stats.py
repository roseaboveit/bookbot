def get_num_words(text):
    return len(text.split())

def get_char_distribution(text):
    distribution = {}
    for c in text:
        char = c.lower()
        if char in distribution:
            distribution[char] += 1
        elif char.isalpha():
            distribution[char] = 1
    return distribution

def sort_on(items):
    return items["num"]

def sort_distribution(dist):
    full_dist = []
    for k, v in dist.items():
        full_dist.append({"char": k, "num":v})
    full_dist.sort(reverse=True, key=sort_on)
    return full_dist
        