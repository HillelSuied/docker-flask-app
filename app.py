from flask import Flask

app = Flask(__name__)

count = 0  # משתנה גלובלי לספירת ביקורים

@app.route('/')
def home():
    return "Hello, Flask is running!"

@app.route('/showcount')  # צריך להיות כתוב בדיוק ככה!
def show_count():
    global count
    count += 1
    return f"Visitor count: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)