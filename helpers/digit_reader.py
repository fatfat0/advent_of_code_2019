from digit import Digit, Code1, Code2, Code99, Code404


def convert_digits_to_class_list(data_list):
    return [_convert_digit(digit, index) for index, digit in enumerate(data_list)]


def _convert_digit(digit, index):
    try:
        return globals()[f"Code{digit}"](digit, index)
    except:
        # TODO write down the error
        return Code404(digit, index)
