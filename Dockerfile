FROM centos:8
USER root
RUN yum -y install bzip2 openscap-scanner python3
USER nobody

WORKDIR /openscap
COPY app.py .
CMD ["python3", "app.py"]
