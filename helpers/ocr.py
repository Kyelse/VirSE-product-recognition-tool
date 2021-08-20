import easyocr
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(f"Wrong argument format. Usage: python {sys.argv[0]} path/to/img")
    else:
        reader = easyocr.Reader(["en", "vi"])

        res = reader.readtext(sys.argv[1], detail=0, paragraph=True)
        print(res)
