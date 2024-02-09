import mimetypes


def get_media_type(file_name):
    media_type, _ = mimetypes.guess_type(file_name)
    return media_type if media_type else "application/octet-stream"


def extensions_program():
    file_name = input("Enter the name of a file: ").strip()

    media_type = get_media_type(file_name.lower())
    print(media_type)


if __name__ == "__main__":
    extensions_program()
