Linux Process Monitor (Kernel-Aware)

A lightweight Linux process monitoring tool written in Python that collects real-time process metrics directly from the Linux kernel via the /proc filesystem.

This project demonstrates low-level Linux knowledge, kernel–userspace interaction, and production-grade monitoring concepts used by tools like top and htop.


Features:
Real-time process monitoring
Direct kernel interaction via /proc
No external commands (ps, top, etc.)
CPU usage calculation using scheduler deltas
Memory usage (RSS)
File descriptor tracking
Process state detection (running, sleeping, zombie, I/O wait)
Safe handling of short-lived processes
Designed for extensibility (alerts, exporters, eBPF)

Architecture:
┌────────────┐
│  Kernel    │
│ (/proc FS) │
└─────┬──────┘
      │
┌─────▼──────────────┐
│ monitor.py         │
│                    │
│ - PID discovery    │
│ - CPU accounting   │
│ - Memory tracking  │
│ - FD counting      │
│ - State detection  │
└─────┬──────────────┘
      │
┌─────▼──────┐
│ Metrics    │
│ Collection │
└────────────┘

Project Structure:
.
├── monitor.py        # Core monitoring logic
├── agent/            # (Optional) extensions / collectors
├── requirements.txt  # Python dependencies (if any)
└── README.md
