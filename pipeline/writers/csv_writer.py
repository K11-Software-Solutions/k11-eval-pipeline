def write_csv(df, path, compress=True): df.to_csv(path, compression='gzip' if compress else None, index=False)
