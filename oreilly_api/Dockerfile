FROM python:latest
WORKDIR /
ENV FLASK_APP=take_home.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY take_home.py ./
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5051
CMD ["python", "./take_home.py"]
