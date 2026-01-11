import os
import time


def get_pids():
    return [int(pid) for pid in os.listdir("/proc") if pid.isdigit()]

def read_state(pid):
    with open(f"/proc/{pid}/stat") as f:
        return f.read().split()[2]

def read_rss(pid):
    with open(f"/proc/{pid}/status") as f:
        for line in f:
            if line.startswith("VmRSS"):
                return int(line.split()[1])
    return 0

def get_total_cpu_time():
    with open("/proc/stat") as f:
        cpu = f.readline().split()[1:]
        return sum(map(int, cpu))


def main():
    print("Monitoring started...")
    while True:
        print("Collecting process information...")
        for pid in get_pids():
            try:
                state = read_state(pid)
                rss = read_rss(pid)
                cpu_time = get_total_cpu_time()
                print(pid, state, rss)
                print(f"Total CPU time: {cpu_time}")
            except Exception:
                continue
        time.sleep(10)


if __name__ == "__main__":
    main()
