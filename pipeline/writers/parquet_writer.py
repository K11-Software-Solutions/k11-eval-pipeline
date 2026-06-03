def write_parquet(df, path): df.to_parquet(path, index=False)
