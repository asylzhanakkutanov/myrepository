import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",   # база аты
        user="postgres",       # username
        password="qwerty",       # пароль (өз пароліңді жаз)
        port="5432"
    )

    print("✅ Connected to PostgreSQL!")

    conn.close()

except Exception as e:
    print("❌ Error:", e)