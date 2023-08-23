import sys

# Check if there are enough command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# Iterate through each command-line argument
for arg in sys.argv:
    print("hello, my name is", arg)

import sys

# Check if there are enough command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# Iterate through each command-line argument (excluding the script name)
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
