import time
from TwitterProducer import *

def main():
    producer = TwitterProducer("twitter-topic1", ["iOS", "Swift", "UIKit"])
    producer.daemon = True
    producer.start()
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()