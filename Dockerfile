FROM ubuntu:20.04
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get -y update && apt-get install -y python3 \ 
        python3-pip git p7zip-full p7zip-rar xz-utils locales unzip
# RUN apt-get -y upgrade
RUN apt-get -y autoremove && apt-get -y autoclean
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY nextract /usr/local/bin
COPY pextract /usr/local/bin
RUN chmod +x /usr/local/bin/nextract && chmod +x /usr/local/bin/pextract
COPY . .

CMD python3 -m unarchiver
