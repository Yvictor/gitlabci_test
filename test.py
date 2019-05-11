import sys
import time

sys.stdout.flush()

print(sys.executable)
print(sys.version_info)

for i in range(30):
  print(f"IDLE: {i}")
  time.sleep(1)
