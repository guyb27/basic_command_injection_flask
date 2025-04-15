FROM ubuntu:jammy

RUN apt-get update && apt-get install -y openssh-server sudo

RUN mkdir -p /run/sshd

# Set up a new user (with password authentication) for SSH access
RUN useradd -ms /bin/bash ubuntu && echo "ubuntu:password" | chpasswd

# Enable password authentication in SSH config
RUN sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/^PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expose SSH port
EXPOSE 22

# Start the SSH service when the container runs
CMD ["/usr/sbin/sshd", "-D"]