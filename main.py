import string
def main():
    book_path = "./books/frankenstein.txt"
    text = get_text(book_path)
    words = count_words(text)

    print(create_report(count_characters(text),book_path, words))


def get_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(book):
    words = book.split()
    return len(words)

def count_characters(text):
    lowered_text = text.lower()
    num_chars = {}

    for x in lowered_text:
        if x not in num_chars and x.isalpha():
            num_chars[x] = 1
        elif x.isalpha():
            num_chars[x] += 1
        
    return num_chars

def create_report(charcount, title, wordcount):
    report = f"--- Begin report for {title} ---\n"
    report += f"There was a total of {wordcount} words\n"
    sorted_charcount =  dict(sorted(charcount.items(), key=lambda item: item[1], reverse=True))
    for char in sorted_charcount:
        report += f"The {char} occured {charcount[char]}\n"
    report+= "--- End report ---"
    return report

main()