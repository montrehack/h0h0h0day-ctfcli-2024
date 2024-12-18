FROM debian:bookworm-slim

RUN apt update && apt install -y vsftpd
RUN apt clean

RUN mkdir /usr/share/empty

RUN useradd -m -d /triage triage && echo "triage:triageisfun789!" | chpasswd

COPY vsftpd.conf /etc/
COPY flag triage.sh /

CMD ["/usr/sbin/vsftpd", "/etc/vsftpd.conf"]