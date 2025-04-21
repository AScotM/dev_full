import datetime
import os
import sys
import traceback

TARGET = "/dev/full"
DATA = f"Test entry: {datetime.datetime.now()}"
DIVIDER = "=" * 50

def get_timestamp():
    """Returns a formatted timestamp."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def print_header():
    """Prints the header information with timestamp and target."""
    print(DIVIDER)
    print(f"Start of /dev/full write test")
    print(f"Timestamp: {get_timestamp()}")
    print(f"Target file: {TARGET}")
    print(DIVIDER)

def print_footer():
    """Prints the footer message."""
    print(DIVIDER)
    print("Test complete.")
    print(DIVIDER)

def test_dev_full_write():
    """Attempts to write to /dev/full and handles different exceptions."""
    print(f"Attempting to write to {TARGET}...")
    try:
        with open(TARGET, "w") as f:
            f.write(DATA)
        print("Unexpected result: Write succeeded.")
        print("This should not happen with /dev/full. Please investigate system behavior.")
    except OSError as e:
        if e.errno == 28:
            print("Expected failure: Disk full simulation successful.")
            print(f"OSError [Errno {e.errno}]: {e.strerror}")
        else:
            print("OSError occurred, but not a typical 'disk full' error.")
            print(f"[Errno {e.errno}]: {e.strerror}")
    except Exception as ex:
        print("An unexpected exception occurred during the write operation.")
        print("Exception details:")
        print(f"{type(ex).__name__}: {str(ex)}")
        traceback.print_exc()

def main():
    """Main execution point for the script."""
    print_header()
    test_dev_full_write()
    print_footer()

if __name__ == "__main__":
    main()
