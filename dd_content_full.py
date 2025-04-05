import csv
import datetime

def get_today_entry(quotes_file='stoic_quotes_output.csv'):
    try:
        # Generate today's date in "Month DaySuffix" format (e.g., April 6th)
        today = datetime.datetime.now()
        day = today.day
        suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
        today_str = today.strftime(f"%B {day}{suffix}")

        # Load all entries
        with open(quotes_file, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='|')
            for row in reader:
                if row[0] == today_str:
                    return format_entry(row)

        # If no matching date is found
        return f"{today_str}\n\n\nNo stoic entry found for today."
    
    except Exception as e:
        # Fallback default entry
        return (
            "Today\n\n\n"
            "BRIGHT SIDE\n\n\n"
            "“Always Look on the Bright Side of Life.” —ERIC IDLE\n\n\n"
            "Sometimes life throws errors instead of wisdom. Today is one of those days."
        )

def format_entry(entry_row):
    date, title, quote, comment = entry_row
    # Replace | with triple newlines (already split)
    # Replace triple space with double newline
    formatted = f"{date}\n\n\n{title}\n\n\n{quote}\n\n\n{comment}"
    formatted = formatted.replace("   ", "\n\n")
    return formatted

if __name__ == '__main__':
    print('\nToday\'s Stoic Quote:\n')
    print(get_today_entry())
