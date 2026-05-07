import time
import os
import random

HELLO = [
    "██╗  ██╗███████╗██╗     ██╗      ██████╗ ",
    "██║  ██║██╔════╝██║     ██║     ██╔═══██╗",
    "███████║█████╗  ██║     ██║     ██║   ██║",
    "██╔══██║██╔══╝  ██║     ██║     ██║   ██║",
    "██║  ██║███████╗███████╗███████╗╚██████╔╝",
    "╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ "
]

colors = [
    "\033[91m",  # 빨강
    "\033[93m",  # 노랑
    "\033[92m",  # 초록
    "\033[96m",  # 하늘
    "\033[94m",  # 파랑
    "\033[95m",  # 보라
]

RESET = "\033[0m"
BOLD = "\033[1m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.02):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

clear()

for i in range(3):
    clear()
    print(random.choice(colors) + BOLD)
    for line in HELLO:
        print(" " * i + line)
    print(RESET)
    time.sleep(0.2)

clear()

print(BOLD + random.choice(colors))
for line in HELLO:
    slow_print(line, 0.005)

print(RESET)
print("\n✨ Python says: Hello, world! ✨")
print("🚀 실행 성공. 오늘도 코드 한 줄로 세상을 흔들었다.")
