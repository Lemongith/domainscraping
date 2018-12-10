FROM python:3
RUN pip install pystrich && pip install requests && pip install bs4
CMD [ "python", "./code.py" ]
