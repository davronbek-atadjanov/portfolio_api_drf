# Asosiy Python imajasi
FROM python:3.9

# Pythonni ba'zi optimallashtirishlar bilan sozlash
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Ishlash papkasi
WORKDIR /code

# requirements.txt-ni konteynerga nusxalash va kutubxonalarni o'rnatish
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Loyiha fayllarini konteynerga nusxalash
COPY . /code/

# Statik fayllarni to'plang (agar kerak bo'lsa)
RUN python manage.py collectstatic --noinput --clear

# Django uchun portni ochish
EXPOSE 8000

# Gunicorn orqali Django ilovasini ishga tushirish
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
