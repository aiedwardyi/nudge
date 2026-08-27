# Each agent writes its own heartbeat file, reads its partner's, and reports how long since the partner was last seen.
import time
import os

name = input("Who am I? ")
partner = input("Who am I talking to? ")
while True:
    time.sleep(2)
    with open(f"mailroom/{name}.txt", "w") as f:
        f.write(f"{name} is alive {time.time()}")
    print(f"{name} is alive")

    # Partner may not have started yet, so the file might not exist.
    if os.path.exists(f"mailroom/{partner}.txt"):
        with open(f"mailroom/{partner}.txt", "r") as f:
            text = f.read()
            words = text.split()
            time_difference = time.time() - float(words[-1])
        print(f"{words[0]} last seen {time_difference:.2f} seconds ago")