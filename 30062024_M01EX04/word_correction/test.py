import streamlit as st
import levenshtein_distance


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input("Word: ")

    if st.button("Compute"):
        leven_distances = dict()
        vocabs = levenshtein_distance.load_vocab(file_path="./vocab.txt")
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance.levenshtein_distance(
                word, vocab)

        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))

        correct_word = list(sorted_distances.keys())[0]
        st.write("correct word: ", correct_word)

        col1, col2 = st.columns(2)
        col1.write("Vocabulary: ")
        col1.write(vocabs)

        col2.write("Distances: ")
        col2.write(sorted_distances)


if __name__ == "__main__":
    main()
