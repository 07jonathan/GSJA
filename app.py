from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Database connection settings
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'gsja'

def get_db_connection():
    return pymysql.connect(host=db_host,
                           user=db_user,
                           password=db_password,
                           db=db_name,
                           cursorclass=pymysql.cursors.DictCursor)

@app.route("/")
@app.route("/index")
def index():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        event = "SELECT id, name, tempat, time, CASE WHEN @prev_date = date THEN NULL ELSE date END AS date, @prev_date := date AS dummy FROM ( SELECT id, name, tempat, date, time FROM events WHERE YEAR(date) = YEAR(CURDATE()) AND WEEK(date) = WEEK(CURDATE()) ORDER BY date ) AS sorted_events, (SELECT @prev_date := '') AS init ORDER BY dummy; "
        cursor.execute(event)
        events = cursor.fetchall()
        berita = "SELECT id, news, CASE WHEN @prev_date = date THEN NULL ELSE date END AS date, @prev_date := date AS dummy FROM ( SELECT id, news, date FROM news WHERE YEAR(date) = YEAR(CURDATE()) AND WEEK(date) = WEEK(CURDATE()) ORDER BY date ) AS sorted_events CROSS JOIN (SELECT @prev_date := '') AS init ORDER BY dummy;  "
        cursor.execute(berita)
        news = cursor.fetchall()
        anggota = "SELECT * FROM `anggota` WHERE YEAR(date) = YEAR(CURDATE()) AND WEEK(date) = WEEK(CURDATE()) ORDER BY date; "
        cursor.execute(anggota)
        erik = cursor.fetchall()
    connection.close()
    return render_template('index.html', events=events, news=news, anggota=erik)



@app.route("/news")
def news():
    return render_template("news.html")


if __name__ == '__main__':
	app.run(debug=True)