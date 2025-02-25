#!/bin/bash

# בודק אם המשתמש סיפק פרמטר
if [ -z "$1" ]; then
    echo "❌ יש לספק מספר מופעים להרצה. דוגמה: ./scale.sh 5"
    exit 1
fi

# קביעת מספר הרפליקות של האפליקציה
SCALE=$1
echo "🔄 שינוי מספר הרפליקות ל-$SCALE..."

# שינוי מספר הרפליקות עם השם הנכון של השירות
docker-compose up -d --scale flask-app=$SCALE

# בדיקה אם ההרצה הצליחה
if [ $? -eq 0 ]; then
    echo "✅ הרפליקות של flask-app עודכנו ל-$SCALE!"
else
    echo "❌ שגיאה: לא הצלחנו לשנות את מספר הרפליקות!"
fi