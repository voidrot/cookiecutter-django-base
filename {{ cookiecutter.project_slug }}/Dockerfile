FROM python:3.13-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN groupadd --gid 1000 warden \
    && useradd --uid 1000 --gid warden --shell /bin/bash --create-home warden

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY --chown=warden:warden . /app

USER warden

WORKDIR /app

RUN uv sync --frozen && \
    mv /app/scripts/start.sh /app/start.sh


ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT [ "bash", "/app/start.sh" ]
CMD ["server"]%
