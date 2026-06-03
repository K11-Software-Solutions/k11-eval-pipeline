def test_parquet(tmp_path):
    write_parquet(df, tmp_path/'out.parquet')
    assert (tmp_path/'out.parquet').exists()
