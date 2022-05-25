from flask import Flask, render_template
import psycopg2
from config import config
from datetime import datetime
import random

### Make the flask app
app = Flask(__name__)

### Commands
params = config()

conn = psycopg2.connect(**params)

cur = conn.cursor()  # make a cursor (allows us to execute queries)

file = open("schema.sql", "r")  # open the file
alltext = file.read()  # read all the text
cur.execute(alltext)  # execute all the SQL in the file
cur.execute('SELECT content FROM entries WHERE id = 1')
conn.commit()  # Actually make the changes to the db
creator = cur.fetchone()

cur.close()
conn.close()  # close everything

time_now = datetime.time(datetime.now())


### Routes
@app.route("/")
def homepage():
    full_name = ['Andriienko', 'Illia', 'KID-21']
    x = random.choice(full_name)
    hero = ''.join(creator)
    n = random.randint(1, 10)
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute('select id, date, title, content from entries order by date')
    royalist = cursor.fetchall()
    return render_template('index.html', entries=royalist, creator=hero, number=n, FIO=x)

### Start flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)