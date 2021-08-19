FROM python:3.6
WORKDIR /app
COPY requirements.txt ./
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./ /app
CMD [ "python", "main.py" ]

