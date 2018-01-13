import pandas as pd
from sqlalchemy import create_egine

def load_locations(df, engine):
	locations = df[["continent",
			"country"]].drop_duplicates(
			).reset_index()
	locations.to_sql("Locations", engine, index=False)

def reshape_data(df):
	data = pd.melt(df, id_vars= ["continent", "country"],
	var_name="quantity_year",
	value_name="value")
	quantity_year = data["quantity"].str.split('_')
	data["quantity"] = quantity_year.str.get(1)
	data["year"] = data["year"].astype(int)
	return data

def load_facts(cleaned_data,locations):
	merged_data = cleaned_data.merge(locations).rename(columns={"index": "locations"})
	facts = ["value", "year", "locations"]
	for quantity, df in merged_data.groupby("quantity"):
	df[facts].to_sql(quantity, engine, index=False, if_exists="replace")

def gapminder_all_etl(connection_string, filepath):
	engine = create_engine(connections_string)
	data = pd.read_csv(filepath)
	locations = load_locations(data, engine)
	reshape_data(data)
	load_facts(cleaned_data, locations, engine)