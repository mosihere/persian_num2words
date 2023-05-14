import small_module.small_function


ones = {
    0: '',
    1: 'یک',
    2: 'دو',
    3: 'سه',
    4: 'چهار',
    5: 'پنج',
    6: 'شش',
    7: 'هفت',
    8: 'هشت',
    9: 'نه',
}

ten_to_nineteen = {
    10: 'ده',
    11: 'یازده',
    12: 'دوازده',
    13: 'سیزده',
    14: 'چهارده',
    15: 'پانزده',
    16: 'شانزده',
    17: 'هفده',
    18: 'هجده',
    19: 'نوزده',
}

twenties_and_others = {
    0: '',
    1: '',
    2: 'بیست',
    3: 'سی',
    4: 'چهل',
    5: 'پنجاه',
    6: 'شصت',
    7: 'هفتاد',
    8: 'هشتاد',
    9: 'نود',
}

hundreds = {
    0: '',
    1: 'صد',
    2: 'دویست',
    3: 'سیصد', 
    4: 'چهارصد',
    5: 'پانصد',
    6: 'ششصد',
    7: 'هفتصد',
    8: 'هشتصد',
    9: 'نهصد',
}

thousands = {
    0: '',
    1: 'یک هزار',
    2: 'دو هزار',
    3: 'سه هزار', 
    4: 'چهار هزار',
    5: 'پنح هزار',
    6: 'شش هزار',
    7: 'هفت هزار',
    8: 'هشت هزار',
    9: 'نه هزار',
}

ten_thousands = {
    0: '',
    1: 'ده',
    2: 'بیست',
    3: 'سی', 
    4: 'چهل',
    5: 'پنحاه',
    6: 'شصت',
    7: 'هفتاد',
    8: 'هشتاد',
    9: 'نود',
}
    
milions = {
    0: '',
    1: 'ده',
    2: 'بیست',
    3: 'سی', 
    4: 'چهل',
    5: 'پنحاه',
    6: 'شصت',
    7: 'هفتاد',
    8: 'هشتاد',
    9: 'نود',
}


