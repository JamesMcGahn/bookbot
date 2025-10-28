def get_book_text(file_path):
    print(f"Analyzing book found at {file_path}...")
    with open(file_path, "r") as f:
        file_contents = f.read()

    return file_contents


def word_count(str):
    count = str.split()
    return len(count)


def charater_count(str):
    chart_dict = {}
    for char in str:
        if not char.isalpha():
            continue
        char = char.lower()
        if chart_dict.get(char, None):
            chart_dict[char] = chart_dict[char] + 1
        else:
            chart_dict[char] = 1
    return chart_dict


def character_count_report(count_dict):
    char_dict = [{"char": k, "num": v} for (k, v) in count_dict.items()]

    def sort_on(item):
        return item["num"]

    char_dict.sort(reverse=True, key=sort_on)
    return char_dict
