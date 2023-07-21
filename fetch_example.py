# TODO: add more examples
# TODO: write tests

"""Combinatorics example fetcher

This script allows to fetch different examples for exercising of combinatorics, mainly at the level of a grammar/high school. An user can choose type of exercise (permutations, variations, combinations),
and can fetch with or without repetion (f.e. combination with repetition). The result is printed in the console after the user solves and wants it. The user can also fetch random examples - 
i. e. examples completely random or random on type and repetition/without repetition base on her own choice. 
"""

import random
import sys
import data


class Example:
    """
    A class used to represent an example

    ...

    Attributes
    ----------
    type_of_example : str
        a type of the fetched example - it is permutations/variations/combinations or all types (default "vse")
    repeat : str
        a type of the fetched example concerning repetition - is it with or without repetition (default "vse")
    number : int
        a random number to choose from data (tuple) - min 0, max length of the tuple of the given type and repetition type
    category : str
        a category of the choosen example - the combination of 1. permutation/variation/combination and 2. no-repeat/repeat

    Methods
    -------
    fetch_example()
        prints the chosen example and its solution to the console
    """

    def __init__(self, type_of_example="vse", repeat="vse"):
        """
        Parameters
        ----------
        type_of_example : str
            a type of the fetched example - it is permutations/variations/combinations or all types (default "vse")
        repeat : str
            a type of the fetched example concerning repetition - is it with or without repetition (default "vse")
        number : int
            a random number to choose from data (tuple) - min 0, max length of the tuple of the given type and repetition type
        category : str
            a category of the choosen example - the combination of 1. permutation/variation/combination and 2. no-repeat/repeat
        """

        self.type_of_example = type_of_example
        self.repeat = repeat
        # choosing random type_of_example, if user wants all the combinatorics types
        if type_of_example == "vse":
            __category = random.randint(0, 2)
            __dicty_type = {
                "0": "perm", "1": "vari", "2": "kombi"
            }
            self.type_of_example = __dicty_type[str(__category)]
        # if not, let user decide
        else:
            self.type_of_example = type_of_example
        # choosing random with or without repetition, if user wants with and without repetition examples
        if self.repeat == "vse":
            __category = random.randint(0, 1)
            __dicty_repetition_type = {
                "0": "bez-opak", "1": "s-opak"
            }
            self.repeat = __dicty_repetition_type[str(__category)]
        # if not random example on repeat, let user decide
        else:
            self.repeat = repeat
        # we want to get a "random" example from data.py
        self.number = random.randint(
            0, len(data.examples[self.type_of_example][self.repeat]) - 1)

        # helper category dictionary to get correct category after initiation
        __category_conversion_dict = {
            "perm": {
                "bez-opak": "Permutace bez opakování",
                "s-opak": "Permutace s opakováním",
            },
            "vari": {
                "bez-opak": "Variace bez opakování",
                "s-opak": "Variace s opakováním",
            },
            "kombi": {
                "bez-opak": "Kombinace bez opakování",
                "s-opak": "Kombinace s opakováním",
            }
        }
        # choosing category with category dictionary instead of if-elif statements
        self.category = __category_conversion_dict[self.type_of_example][self.repeat]

    def fetch_example(self):
        """Prints the example and then even its result.

        Parameters
        ----------
        None
        """

        print("---------------------------------")
        print(data.examples[self.type_of_example][self.repeat][self.number][0])
        print("---------------------------------")
        vysledek = "N"
        while vysledek.lower() != "a":
            vysledek = input(
                "Chcete vidět výsledek, případně s řešením? \"A\\a\" pro ano, \"N\\n\" pro ne.")
        print("---------------------------------")
        print(
            f"Výsledek je roven: {data.examples[self.type_of_example][self.repeat][self.number][1]}")
        print("*****")
        print(f"A jde o: {self.category}")
        print("*****")
        print(
            f"Šlo o příklad číslo: {self.number} a zdroj je: {data.sources[data.examples[self.type_of_example][self.repeat][self.number][2]]}")
        print("---------------------------------")
        return

def main():
    try:
        # if user does not send two arguments with his choice it is supposed to be fail or hacking :-) attempt --> let´s run some random example
        if (len(sys.argv)) != 3 or sys.argv[1] not in ("perm", "vari", "kombi", "vse") or sys.argv[2] not in ("bez-opak", "s-opak", "vse"):
            raise ValueError(
                "Nespustil/a jste aplikaci řádným způsobem s dvěmi argumenty - první: perm (pro permutace), vari (pro variace), komb (pro kombinace), druhý: bez-opak (bez opakování), s-opak (s opakováním), vse (náhodně s nebo bez opakování). Nebo jste nespustil/a s přesně dvěmi argumenty - 'python fetch_example.py [perm, vari, komb] [s-opak/bez-opak/vse]  -> například: 'python fetch_example.py perm vse. Zde je náhodně vybraný příklad.")
        example = Example(sys.argv[1], sys.argv[2])
        example.fetch_example()
    except ValueError as e:
        print(e)
        example = Example()
        example.fetch_example()


if __name__ == "__main__":
    main()
