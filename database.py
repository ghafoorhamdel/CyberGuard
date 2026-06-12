import sqlite3

conn = sqlite3.connect("cyberguard.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alert_type TEXT,
    severity TEXT
)
""")

cursor.execute("""
INSERT INTO alerts (alert_type, severity)
VALUES
('Brute Force Login', 'High'),
('Malware Detection', 'Medium'),
('Unauthorized Access', 'Critical')
""")

conn.commit()
conn.close()

print("Database created successfully!")
