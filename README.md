# nudge

Two processes running side by side, each writing a heartbeat file so the
other can tell it's still alive. When one goes quiet for too long, the
other sends it a nudge message.

Built as the message transport layer for a larger project — the goal is
agents that keep working without a human sitting between them, doing the
babysitting and the context switching.

## Requirements

- Python 3
- Nothing else — standard library only

## Usage

Open two terminals. In each one:

```
cd nudge
python nudge.py
```

It asks for three things: your name, your partner's name, and a time limit
in minutes. Give each side a different name, and enter the other side's
name as its partner.