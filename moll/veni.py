import psycopg2

def db_ready(host: str, port: int, dbname: str, user: str, password: str) -> bool:
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=dbname,
            user=user,
            password=password
        )
        conn.close()
        return True
    except psycopg2.Error:
        return False
