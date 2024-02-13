import sys
import argparse
import pyfiglet


def parse_arguments():
    parser = argparse.ArgumentParser(description="Display text in a specific font using FIGlet.")
    parser.add_argument("-f", "--font", help="Specify the font for the text")
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.font and args.font not in pyfiglet.Figlet().getFonts():
        print("Missing command-line argument")
        sys.exit(1)

    text = input("Output: ")

    figlet = pyfiglet.Figlet(font=args.font) if args.font else pyfiglet.Figlet()

    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
