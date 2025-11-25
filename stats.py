def get_word_count(book_text):

    words = book_text.split()

    return len(words)


def get_char_count(book_text):

    count = {}

    words = book_text.split()

    for word in words:
        for c in word:
            c = c.lower()
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

    return count


def sort_on(items):

    return items["num"]


def get_sorted(to_sort):

    sorted = []

    for key, value in to_sort.items():
    
        sorted.append({"char": key, "num": value})

    sorted.sort(reverse=True, key=sort_on)

    return sorted
