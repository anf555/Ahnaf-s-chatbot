# This code is made by Ahnaf
# DO NOT COPY/USE WITHOUT ANY PERMISSION FROM THE ORIGINAL OWNER (Ahnaf)

from flask import Flask, render_template, request, make_response, redirect, flash, send_file
import sqlite3
from chatbot import *
import random
import datetime
import random

conn = sqlite3.connect('userdata.db')
c = conn.cursor()
c.execute('create table if not exists user(id TEXT, ban_status, TEXT)')
c.close()
conn.close()
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'VGR^yuhNBgvfe$56&*9iUyTRE$5^&8'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods = ['GET'])
def login():
    if request.method == 'GET':
        cookies = request.cookies
        session_id = str(cookies.get('id'))
        conn = sqlite3.connect('userdata.db')
        c = conn.cursor()
        c.execute("SELECT * FROM user WHERE id=?", (session_id,))
        temp_id_validation = ""
        for row in c.fetchall():
            tempdata = str(row)
            for id in tempdata:
                            temp_id_validation = temp_id_validation + id
        c.close()
        conn.commit()
        conn.close()
        if temp_id_validation == "":
            resp = ""
            while True:
                rand_id = random.randint(1, 214748364)
                conn = sqlite3.connect('userdata.db')
                c = conn.cursor()
                c.execute("SELECT * FROM user WHERE id=?", (rand_id,))
                temp_id_validation = ""
                tempdata = c.fetchall()
                if tempdata.__contains__(rand_id):
                    rand_id = random.randint(1, 214748364)
                else:
                     final_id = rand_id
                     c.close()
                     conn.commit()
                     conn.close()
                     conn = sqlite3.connect('userdata.db')
                     c = conn.cursor()
                     c.execute("INSERT INTO user(id, ban_status) VALUES(?, ?)", [str(rand_id), "no01banned"])
                     c.close()
                     conn.commit()
                     conn.close()
                     resp = make_response(redirect('/chatbot'))
                     resp.set_cookie('id', str(final_id), None, datetime.date(2050, 10, 10))
                     logging.info("'" + str(final_id) + "' Signed up")
                     break
            return resp
        else:
             conn = sqlite3.connect('userdata.db')
             c = conn.cursor()
             c.execute("SELECT * FROM user WHERE id=?", (session_id,))
             for row in c.fetchall():
                tempdata = row
             c.close()
             conn.commit()
             conn.close()
             if tempdata.__contains__('yes01banned'):
                  # user banned
                  logging.info("'" + str(session_id) + "' Banned user logged in")
                  return redirect('/banned')
             else:
                logging.info("'" + str(session_id) + "' User logged in")
                return redirect('/chatbot')
    else:
        logging.info("Unknown log in")
        return "Unknown type of request"

@app.route("/chatbot", methods = ['GET', 'POST'])
def chatbot():
    if request.method == 'GET':
        cookies = request.cookies
        session_id = str(cookies.get('id'))
        conn = sqlite3.connect('userdata.db')
        c = conn.cursor()
        c.execute("SELECT * FROM user WHERE id=?", (session_id,))
        tempdata = ""
        for row in c.fetchall():
            tempdata = row
        c.close()
        conn.commit()
        conn.close()
        if tempdata.__contains__('yes01banned'):
            # user banned
            logging.info("'" + session_id + "' Banned user try accessing chatbot")
            return redirect('/banned')
        else:
            # user is verified
            if tempdata == "":
                return redirect('/login')
            else:         
                logging.info("'" + session_id + "' User logged in")
                return render_template("chatbot.html", bordercolor="white", prompt_responds ="")
    else:
        cookies = request.cookies
        prompt_from_user = request.form.get('promptt')
        session_id = str(cookies.get('id'))
        conn = sqlite3.connect('userdata.db')
        c = conn.cursor()
        c.execute("SELECT * FROM user WHERE id=?", (session_id,))
        tempdata = ""
        for row in c.fetchall():
            tempdata = row
        c.close()
        conn.commit()
        conn.close()
        if tempdata.__contains__('yes01banned'):
            # user banned
            logging.info("'" + session_id + "' Banned user try accessing chatbot")
            return redirect('/banned')
        else:
            # user is verified
            if tempdata == "":
                return redirect('/login')
            else:         
                logging.info("'" + str(session_id) + "' User logged in")
                prmpt_responds = prompt(prompt_from_user, session_id)
                if prmpt_responds == "badword-detected":
                    conn = sqlite3.connect('userdata.db')
                    c = conn.cursor()
                    c.execute("UPDATE user SET ban_status = 'yes01banned' WHERE id = ?", [session_id])
                    c.close()
                    conn.commit()
                    conn.close()
                    return redirect('/banned')
                else:
                    return render_template("chatbot.html", bordercolor="grey", prompt_responds = prmpt_responds)

