def separate_to_20_chars_per_line(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read().strip()  

    words = []
    start = 0
    end = 5

    while start < len(content):
        word = content[start:end]

        if end < len(content):
            word += '-'

        words.append(word)
        start = end
        end += 5  

    with open(output_file, 'w') as f:
        for i in range(0, len(words), 4):
            line = ''.join(words[i:i+4])  
            f.write(line + '\n')  

input_file = r'C:\Users\LK\Documents\Ian\scripts\lincese type scripts\output.txt'   
output_file = '22news.txt' 

separate_to_20_chars_per_line(input_file, output_file)
