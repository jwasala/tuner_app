from models.stream import Stream, TuningStatus


def update_view(ts: TuningStatus) -> None:
    print(ts.closest_pitch, ts.freq, 'Hz', [(str(p), b) for (p, b) in ts.strings])


def main():
    stream = Stream(update_view)
    stream.start()

    input('Press any key to exit\n')


if __name__ == '__main__':
    main()
