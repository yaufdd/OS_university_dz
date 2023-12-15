from flask import Flask, request, jsonify
import time
import hashlib


app = Flask(__name__)
db = {
    "admin": {
        "password": hashlib.sha256("password".encode('utf-8')).hexdigest(),
        "last_login": 0,
        "count": 0
    }
}


@app.route('/')
def login():
    log = request.args.get('username')
    password = request.args.get('password')
    time_now = time.time()
    if log in db:
        password_db = db[log]["password"]
        last_login = db[log]["last_login"]
        login_attempts = db[log]["count"]

        if time_now - last_login >60:
            db[log]["count"] = 0
        if login_attempts >= 3:
            return jsonify({"message": f"Превышено количество попыток, повторите через {int(60-(time_now-last_login))} секунд."}), 666
        if hashlib.sha256(password.encode('utf-8')).hexdigest() == password_db:
            db[log]["count"] = 0
            db[log]["last_login"] = time_now
            return jsonify({"message": "Вы вошли"}), 1000
        else:
            db[log]["last_login"] = time_now
            db[log]["count"] += 1
            return jsonify({"message": "Проверьте логин и пароль"}), 666
    else:
        return jsonify({"message": "Проверьте логин и пароль"}), 666

if __name__ == '__main__':
    app.run()