FROM python:latest
COPY . /
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
