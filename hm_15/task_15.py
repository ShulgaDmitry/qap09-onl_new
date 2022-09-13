# Создайте новый репозиторий в github. Создайте программку и залейте её в этот репозиторий.
# Программа следующая:
# Я сейчас скину вам 3 файла, скачайте их себе
# Программа должна:
# 1. прочитать все файлы
# 2. Вывести на экран сколько букв, цифр и спецсимволов в каждом из файлов
# 3. Вывести на экран среднее арифметическое всех цифр для каждого из файлов
# 4. Вывести на экран Топ 3 букв для каждого файла (Топ 3 по количеству)
# 5. Сравнить количество уникальных букв в каждом файле и вывести на экран в каком файле больше всего уникальных букв.
# Если во всех файлах одинаково, вывести на экран, что количество - одинаковое.
# 6. Вывести на экран сумму чисел из всех трех файлов
# 7. Вывести на экран сколько во всех файлах среди спецсимволов знаков препинания (!-(),.:;?), а сколько прочих символов
#
# !!! В пунктах 4 и 5 буква в верхнем регистре = букве в нижнем регистре.
#
# Программа - это не обязательно один файл, она может состоять из нескольких файлов.
# Всё задание в принципе может быть решено с помощью функций, но лучше и аккуратнее будет использовать классы.
# Только если совсем не получается выполнить с помощью классов, то решайте чисто функциями. Но лучше спросите в чате - я
# или кто-нибудь из группы подскажет как выйти из ступора.
# Пример результата работы программы:
#
# Файл1:
# 200 букв, 300 цифр, 400 символов
# среднее арифметическое: 4
# Топ 3 букв:
# А - количество: 33
# D - количество: 30
# Y - количество: 28
# В файле Файл2 больше всего уникальных букв (20)
# Сумма всех чисел: 100
# Всего в файлах 100 знаков препинания и 200 прочих спецсимволов

import string


class Sorting:

    def __init__(self, contents):
        self.contents = contents

    def count_alpha(self):
        count_1 = 1
        count_2 = 1
        count_3 = 1
        for content in self.contents:
            if content.isalpha():
                count_1 += 1
            elif content.isdigit():
                count_2 += 1
            else:
                count_3 += 1

        print(f"{count_1}-букв, {count_2}-цмфр, {count_3}-символов ")

    def only_numbers_sum(self):

        sum_all = 0
        for content in self.contents:
            if content.isdigit():
                content = int(content)
                sum_all += content
        return sum_all

    def average(self, sum_all):

        count = 1
        for content in self.contents:
            if content.isdigit():
                count += 1
        print(f"Среднее арифметическое: {round(sum_all/ count, 2)}")

    def top_alpha(self):
        content_list = {}
        for content in self.contents:
            if content.isalpha():
                content = content.upper()
                content_list[content] = self.contents.count(content)

        content_list_max = sorted(content_list.values(), reverse=True)
        final_contex_list = {}

        for content_max in content_list_max[:3]:
            for k, v in content_list.items():
                if content_max == v:
                    final_contex_list[k] = v

        count = 1
        for final_contex in final_contex_list:
            if count <= 3:
                print(f"{final_contex} - {final_contex_list[final_contex]}")
                count += 1

    def unique_alpha(self):

        unique_alpha_list = {}
        for content in self.contents:
            if content.isalpha():
                content = content.upper()
                if content in unique_alpha_list:
                    unique_alpha_list[content] += 1
                else:
                    unique_alpha_list[content] = 1
        return len(unique_alpha_list.keys())

    def special_symbols(self):

        count_punctual = 1
        count_symbol = 1
        for content in self.contents:
            if content in string.punctuation:
                count_punctual += 1
            elif not content.isalpha() and content.isdigit():
                count_symbol += 1
        return count_punctual, count_symbol


class Common_sorting:

    def __init__(self, *args):
        self.args = args

    def unique_alpha_max(self):

        unique_list = []
        for arg in self.args:
            unique_list.append(arg)
        if unique_list.count(unique_list[0]) == len(unique_list):
            print("Количество уникальных букв одинаково")
        else:
            max_unique_list = max(unique_list)
            print(
                f"В файле Файл{unique_list.index(max_unique_list) + 1} больше всего уникальных букв: {max_unique_list}")

    def sum_all_numbers(self):

        sum_all = 0
        for arg in self.args:
            sum_all += arg
        print(f"Сумма всех чисел: {sum_all}")

    def sum_special_symbols(self):

        list_specials = self.args
        result = [sum(tup) for tup in zip(*list_specials)]
        print(f"Всего в файлах {result[0]} знаков препинания и {result[1]} прочих спецсимволов")


filename_1 = "file7.txt"
filename_2 = "file8.txt"
filename_3 = "file9.txt"

with open(filename_1) as file_object_1:
    contents_1 = file_object_1.read()

with open(filename_2) as file_object_2:
    contents_2 = file_object_2.read()

with open(filename_3) as file_object_3:
    contents_3 = file_object_3.read()

print("Файл 1")
sort_1 = Sorting(contents_1)
sort_1.count_alpha()
sort_1.average(sort_1.only_numbers_sum())
print("Топ 3 букв")
sort_1.top_alpha()

print("\n")

print("Файл 2")
sort_2 = Sorting(contents_2)
sort_2.count_alpha()
sort_2.average(sort_2.only_numbers_sum())
print("Топ 3 букв")
sort_2.top_alpha()

print("\n")

print("Файл 3")
sort_3 = Sorting(contents_3)
sort_3.count_alpha()
sort_3.average(sort_3.only_numbers_sum())
print("Топ 3 букв")
sort_3.top_alpha()

print("\n")

unique_1 = sort_1.unique_alpha()
unique_2 = sort_2.unique_alpha()
unique_3 = sort_3.unique_alpha()
common_sort_1 = Common_sorting(unique_1, unique_2, unique_3)
common_sort_1.unique_alpha_max()

number_1 = sort_1.only_numbers_sum()
number_2 = sort_2.only_numbers_sum()
number_3 = sort_3.only_numbers_sum()
common_sort_2 = Common_sorting(number_1, number_2, number_3)
common_sort_2.sum_all_numbers()

special_1 = sort_1.special_symbols()
special_2 = sort_2.special_symbols()
special_3 = sort_3.special_symbols()
common_sort_3 = Common_sorting(special_1, special_2, special_3)
common_sort_3.sum_special_symbols()

