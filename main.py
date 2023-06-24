import requests
from bs4 import BeautifulSoup
import pandas as pd

results = []

# Iterate through years
for year in range(2013, 2015):
    # Iterate through months
    for month in range(1, 13):
        # Iterate through days
        for day in range(1, 32):
            date = f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
            url = f"https://www.x-rates.com/historical/?from=EUR&amount=1&date={date}"
            session = requests.Session()
            res = session.get(url=url)
            soup = BeautifulSoup(res.text, "html.parser")
            try:
                # Find the rate element
                tb = soup.find("td", class_="rtRates")
                rate = tb.find("a").text
                results.append([date, rate])
            except:
                # Skip if rate element is not found
                pass

# Convert results list to a DataFrame
df = pd.DataFrame(results, columns=['Date', 'Rate'])

# Save DataFrame to an Excel file
df.to_excel('results.xlsx', index=False)

print('Results saved to results.xlsx.')






