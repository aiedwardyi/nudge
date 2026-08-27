# Each agent writes its own heartbeat file and reads its partner's.
import time
import os

name = input("Who am I? ")
partner = input("Who am I talking to? ")
while True:
    time.sleep(2)
    with open(f"mailroom/{name}.txt", "w") as f:
        f.write(f"{name} is alive {time.time()}")
    print(f"{name} is alive {time.time()}")

    # Partner may not have started yet, so the file might not exist.
    if os.path.exists(f"mailroom/{partner}.txt"):
        with open(f"mailroom/{partner}.txt", "r") as f:
            text = f.read()
        print(f"{text}")