from controllers.stream import Stream
from models.pitch import Pitch


class App:
    @classmethod
    def model_to_view(cls, pitch: Pitch, freq: float) -> None:
        print(pitch, freq, 'Hz')

    @classmethod
    def main(cls):
        stream = Stream(cls.model_to_view)
        stream.start()

        input('Press any key to exit')


if __name__ == '__main__':
    App.main()
