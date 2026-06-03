# BUG: no transaction — partial writes on failure
def write_to_db(df, conn):
    for _, row in df.iterrows():
        conn.execute('INSERT INTO records VALUES (?)', row.tolist())
