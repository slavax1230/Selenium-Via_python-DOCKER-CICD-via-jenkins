FROM --platform=linux/amd64 python:3.9-buster

# install google chrome

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

RUN apt-get -y update

RUN apt-get install -y google-chrome-stable


# set display port to avoid crash

ENV DISPLAY=:99

# install selenium

RUN pip install selenium==4.3.0

COPY . .

COPY chromedriver /usr/local/bin/

CMD python main.py