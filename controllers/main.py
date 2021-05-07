from controllers.stream import Stream
from models.pitch import Pitch


def model_to_view(pitch: Pitch, freq: float) -> None:
    print(pitch, freq, 'Hz')


def main():
    stream = Stream(model_to_view)
    stream.start()

    input('Press any key to exit')


if __name__ == '__main__':
    main()
