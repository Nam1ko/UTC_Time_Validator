class Console:

    def __init__(self, repository, service):
        self.repository = repository
        self.service = service

    def run(self):
        while True:
            print("\n==========UTC TIME VALIDATOR==========")
            print("1. Найти время в тексте")
            print("2. Найти время на сайте")
            print("3. Найти время в файле")
            print("0. Выход")

            choice = input("\nВыберите действие: ")

            if choice == "1":
                self.search_input()
            elif choice == "2":
                self.search_url()
            elif choice == "3":
                self.search_file()
            elif choice == "0":
                print("Завершение программы")
                break
            else:
                print("Неверный пункт меню")

    def search_input(self):
        text = self.repository.get_from_input()
        self.show_results(self.service.search(text))

    def search_url(self):
        url = input("Введите URL: ")
        text = self.repository.get_from_url(url)

        if text is None:
            print("Не удалось получить данные с сайта")
            return

        self.show_results(self.service.search(text))

    def search_file(self):
        file_path = input("Введите путь к файлу: ")
        text = self.repository.get_from_file(file_path)

        if text is None:
            print("Не удалось прочитать файл")
            return

        self.show_results(self.service.search(text))

    def show_results(self, results):
        if not results:
            print("Временные отметки UTC не найдены")
            return

        print(f"\nНайдено временных отметок: {len(results)}")

        for timestamp in results:
            print(timestamp)