def hiss(text):
    return text.replace('s', 'ss').replace('S', 'SS')

if __name__ == "__main__":
    sample = "Snake sounds are ssssuperb!"
    print(hiss(sample))