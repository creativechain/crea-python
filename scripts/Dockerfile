# The purpose of this docker file is to provide a shell with
# dpay-python pre-installed for interactive testing purposes.
#
# Usage:
# docker build -t dpaycli .
# docker run -it dpaycli

FROM python:3.5.3
MAINTAINER furion <_@furion.me>

# set default password for BIP38 encrypted wallet
ENV UNLOCK test123

RUN pip install ipython
RUN pip install git+git://github.com/dpays/dpay-python.git

CMD "ipython"
