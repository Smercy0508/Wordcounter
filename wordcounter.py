def count_words(text):
    return len(text.split())

def main():
    text = input("Enter some text: ")
    if not text:
        print("Error: No text entered.")
        return
    total_words = count_words(text)
    print(f"Total Words: {total_words}")

if __name__ == "__main__":
    main()