# BUG: assumes US date format MM/DD/YYYY, breaks on UK dates
def normalise_date(s): return pd.to_datetime(s, format='%m/%d/%Y')