def num_to_word(number: int) -> str:
    """
    Convert Numbers to Words(Persian)
    This function accepts a single argument as number
    then returns That number in Persian Words.

    Args:
        number: int
    
    Return:
        str: Number in Persian Words.

    
    Doc Test:

    >>> print(num_to_word(0))
    صفر

    >>> print(num_to_word(415))
    چهارصد و پانزده

    >>> print(num_to_word(999999))
    This Program Support Numbers Between 0-999999

    >>> print(num_to_word(913))
    نهصد و سیزده
    """


    assert isinstance(number, int), 'You Must Enter an Integer!'

    str_number = str(number)


    if number == 0:
        return 'صفر'

    if number <= 9:
        return ones[number]
    
    elif number > 9 and number <= 19:
        return f'{ten_to_nineteen[number]}'
    

    elif number > 19 and number <= 99:
        if str_number[1] == '0':
            find_number = int(str_number[0])

            return f'{twenties_and_others[find_number]}'
                
        find_tens = int(str_number[0])
        tens_word = twenties_and_others[find_tens]

        find_ones = int(str_number[1])
        ones_word = ones[find_ones]

        return f'{tens_word} و {ones_word}'
   
    elif number > 99 and number <= 999:

        if str_number[1] == '0' and str_number[2] != '0':
            find_ones = int(str_number[2])
            ones_word = ones[find_ones]
            find_hundreds = int(str_number[0])
            hundreds_word = hundreds[find_hundreds]

            return f'{hundreds_word} و {ones_word}'
        
        elif str_number[1] == '0' and str_number[2] == '0':
            find_hundreds = int(str_number[0])
            hundreds_word = hundreds[find_hundreds]

            return f'{hundreds_word}'
        
        elif str_number[1] == '1':
            find_number = int(str_number[1:])
            find_word = ten_to_nineteen[find_number]

            find_hundreds = int(str_number[0])
            hundreds_word = hundreds[find_hundreds]

            return f'{hundreds_word} و {find_word}'
        
        elif str_number[1] != '0' and str_number[2] == '0':
            find_tens = int(str_number[1])
            tens_word = twenties_and_others[find_tens]

            find_hundreds = int(str_number[0])
            hundreds_word = hundreds[find_hundreds]

            return f'{hundreds_word} و {tens_word}'
        
        else:
            find_hundreds = int(str_number[0])
            find_tens = int(str_number[1])
            find_ones = int(str_number[2])

            hundreds_word = hundreds[find_hundreds]
            tens_word = twenties_and_others[find_tens]
            ones_word = ones[find_ones]

            return f'{hundreds_word} و {tens_word} و {ones_word}'
        

    elif number > 999 and number <= 9999:

        last_two_digits = int(str_number[2:])
        if small_module.small_function.is_less_than_twenty(last_two_digits):
            tens_word = ten_to_nineteen[last_two_digits]

            find_thousands = int(str_number[0])
            find_hundreds = int(str_number[1])

            thousands_word = thousands[find_thousands]
            hundreds_word = hundreds[find_hundreds]

            return f'{thousands_word} و {hundreds_word} {tens_word}' 


        find_thousands = int(str_number[0])
        find_hundreds = int(str_number[1])
        find_tens = int(str_number[2])
        find_ones = int(str_number[3])

        thousands_word = thousands[find_thousands]
        hundreds_word = hundreds[find_hundreds]
        tens_word = twenties_and_others[find_tens]
        ones_word = ones[find_ones]

        return f'{thousands_word} و {hundreds_word} {tens_word} {ones_word}' 


    elif number > 9999 and number <= 99999:

        first_two_digits = int(str_number[0:2])
        last_two_digits = int(str_number[3:])


        if small_module.package.small_function.is_less_than_twenty(first_two_digits) and small_module.package.small_function.is_less_than_twenty(last_two_digits):
            thousands_word = ten_to_nineteen[first_two_digits]

            find_hundreds = int(str_number[2])
            hundreds_word = hundreds[find_hundreds]

            tens_word = ten_to_nineteen[last_two_digits]

            return f'{thousands_word} هزار {hundreds_word} و {tens_word}'
    

        elif small_module.package.small_function.is_less_than_twenty(first_two_digits) and not small_module.package.small_function.is_less_than_twenty(last_two_digits):

            thousands_word = ten_to_nineteen[first_two_digits]

            find_hundreds = int(str_number[2])
            hundreds_word = hundreds[find_hundreds]

            find_tens = int(str_number[3])
            tens_word = twenties_and_others[find_tens]

            find_ones = int(str_number[4])
            ones_word = ones[find_ones]

            return f'{thousands_word} هزار {hundreds_word} {tens_word} {ones_word}' 


        elif not small_module.package.small_function.is_less_than_twenty(first_two_digits) and small_module.package.small_function.is_less_than_twenty(last_two_digits):

            find_ten_thousands = int(str_number[0])
            ten_thousands_word = twenties_and_others[find_ten_thousands]

            find_thousands = int(str_number[1])
            thousands_word = ones[find_thousands]

            find_hundreds = int(str_number[2])
            hundreds_word = hundreds[find_hundreds]

            tens_word = ten_to_nineteen[last_two_digits]

            return f'{ten_thousands_word} و {thousands_word} هزار و {hundreds_word} {tens_word}'               
    

        else:

            find_ten_thousands = int(str_number[0])
            ten_thousands_word = twenties_and_others[find_ten_thousands]

            find_thousands = int(str_number[1])
            thousands_word = ones[find_thousands]

            find_hundreds = int(str_number[2])
            hundreds_word = hundreds[find_hundreds]

            find_tens = int(str_number[3])
            tens_word = twenties_and_others[find_tens]

            find_ones = int(str_number[4])
            ones_word = ones[find_ones]

            return f'{ten_thousands_word} {thousands_word} هزار و {hundreds_word} {tens_word} {ones_word}'
        

    elif number > 99999 and number <= 9999999:

        first_two_digits = int(str_number[1:3])
        last_two_digits = int(str_number[4:])


        if small_module.package.small_function.is_less_than_twenty(first_two_digits) and small_module.package.small_function.s_less_than_twenty(last_two_digits):
            find_hundred_thousands = int(str_number[0])
            hundred_thousands_word = hundreds[find_hundred_thousands]
            thousands_word = ten_to_nineteen[first_two_digits]

            find_hundreds = int(str_number[3])
            hundreds_word = hundreds[find_hundreds]

            tens_word = ten_to_nineteen[last_two_digits]

            return f'{hundred_thousands_word} و {thousands_word} هزار {hundreds_word} و {tens_word}'
    

        elif small_module.package.small_function.is_less_than_twenty(first_two_digits) and not small_module.package.small_function.is_less_than_twenty(last_two_digits):

            find_hundred_thousands = int(str_number[0])
            hundred_thousands_word = hundreds[find_hundred_thousands]
            thousands_word = ten_to_nineteen[first_two_digits]


            find_hundreds = int(str_number[3])
            hundreds_word = hundreds[find_hundreds]

            find_tens = int(str_number[4])
            tens_word = twenties_and_others[find_tens]

            find_ones = int(str_number[5])
            ones_word = ones[find_ones]


            return f' {hundred_thousands_word} {thousands_word} هزار {hundreds_word} {tens_word} {ones_word}' 


        elif not small_module.package.small_function.is_less_than_twenty(first_two_digits) and small_module.package.small_function.is_less_than_twenty(last_two_digits):

            find_hundred_thousands = int(str_number[0])
            hundred_thousands_word = hundreds[find_hundred_thousands]

            find_ten_thousands = int(str_number[1])
            ten_thousands_word = ten_to_nineteen[find_ten_thousands]
            print(ten_thousands_word)

            find_thousands = int(str_number[2])
            thousands_word = ones[find_thousands]

            find_hundreds = int(str_number[3])
            hundreds_word = hundreds[find_hundreds]

            tens_word = ten_to_nineteen[last_two_digits]

            return f'{ten_thousands_word} و {thousands_word} هزار و {hundreds_word} {tens_word}'               
    

        else:
            find_hundred_thousands = int(str_number[0])
            hundred_thousands_word = hundreds[find_hundred_thousands]

            find_ten_thousands = int(str_number[1])
            ten_thousands_word = twenties_and_others[find_ten_thousands]

            find_thousands = int(str_number[2])
            thousands_word = ones[find_thousands]

            find_hundreds = int(str_number[3])
            hundreds_word = hundreds[find_hundreds]

            find_tens = int(str_number[4])
            tens_word = twenties_and_others[find_tens]

            find_ones = int(str_number[5])
            ones_word = ones[find_ones]

            return f'{hundred_thousands_word} {ten_thousands_word} {thousands_word} هزار و {hundreds_word} {tens_word} {ones_word}'
        

    else:
        return 'This Program Support Numbers Between 1-999999'


