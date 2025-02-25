# Docker Flask App

זהו פרויקט Flask שמופעל בתוך Docker, עם MySQL ו-Nginx כ-Load Balancer.

## 📌 איך להריץ את הפרויקט?

### 1️⃣ התקנת Docker ו-Docker Compose
וודא שהתקנת את Docker ו-Docker Compose:
- **Linux/macOS:** [הורדה](https://docs.docker.com/get-docker/)
- **Windows:** התקן את Docker Desktop ([קישור](https://www.docker.com/products/docker-desktop))

### 2️⃣ שכפול הריפוזיטורי
```sh
git clone https://github.com/HillelSuied/docker-flask-app.git
cd docker-flask-app
```

### 3️⃣ הפעלת הפרויקט עם Docker Compose
```sh
docker-compose up -d
```
📌 **השרת ירוץ על `http://localhost/`**

### 4️⃣ בדיקות
- גש לכתובת `http://localhost/` ובדוק את השרת.
- רענן את הדף ובדוק את העוגייה (`server_ip`).
- בדוק את מספר הביקורים ב- `http://localhost/showcount`.

## 📌 Scaling - שינוי מספר הרפליקות
ניתן להגדיל או להקטין את מספר מופעי האפליקציה עם:
```sh
./scale.sh 5  # משנה ל-5 מופעים
```

## 📌 עצירת הפרויקט
```sh
docker-compose down
```

## 📌 מידע נוסף
- Flask שומר את הנתונים במסד MySQL
- Nginx משמש כ-Load Balancer עם Sticky Sessions מבוסס עוגיות
- השימוש ב-Docker Compose מאפשר ניהול קל של הסביבה

💡 אם יש בעיה, ניתן לבדוק לוגים עם:
```sh
docker logs docker-flask-app-nginx-1
docker logs docker-flask-app-flask-app-1
```

