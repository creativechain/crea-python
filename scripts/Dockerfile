# The purpose of this docker file is to provide a shell with
# crea-python pre-installed for interactive testing purposes.
#
# Usage:
# docker build -t creacli .
# docker run -it creacli

FROM python:3.5.3
MAINTAINER furion <_@furion.me>

# set default password for BIP38 encrypted wallet
ENV UNLOCK test123

RUN pip install ipython
RUN pip install git+git://github.com/creativechain/crea-python.git

CMD "ipython"
