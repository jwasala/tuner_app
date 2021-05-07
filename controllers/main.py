from controllers.stream import Stream
from models.pitch import Pitch


def model_to_view(pitch: Pitch, freq: float) -> None:
    print(pitch, freq)


stream = Stream(model_to_view)
stream.start()

while True:
    pass
