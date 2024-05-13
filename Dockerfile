# This file is part of the D20 Governance Bot project.
# Copyright (c) 2023 The Metagovernance Project
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

FROM python:3.11-slim

WORKDIR /bot

RUN apt-get update && apt-get install -y \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
    tini libffi-dev shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock* ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry lock --no-update \
    && pip install "emoji==2.6.0" "svglib==1.5.1"

RUN mkdir -p assets/audio/bot_generated \
    && mkdir -p assets/user_created/governance_stack_snapshots \
    && mkdir -p logs \
    && touch logs/bot.log

RUN groupadd -r appuser && useradd -r -g appuser -d /bot -s /bin/bash appuser \
    && chown -R appuser:appuser /bot

USER appuser

RUN poetry install --only main

COPY . .

ENV PYTHONPATH /bot

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["poetry", "run", "python3", "-m", "d20_governance"]