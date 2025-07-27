from stats import count_words

def get_book_text(input_file):
    with open(input_file) as f:
        book_text = f.read()
    return book_text

def main():
    frankenstein_text = get_book_text("./books/frankenstein.txt")
    frankenstein_count = count_words(frankenstein_text)
    print(f"{frankenstein_count} words found in the document")

#Call to main
main()