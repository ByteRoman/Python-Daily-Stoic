async function fetchQuote() {
    try {
        const response = await fetch('stoic_quotes_output.csv');
        const data = await response.text();

        const today = new Date();
        const day = today.getDate();
        const month = today.toLocaleString('default', { month: 'long' });

        // Correct suffix for the day
        const suffix = (day >= 11 && day <= 13) ? 'th' : 
                       (day % 10 === 1) ? 'st' :
                       (day % 10 === 2) ? 'nd' :
                       (day % 10 === 3) ? 'rd' : 'th';

        const todayStr = `${month} ${day}${suffix}`;

        const rows = data.split('\n');
        let found = false;

        for (const row of rows) {
            const [date, title, quote, comment] = row.split('|');
            if (date.trim() === todayStr) {
                document.getElementById('title').textContent = title.trim();
                document.getElementById('quote').textContent = quote.trim();
                document.getElementById('comment').textContent = comment.trim();
                found = true;
                break;
            }
        }

        if (!found) {
            document.getElementById('title').textContent = "No Entry Found";
            document.getElementById('quote').textContent = "Wisdom comes when we least expect it.";
            document.getElementById('comment').textContent = "";
        }

    } catch (error) {
        console.error('Error loading quote:', error);
        document.getElementById('title').textContent = "Error";
        document.getElementById('quote').textContent = "Unable to load today's quote.";
        document.getElementById('comment').textContent = "";
    }
}

fetchQuote();
