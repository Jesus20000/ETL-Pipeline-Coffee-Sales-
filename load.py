from sqlalchemy import create_engine

def load_to_postgres(df, table_name, user, password, db, host='localhost', port='5432'):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    df.to_sql(table_name, engine, if_exists='replace', index=False)