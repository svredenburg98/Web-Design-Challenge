import pandas as pd
import os

#path = os.path.join("../Resources/cities.csv")
cities = pd.read_csv("h:/RICEBOOTCAMP/Homework/Web-Design-Challenge/Resources/cities.csv")
cities_df = pd.DataFrame(cities)
data_html = cities_df.to_html()
print(data_html)

