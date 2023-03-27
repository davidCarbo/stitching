FROM python:3.9.8

COPY . .

EXPOSE 5000
RUN apt update
RUN apt install libgl1-mesa-glx -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]