import sqlite3 as sql
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():

    con = sql.connect("dbase.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute(" select * from post")

    posts = cur.fetchall()

    return render_template('main.html', posts = posts)

@app.route('/add_post',methods = ['POST','GET'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        usr = request.form['username']
        psw = request.form['password']
        with sql.connect("dbase.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute("select * from user")
            answ = cur.fetchall()
            print(answ)
            cur.execute("select * from user where name like '%s' and  password like '%s'" % (usr,psw))
            answ = cur.fetchall()
            print(answ)
            if answ:
                cur.execute("INSERT INTO post (title,content) VALUES(?,?)",(title,content))
                con.commit()
            #con.close()
                return redirect("/")
            else:
                error = True
                return render_template('add_post.html',error = error);
    return render_template('add_post.html')


if __name__ == '__main__':
    app.run(debug = True)