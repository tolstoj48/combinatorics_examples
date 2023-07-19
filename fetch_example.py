# přidat možnost vybrat si kategorii úkolu nebo nahodile
# přidat úlohy z http://kombinatorika.rubesz.cz/

import random
import sys
import data


class Example:
    def __init__(self, start=0, end=len(data.examples) - 1):
        self.start = start
        self.end = end
        self.category_number = random.randint(self.start, self.end)
        self.number = random.randint(
            0, len(data.examples[self.category_number]) - 1)
        if self.category_number == 0:
            self.category = "Variace bez opakování"
        elif self.category_number == 1:
            self.category = "Permutace bez opakování"
        elif self.category_number == 2:
            self.category = "Kombinace bez opakování"
        elif self.category_number == 3:
            self.category = "Variace s opakováním"
        elif self.category_number == 4:
            self.category = "Permutace s opakováním"
        elif self.category_number == 5:
            self.category = "Kombinace s opakováním"

    def fetch_example(self):
        print("---------------------------------")
        print(data.examples[self.category_number][self.number][0])
        print("---------------------------------")
        vysledek = "N"
        while vysledek.lower() != "a":
            vysledek = input(
                "Chcete vidět výsledek, případně s řešením? \"A\\a\" pro ano, \"N\\n\" pro ne.")
        print("---------------------------------")
        print(
            f"Výsledek je roven: {data.examples[self.category_number][self.number][1]}")
        print("*****")
        print(f"A jde o: {self.category}")
        print("*****")
        print(f"Šlo o příklad číslo: {self.number} a zdroj je: {data.sources[data.examples[self.category_number][self.number][2]]}")
        print("---------------------------------")
        return


if __name__ == "__main__":
    try:
        if(sys.argv[2] == "no-repeat"):
            example = Example(start = 0, end = 2)
        elif(sys.argv[2] == "repeat"):
            example = Example(start = 3, end = 5)
        example.fetch_example()
    except:
        example = Example()
        example.fetch_example()
