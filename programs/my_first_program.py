from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform the addition of my_int1 and my_int2
    sum_int = my_int1 + my_int2

    # Return the result of the addition
    return [Output(sum_int, "my_output", party1)]
