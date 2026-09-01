# Each agent writes its own heartbeat file, reads its partner's, and reports how long since the partner was last seen.
import time
import os

# Strips path components to prevent typed name from escaping mailroom. Strips white spaces to prevent blank-looking filenames.
name = os.path.basename(input("Who am I? "))
name = name.strip()
partner = os.path.basename(input("Who am I talking to? "))
partner = partner.strip()
if not name or not partner:
    raise SystemExit("Please enter a valid name")
nudge_sent = False

minutes = int(input("Maximum length in duration (minutes): "))
if minutes <= 0:
    raise SystemExit("Please enter only positive numbers.")
seconds = minutes * 60
stop_time = time.time() + seconds

while True:
    time.sleep(2)
    if time.time() > stop_time:
        print(f"Time limit of {minutes} minute(s) reached. Stopping.")
        break
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

        # Nudge is named for the recipient, so the partner finds it under their own name. After message is sent, nudge_sent is True. If time difference < 5 seconds, nudge_sent is False.
        if time_difference > 5:
            if not nudge_sent:
                with open(f"mailroom/{partner}-nudge.txt", "w") as f:
                    f.write("hey you've been quiet")
                print("hey you've been quiet")
                nudge_sent = True
        else:
            nudge_sent = False

    # Nudge is read by recipient, then deleted after to prevent repeat message.
    if os.path.exists(f"mailroom/{name}-nudge.txt"):
        with open(f"mailroom/{name}-nudge.txt", "r") as f:
            message = f.read()
        print(message)
        os.remove(f"mailroom/{name}-nudge.txt")