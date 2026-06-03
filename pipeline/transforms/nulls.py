def handle_nulls(df, strategy='drop'): return df.dropna() if strategy=='drop' else df.fillna(0)
