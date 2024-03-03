import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_pattern = re.compile(
        r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.("
        r"25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.("
        r"25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.("
        r"25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
    )

    return bool(ip_pattern.match(ip))


if __name__ == "__main__":
    main()
