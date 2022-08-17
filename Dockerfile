FROM appimagecrafters/appimage-builder:latest

ENV ARCH=x86_64

WORKDIR /build

RUN ln -snf /usr/share/zoneinfo/UTC /etc/localtime && echo UTC > /etc/timezone
RUN apt-get update && apt-get install python3-tk -y

COPY requirements.txt /build/requirements.txt
RUN pip3 install -r /build/requirements.txt

COPY build_appimage.sh /entrypoint.sh

CMD /entrypoint.sh
