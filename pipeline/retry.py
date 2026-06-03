import time
def with_retry(fn, retries=3):
    for i in range(retries):
        try: return fn()
        except Exception:
            if i==retries-1: raise
            time.sleep(2**i)
