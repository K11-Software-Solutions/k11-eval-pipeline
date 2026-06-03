def validate(df, schema):
    for col, dtype in schema.items():
        assert df[col].dtype == dtype
