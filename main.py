# Ввод кол-ва инвестированных денег
deposit_money = int(input("Введите сумму вклада:"))
# Создаю словарь с распределением процентных ставок по вкладам
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

procent = list(per_cent.values()) # словарь перевожу в список

# записываю доход в каждом банке в переменнуые и округляю
bank_TKB = round(procent[0] * deposit_money)
bank_CKB = round(procent[1] * deposit_money)
bank_VTB = round(procent[2] * deposit_money)
bank_SBER = round(procent[3] * deposit_money)

deposit = [bank_TKB, bank_CKB, bank_VTB, bank_SBER] # список с возможными доходами

print("Возможный доход:", deposit)

sorted_deposit = sorted(deposit) # Нахождение максимального значения с помощью функции sorted()
result = sorted_deposit[-1]

print("Максимальная сумма, которую вы можете заработать - ", (result)) # вывожу максимальный доход


