FROM python:3.11

RUN apt-get update -y && apt-get install -y git
ADD teller /teller

WORKDIR /teller

RUN pip3 install -r requirements.txt
RUN pip3 install python-dotenv==1.0.1 PyDrive2==1.21.3
COPY upload.py .
COPY fetch.py .
COPY run.sh .

ENTRYPOINT ["/bin/bash", "run.sh"]

