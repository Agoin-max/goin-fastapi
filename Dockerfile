FROM python:3.8.6
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /src/
ADD ./requirements.txt /src/
RUN pip install -r /src/requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple
ADD . /src/
CMD gunicorn run:app -b 0.0.0.0:8000 -w 4 -k uvicorn.workers.UvicornWorker
