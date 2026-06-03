# BUG: chunk size hardcoded to 1000, not configurable
# causes OOM on machines with low RAM and large rows
CHUNK_SIZE = 1000
def read_chunked(path):
    return pd.read_csv(path, chunksize=CHUNK_SIZE)
