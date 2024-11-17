def get_mask_card_number(number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    list_of_numbers_card = []

    if number.isdigit() and len(number) == 16:
        # делим номер карты на группы по 4 цифры
        list_of_numbers_card.append(number[0:4])
        list_of_numbers_card.append(number[4:8])
        list_of_numbers_card.append(number[8:12])
        list_of_numbers_card.append(number[12:])

        # во второй группе меняем две последние цифры на звездочки
        element_two_in_number = list_of_numbers_card[1]
        element_two_in_number_and_stars = element_two_in_number.replace(element_two_in_number[2:], "**")
        list_of_numbers_card[1] = element_two_in_number_and_stars

        # в третьей группе меняем цифры на звездочки
        list_of_numbers_card[2] = "****"

        mask_number = " ".join(list_of_numbers_card)

        return mask_number

    else:
        return "Введен некорректный номер карты"


def get_mask_account(account: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    list_of_numbers_account = ["**"]

    if account.isdigit() and len(account) == 20:
        list_of_numbers_account.append(account[-4:])
        mask_account = "".join(list_of_numbers_account)
        return mask_account

    else:
        return "Введен некорректный номер счета"
