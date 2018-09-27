
FROM alpine

RUN apk update && \
    apk add --no-cache --upgrade \
      python \
      py-pip \
      gcc \
      libc-dev 
RUN pip install --upgrade pip \
      gkeepapi \
      evernote

COPY . /usr/local/gkeep-evernote-sync

#CMD ["crond", "-l", "2", "-f"]
#CMD ["cd", "/usr/local/gkeep-evernote-sync"]
