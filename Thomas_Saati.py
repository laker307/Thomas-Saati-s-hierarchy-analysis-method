import numpy as np

def enter(count): # функция обработки данных
    b = np.eye(count)    # cоздаётся двумерный массив необходимого размера
    sums = list()        # список с суммами по строкам
    if count > 0:
        for j in range(count):  # цикл
            for i in range(j,count):   # вложенный цикл
                print('Введите данные попарного сравнения критериев ', j+1, ' и ', i+1)
                b[j,i] = float(input())     # ввод данных попарного сравнения критериев справа от главной диагонали
                b[i,j] = np.around((1/(b[j,i])), 2)    # заполнение ячеек слева от главной диагонали
            sums.append(np.around(sum(b[j]),2)) # добавление суммы по строке в список
        print(b,'\n\n',sums,'\n\n')
        f = sum(sums) # сумма всех сумм
        print(np.around(sums/f,2))  # вывод коэфф.



if __name__ == '__main__':
    while True: # бесконечный цикл
        try: # обработка ошибок
            print('Введите количество критериев (отличное от 0): ')
            enter(int(input()))    # вводим и передаём данные в функцию
        except ValueError:
            enter(0)