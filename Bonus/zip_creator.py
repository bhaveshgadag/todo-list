import zipfile
import pathlib


def make_archive(files, destination):
    destination = pathlib.Path(destination, 'compressed.zip')
    with zipfile.ZipFile(destination, 'w') as archive:
        for filepath in files:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    make_archive(files=['B_D1_1.py', 'B_D2_1.py'], destination='dest')
