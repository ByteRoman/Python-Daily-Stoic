import csv
import re

def parse_entries(text):
    entries = []
    # Split entries starting at month name + day (e.g., "January 1st")
    raw_entries = re.split(r'(?=\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)\b)', text)

    for entry in raw_entries:
        lines = [line.strip() for line in entry.strip().split('\n') if line.strip()]
        if len(lines) < 3:
            continue  # Skip invalid entries

        date = lines[0]
        title = lines[1]

        # Detect quote lines (until line with author)
        quote_lines = []
        author_line_index = -1
        for i, line in enumerate(lines[2:], start=2):
            quote_lines.append(line)
            if re.search(r'—\s*[A-Z ]+,', line) or re.search(r'”\s*—', line):
                author_line_index = i
                break

        quote = ' '.join(quote_lines).strip()
        quote = re.sub(r'\s+', ' ', quote)

        # Remaining lines are the author's commentary
        comment_lines = lines[author_line_index + 1:]
        comment = '   '.join(comment_lines).strip()

        entries.append([date, title, quote, comment])

    return entries

def write_to_csv(entries, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
        for entry in entries:
            writer.writerow(entry)

# --- Main Execution ---

with open('book.txt', 'r', encoding='utf-8') as f:
    content = f.read()

entries = parse_entries(content)
write_to_csv(entries, 'stoic_quotes_output.csv')

print(f"✅ Done! Parsed {len(entries)} entries into stoic_quotes_output.csv")
