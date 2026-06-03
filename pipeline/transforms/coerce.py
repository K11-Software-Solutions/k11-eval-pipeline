def coerce(df, types):
    for col, t in types.items(): df[col] = df[col].astype(t)
    return df
