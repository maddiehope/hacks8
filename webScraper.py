import requests
import base64
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.fastfoodmenuprices.com/zaxbys-prices/"
soup = BeautifulSoup(requests.get(url).content, "html.parser")

data = []
for td in soup.select(
    "tr:has(.column-1):has(.column-2):has(.column-3):has(input)"
):
    data.append(
        {
            "Type": td.find_previous(colspan="3").get_text(strip=True),
            "Food": td.select_one(".column-1").get_text(strip=True),
            "Size": td.select_one(".column-2").get_text(strip=True),
            "Price": float(
                td.select_one(".column-3").get_text(strip=True).strip("$")
            ),
        }
    )


adjust = soup.select_one('.tp-variation option:-soup-contains("Georgia")')
adjust = float(base64.b64decode(adjust["value"]))

df = pd.DataFrame(data)
df["Price"] = (df["Price"] * adjust).round(2)

print(df)
df.to_csv("zaxbys.csv", index=False)