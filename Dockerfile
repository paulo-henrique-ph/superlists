FROM python:3-alpine

ARG secretKey

ADD requirements/prod.txt /app/requirements.txt

RUN set -ex \
    && apk add --no-cache --virtual .build-deps build-base \
    && python -m venv .venv \
    && /.venv/bin/pip install --upgrade pip \
    && /.venv/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive ./venv \
        | awk '{ gsub(/,/, "\nso:"; print "so:" $2}' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

ADD superlists /app
ADD static /
WORKDIR /app

ENV VIRTUAL_ENV /.venv
ENV PATH /.venv/bin:$PATH
ENV SECRET_KEY $secretKey

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "superlists.wsgi"]
