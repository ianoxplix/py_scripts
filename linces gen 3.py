def separate_to_20_chars_per_line(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read().strip()  # Read content and strip any surrounding whitespace

    words = []
    start = 0
    end = 5

    while start < len(content):
        # Get the next 5 characters
        word = content[start:end]

        # Add a hyphen after every 5 characters except the last one
        if end < len(content):
            word += '-'

        words.append(word)
        start = end
        end += 5  # Move to the next 5 characters

    with open(output_file, 'w') as f:
        for i in range(0, len(words), 4):
            line = ''.join(words[i:i+4])  # Join every 4 words with a hyphen
            f.write(line + '\n')  # Write each line to the output file

# Example usage:
input_file = r'C:\Users\LK\Documents\Ian\scripts\lincese type scripts\output.txt'   # Replace with your input file name
output_file = '22news.txt' # Replace with the desired output file name

separate_to_20_chars_per_line(input_file, output_file)
