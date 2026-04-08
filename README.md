# Marketplace Negotiation Environment

## Overview
This project implements a real-world OpenEnv environment simulating buyer–seller negotiation in online marketplaces.

The agent acts as a seller and must decide whether to accept, reject, or counter buyer offers.

---

## Key Features

- Multi-step negotiation
- Dynamic buyer behavior (aggressive, normal, generous)
- Reward shaping based on profit and strategy
- Easy, Medium, and Hard tasks

---

## Action Space

- accept
- reject
- counter

---

## Observation Space

- listed_price
- buyer_offer
- round
- max_rounds

---

## Reward

The agent receives a score between 0 and 1 based on:
- profit margin
- negotiation strategy
- efficiency (number of rounds)

---

## Tasks

- High Offer (Easy)
- Medium Offer (Medium)
- Dynamic Negotiation (Hard)

---

## Run

```bash
python run_baseline.py# openenv-marketplace-negotiation-final
