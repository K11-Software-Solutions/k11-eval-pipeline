# BUG: threshold comparison is inverted — alerts when data is GOOD
def check_null_rate(df, threshold=0.05):
    rate = df.isnull().mean().max()
    if rate < threshold:    # BUG: should be >
        send_alert(f'High null rate: {rate}')
