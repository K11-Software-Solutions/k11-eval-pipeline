def dedup(df, key): return df.drop_duplicates(subset=[key])
