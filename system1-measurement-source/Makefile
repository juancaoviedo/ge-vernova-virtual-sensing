# Makefile — IEEE 33-Bus DER Measurement Source (System 1)
# Wraps the ordered runbook: up → ingest → sim → validate.
# See README.md for the full step-by-step "rhythm" from a clean checkout.
#
# Prerequisites: Docker + Compose v2, uv (https://github.com/astral-sh/uv)
# Run `uv sync` once before using ingest/sim/validate targets.

.PHONY: up down ingest sim validate all clean

up:
	docker compose up -d

ingest: up
	uv run ingest

sim: up
	uv run sim

validate:
	uv run validate

all: up ingest sim

down:
	docker compose down

clean: down
	docker volume rm system1-measurement-source_influxdb-data system1-measurement-source_influxdb-config system1-measurement-source_grafana-data 2>/dev/null || true
