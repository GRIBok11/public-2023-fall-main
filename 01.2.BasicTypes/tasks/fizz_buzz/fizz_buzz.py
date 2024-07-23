def get_fizz_buzz(n: int) -> list[int | str]:
    """
    If value divided by 3 - "Fizz",
       value divided by 5 - "Buzz",
       value divided by 15 - "FizzBuzz",
    else - value.
    :param n: size of sequence
    :return: list of values.
    """
    list_fizz_buzz = []
    for x in range(1, n+1):
        if x % 15 == 0:
            list_fizz_buzz.append("FizzBuzz")
        

        elif x % 5 == 0:
            list_fizz_buzz.append("Buzz")
        elif x % 3 == 0:
            list_fizz_buzz.append("Fizz")

        else:
            list_fizz_buzz.append(x)
    

    return list_fizz_buzz


print(get_fizz_buzz(16))
            
