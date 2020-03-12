FROM alpine:3.10

WORKDIR /resources
COPY resources resources
COPY apps apps
CMD ["/bin/false"]

