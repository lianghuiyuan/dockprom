FROM python:3.7-slim-stretch
#COPY ./server.py /homework/
RUN pip install requests

EXPOSE 8081

WORKDIR /homework/
#CMD ["python", "/homework/server.py", "--host", "0.0.0.0"]
#CMD "python /homework/server.py --host 0.0.0.0 > /homework/server.log 2>&1"
CMD ["python",  "-u", "/homework/server.py", "--host", "0.0.0.0", "1>/homework/server.log", "2>/homework/server.log"]
