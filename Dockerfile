FROM python:latest

COPY bin/ /opt/bin/
RUN chmod +x /opt/bin/memeater.py
ENTRYPOINT ["/opt/bin/memeater.py"]
