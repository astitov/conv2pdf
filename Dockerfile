FROM ubuntu:focal
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update -q && \
    apt install -y lighttpd lighttpd-doc libcgi-pm-perl wget perl && \
    wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb && \
    apt install -y ./wkhtmltox_0.12.6-1.focal_amd64.deb && \
    rm -rf ./wkhtmltox_0.12.6-1.focal_amd64.deb && \
    rm -rf /var/lib/apt/lists/* && \
    lighttpd-enable-mod cgi && \
    service lighttpd stop

COPY  files/wk_convert.cgi  /usr/lib/cgi-bin/wk_convert.cgi

EXPOSE 80

CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]

