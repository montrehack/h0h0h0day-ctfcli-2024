FROM debian:bookworm-slim

RUN apt-get update && apt-get -y --no-install-recommends install gcc libc6-dev python3 xinetd && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN useradd -s/bin/sh -m ctf
WORKDIR /home/ctf

COPY --chown=root:root --chmod=0644 src/* /home/ctf/
COPY --chown=root:root --chmod=0644 ctf.xinetd /etc/xinetd.d/ctf

ENTRYPOINT ["/bin/sh", "/home/ctf/entrypoint.sh"]
