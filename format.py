import re
import textwrap

def clean_timestamp(timestamp):
    timestamp = re.sub(r'\s+', '', timestamp)
    return timestamp

def parse_timestamp_line(timestamp_line):
    # Regex pattern matching the timestamp format "00:00:00,000 --> 00:00:00,000" with possible errors
    match = re.match(r'(\d{2}:\d{2}:\d{2},\d{3})\s*[-–—]+\s*>(?:\s*[-–—]+\s*)?(\d{2}:\d{2}:\d{2},\d{3})', timestamp_line)
    if match:
        start_time, end_time = match.groups()
        return clean_timestamp(start_time), clean_timestamp(end_time)
    return None, None

def wrap_text(text, width=75):
    return textwrap.wrap(text, width=width)

def generate_srt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]

    srt_content = ""
    counter = 1
    i = 0
    while i < len(lines):
        # Checking for batch number (assuming it's a number)
        if not re.match(r'\d+', lines[i]):
            i += 1
            continue

        # Checking for timestamp with possible errors
        lines[i] = lines[i].replace(" ", "")
        if i >= len(lines) or not re.match(r'\d{2}:\d{2}:\d{2},\d{3}', lines[i]):
            i += 1
            continue

        start_time, end_time = parse_timestamp_line(lines[i])
        i += 1

        caption = ""
        while i < len(lines) and not re.match(r'\d+', lines[i]) and not re.match(r'\d{2}:\d{2}:\d{2},\d{3}', lines[i]):
            caption += lines[i] + " "
            i += 1

        if start_time and end_time:
            wrapped_caption = wrap_text(caption)
            srt_content += f"{counter}\n{start_time} --> {end_time}\n" + "\n".join(wrapped_caption) + "\n\n"
            counter += 1

    with open('Fireside Chat with our Chief Security Officer_FR formatted.srt', 'w', encoding='utf-8') as file:
        file.write(srt_content)

# Example usage
generate_srt('Fireside Chat with our Chief Security Officer_FR txt.txt')