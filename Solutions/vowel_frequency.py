def vowel_frequency(text):
    vowels = 'AEIOU'
    frequency = {vowel: 0 for vowel in vowels}
    for char in text:
        if char in vowels:
            frequency[char] += 1
    return frequency