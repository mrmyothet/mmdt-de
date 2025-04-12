import pandas as pd

covid_19_df = pd.read_csv("covid_19_processed.csv")
weather_df = pd.read_csv("weather_data.csv")

covid_19_df["capital"] = covid_19_df["capital"].str.lower()
weather_df["name"] = weather_df["name"].str.lower()

combined_df = covid_19_df.merge(weather_df, left_on="capital", right_on="name")

print("shape of combined data ", combined_df.shape)

combined_df.to_csv("combined_data.csv", index=False)
