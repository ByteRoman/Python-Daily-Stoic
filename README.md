# 📬 Daily Stoic Email Bot

This project automatically sends a daily Stoic quote from *The Daily Stoic* by Ryan Holiday to your email inbox using Python and GitHub Actions.

Each email contains:
- The current date in a human-readable format (e.g., *April 12th*)
- The daily meditation title
- A quote from a Stoic philosopher
- Commentary from the book

All content is sent directly from a pre-formatted `.csv` file (`stoic_quotes_output.csv`) which includes all 366 daily entries (for leap years too).

---

## ✨ Features

- Automatically runs **daily at 7:00 AM ACST** (configured via GitHub Actions cron)
- Sends email using your GMX account credentials (any email service of your choice can be used)
- Designed to be fully automated – no manual work once set up

---

## 🔧 How It Works

### GitHub Actions

A GitHub Actions workflow is configured in `.github/workflows/send_stoic_email.yml` to trigger:

- Automatically at `21:30 UTC` (7:00 AM ACST)
- Manually via the "Run workflow" button

It runs the `dd_email.py` script in the repo.

### Python Script

The core script `dd_email.py` does the following:

1. Reads today’s date and formats it (`April 12th`, etc.)
2. Looks up the corresponding entry from `stoic_quotes_output.csv`
3. Builds and sends an email using GMX SMTP
4. Includes only one recipient (yourself), configured via environment variables

---

## 🔐 Environment Variables

To keep credentials safe, the following **GitHub repository secrets** must be set:

- `EMAIL` – your GMX email address
- `EMAIL_PASSWORD` – your GMX app password

These are used by the Python script to log in and send the email.

---

## 📚 Disclaimer

The content used in this project — including daily titles, quotes, and commentary — is sourced from:

**The Daily Stoic** by Ryan Holiday and Stephen Hanselman

> This project is intended **strictly for personal and educational use only.**
> 
> All rights to the original content remain with the authors and publishers.
> 
> If the author or publisher requests removal, all content will be immediately deleted upon request.

---

## 🧪 For Learning Purposes Only

This project was created to:
- Practice GitHub Actions automation
- Explore email automation with Python
- Study and reflect on Stoic philosophy daily

It is **not** intended for redistribution or commercial use.


---

## 🛠 Future Improvements

- Optional multiple recipients
- Web interface for adding/removing entries
- Alternative SMTP provider support

---

## 📬 Contact

If you have any questions or concerns about this project or its content, feel free to reach out.

Cheers, 

ByteRoman



