import csv
import datetime

def get_today_quote_only(quotes_file='stoic_quotes_stripped.csv'):
    try:
        # Get today's date in "Month DaySuffix" format (e.g., April 6th)
        today = datetime.datetime.now()
        day = today.day
        suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
        today_str = today.strftime(f"%B {day}{suffix}")

        # Load CSV and find today's quote
        with open(quotes_file, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='|')
            for row in reader:
                if row[0] == today_str:
                    return format_quote_only(row)

        return f"{today_str}\n\n\nNo stoic quote found for today."

    except Exception:
        return (
            "Today\n\n\n"
            "BRIGHT SIDE\n\n\n"
            "“Always Look on the Bright Side of Life.” —ERIC IDLE"
        )

def format_quote_only(entry_row):
    date, title, quote = entry_row  # Assuming the CSV has 3 columns: date, title, and quote
    formatted = f"{date}\n\n\n{title}\n\n\n{quote}"
    return formatted.replace("   ", "\n\n")

if __name__ == '__main__':
    print('\nToday\'s Stoic Quote (No Comment):\n')
    print(get_today_quote_only())
