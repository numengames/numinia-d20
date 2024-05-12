# This file is part of the D20 Governance Bot project.
# Copyright (c) 2023 The Metagovernance Project
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

FROM python:3.10-slim

WORKDIR /bot

COPY pyproject.toml poetry.lock* ./

RUN apt-get update && apt-get install -y \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
    tini libffi-dev shared-mime-info \
    && rm -rf /var/lib/apt/lists/* \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && pip install "emoji==2.6.0" \
    && pip install "svglib==1.5.1" \
    && poetry install --only main

COPY . .

ENV PYTHONPATH /bot

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["poetry", "run", "python3", "-m", "d20_governance"]