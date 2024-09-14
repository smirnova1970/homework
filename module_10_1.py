from time import sleep
from threading import Thread
from datetime import datetime


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f"Какое-то слово № {i}"
            file.write(word + '\n')

            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


start_time_func = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time_func = datetime.now()


print(f"Время выполнения функций: {end_time_func - start_time_func} секунд")


start_time_thread = datetime.now()

thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

end_time_thread = datetime.now()

print(f"Время выполнения потоков: {end_time_thread - start_time_thread} секунд")
