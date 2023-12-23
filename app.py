from src.extractor.extractor import Extractor
from unidecode import unidecode


def main():
    print("Welcome to EFREI Crawler Exams!\n\n\n")
    lastname = unidecode(input("Enter your lastname: "))
    extractor = Extractor(lastname=lastname)
    information = extractor.extract_info()
    print(information)


if __name__ == "__main__":
    main()
