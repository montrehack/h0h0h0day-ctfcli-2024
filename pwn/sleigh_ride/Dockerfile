FROM debian:bookworm

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y --no-install-recommends install xinetd strace python3

RUN mkdir /app

# i=1001
# n="sleigh_ride"

RUN useradd -s /bin/sh -u "1001" "sleigh_ride"
RUN useradd -s /bin/sh -u "1002" "sleigh_ride_shell"

RUN chown root:root /app
RUN chmod 0755 /app

COPY . /root/
RUN cp /root/xinetd.conf /etc/xinetd.d/sleigh_ride
RUN install -o root -g root -m 0755 /root/runquete /usr/local/bin/runquete
RUN install -o root -g root -m 0755 /root/snow /usr/local/bin/snow
RUN install -o root -g root -m 0755 /root/sleigh_ride /app/sleigh_ride
RUN install -o root -g sleigh_ride_shell -m 2755 /root/cat_flag /app/cat_flag
RUN install -o root -g sleigh_ride_shell -m 0640 /root/flag.txt /flag.txt

RUN rm -rf /usr/share/man/*
RUN rm -rf /usr/share/doc/*
RUN apt-get -y autoremove
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

CMD ["/root/start.sh"]
