FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat-openbsd && \
    ln -s /usr/games/fortune /usr/bin/fortune && \
    ln -s /usr/games/cowsay /usr/bin/cowsay && \
    apt-get clean

WORKDIR /app

COPY wisecow.sh /app/wisecow.sh

RUN chmod +x /app/wisecow.sh

EXPOSE 4499

CMD ["./wisecow.sh"]