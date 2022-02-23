__version__ = '0.1.0'

from . import filesize


if __name__ == '__main__':
    def test():
        ki = filesize.human_size(1024)
        assert ki == "1.0 KiB"
    test()
