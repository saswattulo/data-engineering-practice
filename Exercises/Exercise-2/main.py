import requests
import pandas as pd
import re
from bs4 import BeautifulSoup


def main():
    # your code here
    url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
    target_timestamp = "2024-01-19 10:27"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.content
            print("Page scrapped successfully.")
    except Exception as e:
        print("Failed to scrape the webpage.")
        print(f"Error: {e}")
    
    # parse the html content
    soup = BeautifulSoup(html_content, 'html.parser')
    # fetch all the rows of the html
    rows = soup.find_all('tr')

    file_name = ''
    # iterate over all the rows of the html page
    for row in rows:
        columns = row.find_all('td')
        if len(columns) > 2:
            # extract timestamp from the column
            timestamp = columns[1].text.strip()
            if timestamp == target_timestamp:
                file_name = columns[0].text.strip()
                print("File found !!!")
                break
    
    # download the file from the new url
    file_url = f"{url}{file_name}"

    try:
        response = requests.get(file_url)
        if response.status_code == 200:
            print("File fetched successfully.")
            with open(f"{file_name}",'wb') as f:
                f.write(response.content)
            print("File saved successfully.")
    except Exception as e:
        print("Failed to download the file.")
        print(f"Error: {e}")
    
    df = pd.read_csv(f"{file_name}")
    print(df[df['HourlyDryBulbTemperature'] == max(df['HourlyDryBulbTemperature'])].to_dict())




if __name__ == "__main__":
    main()
