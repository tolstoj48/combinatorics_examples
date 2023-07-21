# přidat úlohy z http://kombinatorika.rubesz.cz/, sbírky úloh
#


import random
import sys
import data


class Example:
    def __init__(self, type_of_example="vse", repeat="vse"):
        self.type_of_example = type_of_example
        self.repeat = repeat
        # choosing random type_of_example
        if type_of_example == "vse":
            category = random.randint(0, 2)
            dicty = {
                "0": "perm", "1": "vari", "2": "kombi"
            }
            self.type_of_example = dicty[str(category)]
        else:
            self.type_of_example = type_of_example
        # choosing random with or without repetition
        if self.repeat == "vse":
            category = random.randint(0, 1)
            dicty = {
                "0": "bez-opak", "1": "s-opak"
            }
            self.repeat = dicty[str(category)]
        else:
            self.repeat = repeat
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


if __name__ == "__main__":
    try:
        if (len(sys.argv)) != 3 or sys.argv[1] not in ("perm", "vari", "kombi", "vse") or sys.argv[2] not in ("bez-opak", "s-opak", "vse"):
            raise ValueError(
                "Nespustil/a jste aplikaci řádným způsobem s dvěmi argumenty - první: perm (pro permutace), vari (pro variace), komb (pro kombinace), druhý: bez-opak (bez opakování), s-opak (s opakováním), vse (náhodně s nebo bez opakování). Nebo jste nespustil/a s přesně dvěmi argumenty - 'python fetch_example.py [perm, vari, komb] [s-opak/bez-opak/vse]  -> například: 'python fetch_example.py perm vse. Zde je náhodně vybraný příklad.")
        example = Example(sys.argv[1], sys.argv[2])
        example.fetch_example()
    except ValueError as e:
        print(e)
        example = Example()
        example.fetch_example()
