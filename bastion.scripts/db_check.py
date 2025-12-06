#!/usr/bin/env python3
import mysql.connector

RDS_HOST = "bookverse-db.cala26qu66fk.us-east-1.rds.amazonaws.com"
RDS_USER = "admin"
RDS_PASSWORD = "Admin12345"
RDS_DB = "bookverse"


def main():
    print("Connecting to RDS...")

    conn = None
    try:
        conn = mysql.connector.connect(
            host=RDS_HOST,
            user=RDS_USER,
            password=RDS_PASSWORD,
            database=RDS_DB,
        )

        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, genre, title, author
            FROM books
            ORDER BY id
            LIMIT 10;
            """
        )

        rows = cursor.fetchall()
        if not rows:
            print("No rows found in books table.")
            return

        print("✅ Connected. Sample rows:")
        for row in rows:
            book_id, genre, title, author = row
            print(f"- [{genre}] {title} by {author} (id={book_id})")

    except Exception as e:
        print("❌ Error while connecting or querying:", e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    main()
