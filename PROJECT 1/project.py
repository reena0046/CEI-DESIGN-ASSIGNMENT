import pandas as pd
import requests

def veg_data_scrapper(day):
    day_str = day.strftime('%Y-%m-%d')  # Convert Timestamp to string in 'YYYY-MM-DD' format
    url = f"https://vegetablemarketprice.com/api/dataapi/market/maharashtra/daywisedata?date={day_str}"
    response = requests.get(url)
    
    if response.status_code == 200:
        info = response.json()
        date = info['date']
        data = info['data']
        rows = []
        for item in data:
            row = {
                "Date": date,
                "State Name": "Maharashtra",
                "Vegetable Name": item["vegetablename"],
                "Wholesale Price": item["price"],
                "Retail Price": item["retailprice"],
                "Shopping Mall Price": item["shopingmallprice"],
                "Units": item["units"],
                "Vegetable Image": item["table"]["table_image_url"]
            }
            rows.append(row)
        df = pd.DataFrame(rows)
        return df
    else:
        print(f"Failed to fetch data for {day_str} with status code: {response.status_code}")
        return pd.DataFrame()  # Return an empty DataFrame if the request fails
        
if __name__ == "__main__":
    START_DATE = "2024-05-01"
    END_DATE = "2024-06-30"
    days = pd.date_range(START_DATE, END_DATE)
    dfs = []
    
    for day in days:
        df = veg_data_scrapper(day)
        if not df.empty:
            dfs.append(df)
    
    if dfs:
        final_df = pd.concat(dfs, axis='rows', ignore_index=True)
        final_df.to_csv("Vegetable_data.csv", index=False)
        print("Data has been saved to 'Vegetable_data.csv'.")
    else:
        print("No data was scraped.")
