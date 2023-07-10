import zipfile

def extract_archive(archivepath, destination):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(destination)
