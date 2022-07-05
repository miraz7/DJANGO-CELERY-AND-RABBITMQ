FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

ENV TZ=Asia/Dhaka
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN python -m pip install --upgrade pip

WORKDIR /app
RUN mkdir src


ADD requirements.txt /app
RUN pip install -r requirements.txt

COPY src/ /app/src/

EXPOSE 8000


CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]




