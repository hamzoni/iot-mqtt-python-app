FROM python:3.7

COPY requirement.txt .
RUN pip install -r requirement.txt

EXPOSE 9992

WORKDIR app

COPY ./main.py main.py

CMD ["uvicorn", "main:app", "--phost", "0.0.0.0", "--port", "9992"]