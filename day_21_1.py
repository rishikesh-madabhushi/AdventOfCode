import re
import pprint

f = open("day_21.txt")
#f = open("test.txt")

line_re = re.compile("(.*)\(contains (.*)\)")

allergen_sets = {}

all_dishes = [l.rstrip() for l in f.readlines()]

for l in all_dishes:
    match = line_re.fullmatch(l)
    ingredients = match.group(1).strip().split()
    allergens = [l.strip() for l in match.group(2).strip().split(',')]

    for allergen in allergens:
        if allergen in allergen_sets:
            allergen_sets[allergen] = allergen_sets[allergen].intersection(ingredients)
        else:
            allergen_sets[allergen] = set(ingredients)


pprint.pprint(allergen_sets)
eliminated = set()
changed = True
while changed:
    changed = False
    for key in allergen_sets:
        if len(allergen_sets[key]) == 1:
            ingredient = next(iter(allergen_sets[key]))
            if ingredient not in eliminated:
                eliminated.add(ingredient)
                changed = True
        else: 
            new_set = allergen_sets[key] - eliminated
            if new_set != allergen_sets[key]:
                allergen_sets[key] = new_set
                changed = True

pprint.pprint(allergen_sets)
count = 0
for l in all_dishes:
    match = line_re.fullmatch(l)
    ingredients = match.group(1).strip().split()
    for ingredient in ingredients:
        if ingredient not in eliminated:
            count += 1

print(count)

print(",".join([allergen_sets[l].pop() for l in sorted(allergen_sets.keys())]))

