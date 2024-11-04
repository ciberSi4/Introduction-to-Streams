# Домашнее задание по теме "Введение в потоки".

import time
from threading import Thread

def write_words(word_count, file_name): # Функция записывает слова в указанный файл
    # Открываем файл для записи
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f"Какое-то слово № {i}\n" # Формируем строку для записи
            file.write(word) # Пишем строку в файл
            time.sleep(0.1) # Делаем паузу на 0.1 секунды
    print(f"Завершилась запись в файл: {file_name}")


# Основная программа
if __name__ == "__main__":

    start_time_functions = time.time() # Начало измерения времени выполнения последовательных вызовов функций
    # Вызываем функции последовательно
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")
    end_time_functions = time.time() # Конец измерения времени выполнения последовательных вызовов функций
    print(f"Время выполнения функций: {end_time_functions - start_time_functions:.2f} секунд.")

    start_time_threads = time.time() # Начало измерения времени выполнения потоков
    threads = [] # Создаем список потоков
    # Создаем потоки
    thread1 = Thread(target=write_words, args=(10, "example5.txt"))
    thread2 = Thread(target=write_words, args=(30, "example6.txt"))
    thread3 = Thread(target=write_words, args=(200, "example7.txt"))
    thread4 = Thread(target=write_words, args=(100, "example8.txt"))
    # Добавляем потоки в список
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)
    threads.append(thread4)

    for t in threads: # Запускаем все потоки
        t.start()

    for t in threads: # Ожидаем завершения всех потоков
        t.join()

    end_time_threads = time.time() # Конец измерения времени выполнения потоков
    print(f"Время выполнения потоков: {end_time_threads - start_time_threads:.2f} секунд.")