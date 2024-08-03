import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='career_matching'
)
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS graduates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    skills TEXT,
    university_id INT,
    FOREIGN KEY (university_id) REFERENCES universities(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS universities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    location TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS companies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    industry TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS job_opportunities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT,
    title TEXT,
    required_skills TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
)
''')

conn.commit()
