FROM appimagecrafters/appimage-builder

WORKDIR /build

RUN ln -snf /usr/share/zoneinfo/UTC /etc/localtime && echo UTC > /etc/timezone
RUN apt-get update && apt-get install python3-tk python3-dev -y

COPY requirements.txt requirements.txt

RUN pip3 install -r ./requirements.txt

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT /entrypoint.sh