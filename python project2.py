# Word Counter for IDLE
def word_counter():
    print("=== Word Counter ===")
    print("Enter/Paste your text (press Enter twice to finish):\n")
    
    # Collect multi-line input
    lines = []
    while True:
        line = input()
        if line == "":  # Stop when user enters empty line
            break
        lines.append(line)
    
    text = '\n'.join(lines)
    
    if not text.strip():
        print("Error: No text was entered!")
        return
    
    # Count words (basic version)
    words = text.split()
    word_count = len(words)
    
    # Advanced statistics
    unique_words = len(set(words))
    avg_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
    
    # Display results
    print("\n=== Results ===")
    print(f"Total words: {word_count}")
    print(f"Unique words: {unique_words}")
    print(f"Average word length: {avg_length:.1f} characters")
    
    # Word frequency (top 5)
    if word_count > 0:
        from collections import Counter
        word_freq = Counter(words)
        print("\nTop 5 most frequent words:")
        for word, count in word_freq.most_common(5):
            print(f"{word}: {count}")

# Run the program
if __name__ == "__main__":
    word_counter()
    input("\nPress Enter to exit...")  # Keeps window open in IDLE
