import sys
import time

for path in sys.path:
    print(path)

from tqdm import tqdm

# for n in tqdm(range(100)):
#     time.sleep(0.1)


class TestClassAPIView:

    def __init__(self):
        print(dir(self.__class__))
        print(self.__class__.__name__)

t = TestClassAPIView()
