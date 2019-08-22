FROM python:latest
COPY . /
RUN pip3 install requests flask
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