if __name__ == "__main__":


    # Uncomment if you want to print 0-999999 in Persian(Words)

    # for i in range(1,1000000):
    #     print(num_to_word(i))


    print(num_to_word(0))
    print(num_to_word(1))
    print(num_to_word(19))
    print(num_to_word(23))
    print(num_to_word(22))
    print(num_to_word(31))
    print(num_to_word(40))
    print(num_to_word(49))
    print(num_to_word(56))
    print(num_to_word(63))
    print(num_to_word(70))
    print(num_to_word(81))
    print(num_to_word(99))
    print(num_to_word(100))
    print(num_to_word(106))
    print(num_to_word(209))
    print(num_to_word(917))
    print(num_to_word(212))
    print(num_to_word(415))
    print(num_to_word(619))
    print(num_to_word(720))
    print(num_to_word(913))
    print(num_to_word(633))
    print(num_to_word(645))
    print(num_to_word(735))
    print(num_to_word(891))
    print(num_to_word(999))
    print(num_to_word(9999))
    print(num_to_word(8972))
    print(num_to_word(19010))
    print(num_to_word(11275))
    print(num_to_word(12275))
    print(num_to_word(10275))
    print(num_to_word(14275))
    print(num_to_word(15421))
    print(num_to_word(16270))
    print(num_to_word(17225))
    print(num_to_word(18215))
    print(num_to_word(19275))
    print(num_to_word(21111))
    print(num_to_word(99001))
    print(num_to_word(22222))
    print(num_to_word(50003))
    print(num_to_word(69810))
    print(num_to_word(70301))
    print(num_to_word(98741))
    print(num_to_word(891299))
    print(num_to_word(191200))
    print(num_to_word(291299))
    print(num_to_word(191299))