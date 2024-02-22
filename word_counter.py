# word_counter.py

def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    text = input("Enter text: ")
    word_count = count_words(text)
    print("Number of words:", word_count)
