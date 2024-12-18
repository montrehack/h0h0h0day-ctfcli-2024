# Base image with minimal tools
FROM debian:bullseye-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary tools
RUN apt-get update && apt-get install -y \
    bash \
    coreutils \
    nano \
    net-tools \
    openssh-server \
    bash \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

    
# Configuring SSH
# && echo "AllowUsers bauble" >> /etc/ssh/sshd_config \
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config \
&& ssh-keygen -A \
&& mkdir -p /var/run/sshd 
EXPOSE 22

# This is the default shell
COPY sUPPER.sh /usr/local/bin/sUPPERsh
RUN chmod +x /usr/local/bin/sUPPERsh

# This is kind of a helpful file to get out,
# but executing it will no change anything
COPY decoy.sh /bin/another_sh
RUN chmod +x /bin/another_sh

# Copy flag file to home of user
COPY flag.txt /home/bauble/flag.txt 

# Create a Symlink bash -> /usr/local/bin/bash
# And another for cat because you'd have to /bin/cat 
# once you broke the jail
RUN ln -s /bin/bash /usr/local/bin/bash \
 && ln -s /bin/cat /usr/local/bin/cat

# Create a restricted user
RUN useradd -m -s /usr/local/bin/sUPPERsh bauble && echo "bauble:BAUBLE" | chpasswd
RUN mkdir -p /home/Bauble && chown bauble:bauble /home/Bauble

# Set the default command to a restricted shell
CMD ["/usr/sbin/sshd", "-D"]
