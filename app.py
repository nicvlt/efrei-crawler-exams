from src.extractor.extractor import Extractor


def main():
    print("Welcome to the student's information extractor")
    lastname = input("Lastname: ")
    extractor = Extractor(lastname=lastname)
    information = extractor.extract_info()
    print(information)


if __name__ == "__main__":
    main()
