def test_full_pipeline(tmp_path):
    run({'source': 'tests/fixtures/sample.csv', 'sink': str(tmp_path/'out.parquet')})
    assert (tmp_path/'out.parquet').exists()
