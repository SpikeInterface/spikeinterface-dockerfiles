FROM python:3.8

RUN pip install scipy PyWavelets matplotlib tables PyQt5
RUN mkdir -p /src && git clone https://github.com/jniediek/combinato && cd combinato && python setup_options.py && cd ..

ENV COMBINATO_PATH="/combinato"
RUN echo $COMBINATO_PATH
