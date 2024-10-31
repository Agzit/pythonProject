# Исходные данные
documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_document_owner(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            return doc['name']
    return "Документ не найден."


def get_document_shelf(doc_number):
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return "Документ не найден."

def main():
    while True:
        command = input("Введите команду (для выхода введите 'q'): ")
        if command == 'q':
            print("Выход из программы.")
            break
        elif command == 'p':
            doc_number = input("Введите номер документа: ")
            owner = get_document_owner(doc_number)
            print(f"Владелец документа: {owner}")
        elif command == 's':
            doc_number = input("Введите номер документа: ")
            shelf = get_document_shelf(doc_number)
            print(f"Документ хранится на полке: {shelf}")
        else:
            print("Неизвестная команда. Пожалуйста, попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()
