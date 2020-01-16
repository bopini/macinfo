FROM python:3.7-alpine

RUN apk update --allow-untrusted \
 && apk --update add curl ca-certificates tar bash bind-tools expat db libsasl subversion-libs apr-util apr libc6-compat libstdc++ fts

RUN apk add --no-cache --update python py-pip

RUN mkdir macinfo
ADD find_mac_info.py /macinfo
WORKDIR /macinfo

#CMD ["/launch.sh"]