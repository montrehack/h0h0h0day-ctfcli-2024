FROM ubuntu@sha256:0e5e4a57c2499249aafc3b40fcd541e9a456aab7296681a3994d631587203f97 AS base

# Install requirements
RUN dpkg --add-architecture i386
RUN apt-get update -y && apt-get install -y libc6:i386 libssl3:i386

WORKDIR /app
ADD --chmod=755 gift_wrapper run

ARG FLAG
RUN echo "${FLAG}" > flag.txt
RUN chmod 644 flag.txt
RUN mv flag.txt flag-$(md5sum flag.txt | awk '{print $1}').txt

FROM pwn.red/jail
COPY --from=base / /srv
