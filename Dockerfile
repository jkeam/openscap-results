FROM registry.access.redhat.com/ubi7/python-38
USER root
RUN yum -y install bzip2 openscap-scanner
USER nobody

WORKDIR /openscap
COPY app.py .
RUN python3 app.py

WORKDIR /openscap/reportsdir
CMD ["python3", "-m", "http.server"]
