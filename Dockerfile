FROM python:3.10.0-alpine3.15
WORKDIR /application
COPY needed_modules.txt needed_modules.txt
RUN pip install -r needed_modules.txt
COPY . /application
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]