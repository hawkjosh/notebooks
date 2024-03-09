import sqlite3
from datetime import datetime





def main():
  connection = sqlite3.connect("sample.db")
  cursor = connection.cursor()

  cursor.execute(
      """CREATE TABLE IF NOT EXISTS sample (timestamp DATETIME, calls INTEGER, tokens INTEGER, spent REAL)"""
  )

  timestamp = datetime.now()
  calls = 1
  tokens = 1000
  spent = 2.17

  cursor.execute("""INSERT INTO sample (timestamp, calls, tokens, spent) VALUES (?, ?, ?, ?)""", (timestamp, calls, tokens, spent))

  connection.commit()
  connection.close()


if __name__ == "__main__":
    main()
    print("Database successfully updated!")