@app.route("/banned")
def banned():
    cookies = request.cookies
    session_id = str(cookies.get('id'))
    conn = sqlite3.connect('userdata.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user WHERE id=?", (session_id,))
    tempdata = ""
    for row in c.fetchall():
        tempdata = row
    c.close()
    conn.commit()
    conn.close()
    if tempdata.__contains__('yes01banned'):
        # user banned
        logging.info("'" + session_id + "' Banned user accessing banned page")
        return render_template("banned.html")
    else:
        return redirect('/')

@app.route("/support")
def support():
    return render_template("support.html")
@app.route("/admin", methods=['GET', 'POST'])
def admin():
    cookies = request.cookies
    auth1 = str(cookies.get('auth1'))
    auth2 = str(cookies.get('auth2'))
    auth3 = str(cookies.get('check_auth3'))
    auth4 = str(cookies.get('auth4000'))
    auth5 = str(cookies.get('auth5'))
    auth6 = str(cookies.get('authentication6'))
    auth7 = str(cookies.get('auth7'))
    auth8 = str(cookies.get('auth8'))
    auth9 = str(cookies.get('auth9'))
    auth10 = str(cookies.get('auth10'))
    if request.method == 'GET':
        all_auth = auth1+auth2+auth3+auth4+auth5+auth6+auth7+auth8+auth9+auth10
        valid_auth = 0
        if str(all_auth) == "NoneNoneNoneNoneNoneNoneNoneNoneNoneNone":
            return render_template("dashboard_login.html")
        else:
            if auth1 == "nd756F6tgce8vrt8hev84gy^&H$67g5hj(h)":
                valid_auth = valid_auth + 1
            if auth2 == "bfy7huy%^&gT5678iFdwertyujmnbvcxs^c@":
                valid_auth = valid_auth + 1
            if auth3 == "dr5678iKNBFE$56789okMNBGFRT^&8iknGFr!":
                valid_auth = valid_auth + 1
            if auth4 == "DRTYUnfr5678ijHT%^78oknbfde5678ikmngf":
                valid_auth = valid_auth + 1
            if auth5 == "e45^&8ikde34%^&8vfrtdsaqweRSwHyuikmT&*":
                valid_auth = valid_auth + 1
            if auth6 == "6789okMNBGweRSwHyuikjhs7ikde34%BVgyuik":
                valid_auth = valid_auth + 1
            if auth7 == "vrt8hev84gy^&H$6ujkMNBGweRSwHyuiikmT&*":
                valid_auth = valid_auth + 1
            if auth8 == "RTfd53827u(hj(Unf*&6fde5678iJD&^Dkmg9i":
                valid_auth = valid_auth + 1
            if auth9 == "^78oknbfde5678ikmngfRTYUnf*&VFR%^&6g9i":
                valid_auth = valid_auth + 1
            if auth10 == "(*$SDBKYHFR%^&*IW#$%^GYUIJNBGYujhyUJ)":
                valid_auth = valid_auth + 1
            if valid_auth == 10:
                return render_template("admin.html")
            else:
                return render_template("dashboard_login.html")
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == "nothing":
            if password == "nothing":
                resp = make_response(render_template("admin.html"))
                resp.set_cookie("auth1", "nd756F6tgce8vrt8hev84gy^&H$67g5hj(h)")
                resp.set_cookie("auth2", "bfy7huy%^&gT5678iFdwertyujmnbvcxs^c@")
                resp.set_cookie("check_auth3", "dr5678iKNBFE$56789okMNBGFRT^&8iknGFr!")
                resp.set_cookie("auth4000", "DRTYUnfr5678ijHT%^78oknbfde5678ikmngf")
                resp.set_cookie("auth5", "e45^&8ikde34%^&8vfrtdsaqweRSwHyuikmT&*")
                resp.set_cookie("authentication6", "6789okMNBGweRSwHyuikjhs7ikde34%BVgyuik")
                resp.set_cookie("auth7", "vrt8hev84gy^&H$6ujkMNBGweRSwHyuiikmT&*")
                resp.set_cookie("auth8", "RTfd53827u(hj(Unf*&6fde5678iJD&^Dkmg9i")
                resp.set_cookie("auth9", "^78oknbfde5678ikmngfRTYUnf*&VFR%^&6g9i")
                resp.set_cookie("auth10", "(*$SDBKYHFR%^&*IW#$%^GYUIJNBGYujhyUJ)")
                return resp
            else:
                flash("Wrong Password")
        else:
            flash("Unathorized Username")
        return render_template("dashboard_login.html")

@app.route("/server-log")
def admin_log():
    cookies = request.cookies
    auth1 = str(cookies.get('auth1'))
    auth2 = str(cookies.get('auth2'))
    auth3 = str(cookies.get('check_auth3'))
    auth4 = str(cookies.get('auth4000'))
    auth5 = str(cookies.get('auth5'))
    auth6 = str(cookies.get('authentication6'))
    auth7 = str(cookies.get('auth7'))
    auth8 = str(cookies.get('auth8'))
    auth9 = str(cookies.get('auth9'))
    auth10 = str(cookies.get('auth10'))
    if request.method == 'GET':
        all_auth = auth1+auth2+auth3+auth4+auth5+auth6+auth7+auth8+auth9+auth10
        valid_auth = 0
        if str(all_auth) == "NoneNoneNoneNoneNoneNoneNoneNoneNoneNone":
            return redirect('/admin')
        else:
            if auth1 == "nd756F6tgce8vrt8hev84gy^&H$67g5hj(h)":
                valid_auth = valid_auth + 1
            if auth2 == "bfy7huy%^&gT5678iFdwertyujmnbvcxs^c@":
                valid_auth = valid_auth + 1
            if auth3 == "dr5678iKNBFE$56789okMNBGFRT^&8iknGFr!":
                valid_auth = valid_auth + 1
            if auth4 == "DRTYUnfr5678ijHT%^78oknbfde5678ikmngf":
                valid_auth = valid_auth + 1
            if auth5 == "e45^&8ikde34%^&8vfrtdsaqweRSwHyuikmT&*":
                valid_auth = valid_auth + 1
            if auth6 == "6789okMNBGweRSwHyuikjhs7ikde34%BVgyuik":
                valid_auth = valid_auth + 1
            if auth7 == "vrt8hev84gy^&H$6ujkMNBGweRSwHyuiikmT&*":
                valid_auth = valid_auth + 1
            if auth8 == "RTfd53827u(hj(Unf*&6fde5678iJD&^Dkmg9i":
                valid_auth = valid_auth + 1
            if auth9 == "^78oknbfde5678ikmngfRTYUnf*&VFR%^&6g9i":
                valid_auth = valid_auth + 1
            if auth10 == "(*$SDBKYHFR%^&*IW#$%^GYUIJNBGYujhyUJ)":
                valid_auth = valid_auth + 1
            if valid_auth == 10:
                logs = []
                with open('server.log', 'r') as f:
                    logs = f.read()
                    f.close()
                return render_template("admin_a_log.html", log_file=logs)
            else:
                return redirect('/admin')
    else:
        return redirect('/admin')

@app.route("/clear-log", methods=['GET', 'POST'])
def clear_log():
    cookies = request.cookies
    auth1 = str(cookies.get('auth1'))
    auth2 = str(cookies.get('auth2'))
    auth3 = str(cookies.get('check_auth3'))
    auth4 = str(cookies.get('auth4000'))
    auth5 = str(cookies.get('auth5'))
    auth6 = str(cookies.get('authentication6'))
    auth7 = str(cookies.get('auth7'))
    auth8 = str(cookies.get('auth8'))
    auth9 = str(cookies.get('auth9'))
    auth10 = str(cookies.get('auth10'))
    if request.method == 'GET':
        all_auth = auth1+auth2+auth3+auth4+auth5+auth6+auth7+auth8+auth9+auth10
        valid_auth = 0
        if str(all_auth) == "NoneNoneNoneNoneNoneNoneNoneNoneNoneNone":
            return redirect('/admin')
        else:
            if auth1 == "nd756F6tgce8vrt8hev84gy^&H$67g5hj(h)":
                valid_auth = valid_auth + 1
            if auth2 == "bfy7huy%^&gT5678iFdwertyujmnbvcxs^c@":
                valid_auth = valid_auth + 1
            if auth3 == "dr5678iKNBFE$56789okMNBGFRT^&8iknGFr!":
                valid_auth = valid_auth + 1
            if auth4 == "DRTYUnfr5678ijHT%^78oknbfde5678ikmngf":
                valid_auth = valid_auth + 1
            if auth5 == "e45^&8ikde34%^&8vfrtdsaqweRSwHyuikmT&*":
                valid_auth = valid_auth + 1
            if auth6 == "6789okMNBGweRSwHyuikjhs7ikde34%BVgyuik":
                valid_auth = valid_auth + 1
            if auth7 == "vrt8hev84gy^&H$6ujkMNBGweRSwHyuiikmT&*":
                valid_auth = valid_auth + 1
            if auth8 == "RTfd53827u(hj(Unf*&6fde5678iJD&^Dkmg9i":
                valid_auth = valid_auth + 1
            if auth9 == "^78oknbfde5678ikmngfRTYUnf*&VFR%^&6g9i":
                valid_auth = valid_auth + 1
            if auth10 == "(*$SDBKYHFR%^&*IW#$%^GYUIJNBGYujhyUJ)":
                valid_auth = valid_auth + 1
            if valid_auth == 10:
                return render_template("confirm_log_deletion.html")
            else:
                return redirect('/admin')
    else:
        valid_auth = 0
        if auth1 == "nd756F6tgce8vrt8hev84gy^&H$67g5hj(h)":
            valid_auth = valid_auth + 1
        if auth2 == "bfy7huy%^&gT5678iFdwertyujmnbvcxs^c@":
            valid_auth = valid_auth + 1
        if auth3 == "dr5678iKNBFE$56789okMNBGFRT^&8iknGFr!":
            valid_auth = valid_auth + 1
        if auth4 == "DRTYUnfr5678ijHT%^78oknbfde5678ikmngf":
            valid_auth = valid_auth + 1
        if auth5 == "e45^&8ikde34%^&8vfrtdsaqweRSwHyuikmT&*":
            valid_auth = valid_auth + 1
        if auth6 == "6789okMNBGweRSwHyuikjhs7ikde34%BVgyuik":
            valid_auth = valid_auth + 1
        if auth7 == "vrt8hev84gy^&H$6ujkMNBGweRSwHyuiikmT&*":
            valid_auth = valid_auth + 1
        if auth8 == "RTfd53827u(hj(Unf*&6fde5678iJD&^Dkmg9i":
            valid_auth = valid_auth + 1
        if auth9 == "^78oknbfde5678ikmngfRTYUnf*&VFR%^&6g9i":
            valid_auth = valid_auth + 1
        if auth10 == "(*$SDBKYHFR%^&*IW#$%^GYUIJNBGYujhyUJ)":
            valid_auth = valid_auth + 1
        if valid_auth == 10:
            with open('server.log', 'w+') as f:
                f.close()
            return redirect('/server-log')
        else:
            return redirect('/admin')

@app.route("/download-log")
def download_log():
    cookies = request.cookies
    auth1 = str(cookies.get('auth1'))
    auth2 = str(cookies.get('auth2'))
    auth3 = str(cookies.get('check_auth3'))
    auth4 = str(cookies.get('auth4000'))
    auth5 = str(cookies.get('auth5'))
    auth6 = str(cookies.get('authentication6'))
    auth7 = str(cookies.get('auth7'))
    auth8 = str(cookies.get('auth8'))
    auth9 = str(cookies.get('auth9'))
    auth10 = str(cookies.get('auth10'))
    if request.method == 'GET':
        all_auth = auth1+auth2+auth3+auth4+auth5+auth6+auth7+auth8+auth9+auth10
        valid_auth = 0
        if str(all_auth) == "NoneNoneNoneNoneNoneNoneNoneNoneNoneNone":
            return redirect('/admin')
        else:
            if auth1 == "nd756F6tgce8vrt8hev84gy^&H$67g5hj(h)":
                valid_auth = valid_auth + 1
            if auth2 == "bfy7huy%^&gT5678iFdwertyujmnbvcxs^c@":
                valid_auth = valid_auth + 1
            if auth3 == "dr5678iKNBFE$56789okMNBGFRT^&8iknGFr!":
                valid_auth = valid_auth + 1
            if auth4 == "DRTYUnfr5678ijHT%^78oknbfde5678ikmngf":
                valid_auth = valid_auth + 1
            if auth5 == "e45^&8ikde34%^&8vfrtdsaqweRSwHyuikmT&*":
                valid_auth = valid_auth + 1
            if auth6 == "6789okMNBGweRSwHyuikjhs7ikde34%BVgyuik":
                valid_auth = valid_auth + 1
            if auth7 == "vrt8hev84gy^&H$6ujkMNBGweRSwHyuiikmT&*":
                valid_auth = valid_auth + 1
            if auth8 == "RTfd53827u(hj(Unf*&6fde5678iJD&^Dkmg9i":
                valid_auth = valid_auth + 1
            if auth9 == "^78oknbfde5678ikmngfRTYUnf*&VFR%^&6g9i":
                valid_auth = valid_auth + 1
            if auth10 == "(*$SDBKYHFR%^&*IW#$%^GYUIJNBGYujhyUJ)":
                valid_auth = valid_auth + 1
            if valid_auth == 10:
                return send_file('server.log', as_attachment=True)
            else:
                return redirect('/admin')

@app.route("/train-chatbot", methods=['GET', 'POST'])
def train_chatbot():
    cookies = request.cookies
    auth1 = str(cookies.get('auth1'))
    auth2 = str(cookies.get('auth2'))
    auth3 = str(cookies.get('check_auth3'))
    auth4 = str(cookies.get('auth4000'))
    auth5 = str(cookies.get('auth5'))
    auth6 = str(cookies.get('authentication6'))
    auth7 = str(cookies.get('auth7'))
    auth8 = str(cookies.get('auth8'))
    auth9 = str(cookies.get('auth9'))
    auth10 = str(cookies.get('auth10'))
    if request.method == 'GET':
        all_auth = auth1+auth2+auth3+auth4+auth5+auth6+auth7+auth8+auth9+auth10
        valid_auth = 0
        if str(all_auth) == "NoneNoneNoneNoneNoneNoneNoneNoneNoneNone":
            return redirect('/admin')
        else:
            if auth1 == "nd756F6tgce8vrt8hev84gy^&H$67g5hj(h)":
                valid_auth = valid_auth + 1
            if auth2 == "bfy7huy%^&gT5678iFdwertyujmnbvcxs^c@":
                valid_auth = valid_auth + 1
            if auth3 == "dr5678iKNBFE$56789okMNBGFRT^&8iknGFr!":
                valid_auth = valid_auth + 1
            if auth4 == "DRTYUnfr5678ijHT%^78oknbfde5678ikmngf":
                valid_auth = valid_auth + 1
            if auth5 == "e45^&8ikde34%^&8vfrtdsaqweRSwHyuikmT&*":
                valid_auth = valid_auth + 1
            if auth6 == "6789okMNBGweRSwHyuikjhs7ikde34%BVgyuik":
                valid_auth = valid_auth + 1
            if auth7 == "vrt8hev84gy^&H$6ujkMNBGweRSwHyuiikmT&*":
                valid_auth = valid_auth + 1
            if auth8 == "RTfd53827u(hj(Unf*&6fde5678iJD&^Dkmg9i":
                valid_auth = valid_auth + 1
            if auth9 == "^78oknbfde5678ikmngfRTYUnf*&VFR%^&6g9i":
                valid_auth = valid_auth + 1
            if auth10 == "(*$SDBKYHFR%^&*IW#$%^GYUIJNBGYujhyUJ)":
                valid_auth = valid_auth + 1
            if valid_auth == 10:
                return render_template("train-chatbot.html")
            else:
                return redirect('/admin')
    else:
        valid_auth = 0
        if auth1 == "nd756F6tgce8vrt8hev84gy^&H$67g5hj(h)":
            valid_auth = valid_auth + 1
        if auth2 == "bfy7huy%^&gT5678iFdwertyujmnbvcxs^c@":
            valid_auth = valid_auth + 1
        if auth3 == "dr5678iKNBFE$56789okMNBGFRT^&8iknGFr!":
            valid_auth = valid_auth + 1
        if auth4 == "DRTYUnfr5678ijHT%^78oknbfde5678ikmngf":
            valid_auth = valid_auth + 1
        if auth5 == "e45^&8ikde34%^&8vfrtdsaqweRSwHyuikmT&*":
            valid_auth = valid_auth + 1
        if auth6 == "6789okMNBGweRSwHyuikjhs7ikde34%BVgyuik":
            valid_auth = valid_auth + 1
        if auth7 == "vrt8hev84gy^&H$6ujkMNBGweRSwHyuiikmT&*":
            valid_auth = valid_auth + 1
        if auth8 == "RTfd53827u(hj(Unf*&6fde5678iJD&^Dkmg9i":
            valid_auth = valid_auth + 1
        if auth9 == "^78oknbfde5678ikmngfRTYUnf*&VFR%^&6g9i":
            valid_auth = valid_auth + 1
        if auth10 == "(*$SDBKYHFR%^&*IW#$%^GYUIJNBGYujhyUJ)":
            valid_auth = valid_auth + 1
        if valid_auth == 10:
            questions = request.form.get('question')
            answer = request.form.get('answer')
            class_name = request.form.get('class')
            splitted_question = questions.split('\n')
            with open("wordlist00" + str(random.randint(1, 9)) + ".py", "a") as wp:
                wp.write('\n\n')
                wp.write(class_name + " = {")
                for question in splitted_question:
                    wp.write('\n')
                    wp.write('  "' + str(question.replace('\r', "")) + '": "' + str(answer) + '",')
                wp.write('\n')
                wp.write("}")
                wp.close()
            temp_data1 = ""
            with open("wordvariable.py", "r") as wl:
                temp_data1 = wl.read()
                wl.close
            temp_data1 = temp_data1.replace("]", str(", " + class_name + "]"))
            with open("wordvariable.py", "w") as wl:
                wl.write(temp_data1)
                wl.close
            return render_template("train-chatbot.html")
        else:
            return redirect('/admin')

@app.route("/badword-history")
def badword_history():
    cookies = request.cookies
    auth1 = str(cookies.get('auth1'))
    auth2 = str(cookies.get('auth2'))
    auth3 = str(cookies.get('check_auth3'))
    auth4 = str(cookies.get('auth4000'))
    auth5 = str(cookies.get('auth5'))
    auth6 = str(cookies.get('authentication6'))
    auth7 = str(cookies.get('auth7'))
    auth8 = str(cookies.get('auth8'))
    auth9 = str(cookies.get('auth9'))
    auth10 = str(cookies.get('auth10'))
    if request.method == 'GET':
        all_auth = auth1+auth2+auth3+auth4+auth5+auth6+auth7+auth8+auth9+auth10
        valid_auth = 0
        if str(all_auth) == "NoneNoneNoneNoneNoneNoneNoneNoneNoneNone":
            return redirect('/admin')
        else:
            if auth1 == "nd756F6tgce8vrt8hev84gy^&H$67g5hj(h)":
                valid_auth = valid_auth + 1
            if auth2 == "bfy7huy%^&gT5678iFdwertyujmnbvcxs^c@":
                valid_auth = valid_auth + 1
            if auth3 == "dr5678iKNBFE$56789okMNBGFRT^&8iknGFr!":
                valid_auth = valid_auth + 1
            if auth4 == "DRTYUnfr5678ijHT%^78oknbfde5678ikmngf":
                valid_auth = valid_auth + 1
            if auth5 == "e45^&8ikde34%^&8vfrtdsaqweRSwHyuikmT&*":
                valid_auth = valid_auth + 1
            if auth6 == "6789okMNBGweRSwHyuikjhs7ikde34%BVgyuik":
                valid_auth = valid_auth + 1
            if auth7 == "vrt8hev84gy^&H$6ujkMNBGweRSwHyuiikmT&*":
                valid_auth = valid_auth + 1
            if auth8 == "RTfd53827u(hj(Unf*&6fde5678iJD&^Dkmg9i":
                valid_auth = valid_auth + 1
            if auth9 == "^78oknbfde5678ikmngfRTYUnf*&VFR%^&6g9i":
                valid_auth = valid_auth + 1
            if auth10 == "(*$SDBKYHFR%^&*IW#$%^GYUIJNBGYujhyUJ)":
                valid_auth = valid_auth + 1
            if valid_auth == 10:
                logs = []
                with open('badword.txt', 'r') as f:
                    logs = f.read()
                    f.close()
                return render_template("admin_b_log.html", log_file=logs)
            else:
                return redirect('/admin')
    else:
        return redirect('/admin')

@app.route("/edit-html")
def edit_html():
    cookies = request.cookies
    auth1 = str(cookies.get('auth1'))
    auth2 = str(cookies.get('auth2'))
    auth3 = str(cookies.get('check_auth3'))
    auth4 = str(cookies.get('auth4000'))
    auth5 = str(cookies.get('auth5'))
    auth6 = str(cookies.get('authentication6'))
    auth7 = str(cookies.get('auth7'))
    auth8 = str(cookies.get('auth8'))
    auth9 = str(cookies.get('auth9'))
    auth10 = str(cookies.get('auth10'))
    if request.method == 'GET':
        all_auth = auth1+auth2+auth3+auth4+auth5+auth6+auth7+auth8+auth9+auth10
        valid_auth = 0
        if str(all_auth) == "NoneNoneNoneNoneNoneNoneNoneNoneNoneNone":
            return redirect('/admin')
        else:
            if auth1 == "nd756F6tgce8vrt8hev84gy^&H$67g5hj(h)":
                valid_auth = valid_auth + 1
            if auth2 == "bfy7huy%^&gT5678iFdwertyujmnbvcxs^c@":
                valid_auth = valid_auth + 1
            if auth3 == "dr5678iKNBFE$56789okMNBGFRT^&8iknGFr!":
                valid_auth = valid_auth + 1
            if auth4 == "DRTYUnfr5678ijHT%^78oknbfde5678ikmngf":
                valid_auth = valid_auth + 1
            if auth5 == "e45^&8ikde34%^&8vfrtdsaqweRSwHyuikmT&*":
                valid_auth = valid_auth + 1
            if auth6 == "6789okMNBGweRSwHyuikjhs7ikde34%BVgyuik":
                valid_auth = valid_auth + 1
            if auth7 == "vrt8hev84gy^&H$6ujkMNBGweRSwHyuiikmT&*":
                valid_auth = valid_auth + 1
            if auth8 == "RTfd53827u(hj(Unf*&6fde5678iJD&^Dkmg9i":
                valid_auth = valid_auth + 1
            if auth9 == "^78oknbfde5678ikmngfRTYUnf*&VFR%^&6g9i":
                valid_auth = valid_auth + 1
            if auth10 == "(*$SDBKYHFR%^&*IW#$%^GYUIJNBGYujhyUJ)":
                valid_auth = valid_auth + 1
            if valid_auth == 10:
                with open("templates/home.html", "r+") as homepage:
                    return render_template("edit_html.html", home_html_placeholder=homepage.read())
            else:
                return redirect('/admin')
    else:
        return redirect('/admin')
if __name__ == '__main__':
    app.run()
