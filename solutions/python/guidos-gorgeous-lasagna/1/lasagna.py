EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers: int) -> int:
    """
    Calculate the total preparation time in minutes.
    Each layer of lasagna takes 2 minutes to prepare.
    
    :param number_of_layers: int - Number of layers to prepare.
    :return: int - Total preparation time in minutes.
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    Calculate the total elapsed time in minutes.

    This includes the preparation time for the layers and the time the lasagna
    has already spent baking.

    :param number_of_layers: int - Number of layers prepared.
    :param elapsed_bake_time: int - Time in minutes the lasagna has been baking.
    :return: int - Total elapsed time in minutes.
    """
    return  (EXPECTED_BAKE_TIME + preparation_time_in_minutes(number_of_layers)) - bake_time_remaining(elapsed_bake_time)

print(elapsed_time_in_minutes(10, 40))