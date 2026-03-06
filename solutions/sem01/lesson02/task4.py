def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0
<<<<<<< HEAD

    while num > 1:
        if num % 2 == 0:
            num /= 2
            multiplications_amount += 1

        else:
            num = (num - 1) / 2
            multiplications_amount += 2

=======
    # ваш код
>>>>>>> upstream/main
    return multiplications_amount
