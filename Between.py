def find_text_between_words(input_string, word1, word2):
    start_indices = [i + len(word1) for i in range(len(input_string)) if input_string.startswith(word1, i)]
    end_indices = [i for i in range(len(input_string)) if input_string.startswith(word2, i)]

    last_end_index = -1

    for start_index in start_indices:
        found = False
        for end_index in end_indices:
            if end_index > last_end_index and start_index < end_index:
                text_between = input_string[start_index:end_index]
                print(f"Text between '{word1}' and '{word2}': {text_between}")
                found = True
                last_end_index = end_index
                break
        if found:
            continue

# Example usage
input_string = "apple banana orange apple mango apple banana apple mango orange banana apple"

word1 = "apple"
word2 = "banana"

find_text_between_words(input_string, word1, word2)
