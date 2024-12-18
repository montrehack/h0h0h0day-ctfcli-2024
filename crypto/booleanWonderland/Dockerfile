# Use a base image with SSH installed (you can choose a different base image if needed)
FROM ubuntu:latest
# Install SSH server
RUN apt-get update && \
    apt-get install -y openssh-server python3 sudo && \
    apt-get clean

# Add a non-root user
RUN useradd -m ctfuser && echo 'ctfuser:nowel' | chpasswd && mkdir /home/ctfuser/challenge


# Copy the scripts to the appropriate directories
COPY src/booleanWonderland.py /root/booleanWonderland.py
COPY src/README /home/ctfuser/challenge/README

# Change the permissions and ownership of the scripts
RUN chown ctfuser:ctfuser /home/ctfuser/challenge/README
RUN chmod +r /home/ctfuser/challenge/README
RUN chmod 600 /root/booleanWonderland.py

# Allow ctfuser to execute the script with sudo without a password
RUN echo "ctfuser ALL=(ALL) NOPASSWD: /usr/bin/python3 /root/booleanWonderland.py" >> /etc/sudoers

# SSH port (optional, change if needed)
EXPOSE 22

# Start SSH service
RUN service ssh start
CMD ["/usr/sbin/sshd", "-D"]

