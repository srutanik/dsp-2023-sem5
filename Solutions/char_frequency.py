def char_frequency(text, character):
    frequency=0
    for char in text:
        if char==character:
            frequency += 1
    return frequency