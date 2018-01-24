FROM python:3
ADD prime.py /
ADD http_server.py /
RUN pip install requests
RUN pip3 install requests
#RUN touch index.html
#CMD [ "python3", "./http_server.py" ]
