# משתמשים בתמונה רשמית של Python 3.9
FROM python:3.9

# מגדירים את ספריית העבודה בתוך הקונטיינר
WORKDIR /app

# מעתיקים את קובץ התלויות (requirements.txt) לקונטיינר
COPY requirements.txt .

# מתקינים את החבילות הנדרשות
RUN pip install -r requirements.txt

# מעתיקים את שאר קבצי האפליקציה לקונטיינר
COPY . .

# מגדירים את הפקודה שתורץ כאשר הקונטיינר יפעל
CMD ["python", "app.py"]