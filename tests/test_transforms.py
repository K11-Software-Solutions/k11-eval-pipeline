def test_rename(): assert 'new_col' in rename_cols(df, {'old_col': 'new_col'}).columns
