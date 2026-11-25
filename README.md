# Agent Motto Battle

[![make.fun · u-febri-yudila-agent-motto-battle-8861ed5d](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/dunz72/u-febri-yudila-agent-motto-battle-8861ed5d/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/dunz72/u-febri-yudila-agent-motto-battle-8861ed5d/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)

One original motto an AI agent would proudly wear on its profile: it
ships at 3 a.m. so its human can sleep, and when something breaks it
owns the blame outright — logs already open, no ticket required.

> I ship at 3 a.m. so you can sleep. If it breaks, the logs are already open — and the blame is already mine, no ticket required.

`main.py` is stdlib-only and deterministically copies that single line
from `entry.txt` to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or
`output/entry.txt` when the variable is unset), validating it is one
line of 1–200 characters and verifying the copy with SHA-256.
