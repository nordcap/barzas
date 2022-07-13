from openpyxl import load_workbook
import re


# функция обработки листа навигации и возвр. словарь ходок без учета кол-ва ходок
def calc_trip(sheet, MAXROW):
    # создаем словарь с распарсенными данными вида {'Howo №100': {'01.12.2021. Смена 1': [('Склад ДСУ1,2,3', 'Ж/Д склад')}}
    global name_tonar
    dict_move = dict()
    name_date = ""

    for row in range(5, MAXROW):
        # 1 ячейка
        find_str = str(sheet.cell(row=row, column=1).value)
        # ищем строку вида Тонар №2694
        match_tonar = re.findall(r".*\s№.*", find_str)
        if len(match_tonar) > 0:
            name_tonar = match_tonar[0]
            # если ключа нет в словаре, то добавляем и продолжаем цикл
            if name_tonar not in dict_move:
                dict_move[name_tonar] = dict()
                continue
        # ищем строку вида 02.10.2021. Смена 2
        match_date = re.findall(r"(\d{2}\.\d{2}\.\d{4}(\s|\S)*)", find_str)
        if len(match_date) > 0:
            name_date = match_date[0][0]
            dict_move[name_tonar][name_date] = []
            continue

        match_num = re.findall(r"\d{1,3}", find_str)
        if len(match_num) > 0:
            # 2 Ячейка -Зона погрузки
            zone_1 = str(sheet.cell(row=row, column=2).value)
            # 3 Ячейка -Зона разгрузки
            zone_2 = str(sheet.cell(row=row, column=3).value)
            dict_move[name_tonar][name_date].append((zone_1, zone_2))
    return dict_move


# функция расширения calc_trip для подсчета кол-ва ходок
def calc_trip_adv(dict_move):
    dict_auto = dict()
    for key_tonar in dict_move:
        dict_auto[key_tonar] = dict()
        for key_date in dict_move[key_tonar]:
            list_zone = list(set(dict_move[key_tonar][key_date]))
            list_zone.sort()
            dict_auto[key_tonar][key_date] = dict()
            for zone in list_zone:
                count_zone = dict_move[key_tonar][key_date].count(zone)  # кол-во ходок
                dict_auto[key_tonar][key_date][zone] = count_zone
    return dict_auto


def handle_upload_file(file):
    wb = load_workbook(filename=file)
    sheet = wb.active
    dict_move = calc_trip(sheet, sheet.max_row)
    dict_trip = calc_trip_adv(dict_move)
    return dict_trip
