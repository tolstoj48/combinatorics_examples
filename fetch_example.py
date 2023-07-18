# přidat možnost vybrat si kategorii úkolu nebo nahodile
# přidat úlohy z http://kombinatorika.rubesz.cz/

import random
import data


class Example:
    def __init__(self):
        # TODO: upravit na slovníky - slovníky z důvodu ozdrojování
        self.category_number = random.randint(0, len(data.examples) - 1)
        self.number = random.randint(
            1, len(data.examples[self.category_number]) - 1)
        if self.category_number == 0:
            self.category = "Variace bez opakování"
        elif self.category_number == 1:
            self.category = "Permutace bez opakování"
        elif self.category_number == 2:
            self.category = "Kombinace bez opakování"

    def fetch_example(self):
        print("---------------------------------")
        print(data.examples[self.category_number][self.number][0])
        print("---------------------------------")
        vysledek = "N"
        while vysledek.lower() != "a":
            vysledek = input(
                "Chcete vidět výsledek, případně s řešením? A pro ano, N pro ne.")
        print("---------------------------------")
        print(
            f"Výsledek je roven: {data.examples[self.category_number][self.number][1]}")
        print("*****")
        print(f"A jde o: {self.category}")
        print("*****")
        print(f"Šlo o příklad číslo: {self.number} a zdroj je: {data.examples[self.category_number][0]}")
        print("---------------------------------")
        return


if __name__ == "__main__":
    example = Example()
    example.fetch_example()
