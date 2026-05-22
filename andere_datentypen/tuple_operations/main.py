# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]


#1 Umwandlung von shelf1_update in shelf1_update_tuple
shelf1_update_tuple = tuple(shelf1_update)

#2 Verkettung von shelf1_update_tuple und shelf1 mit der Bezeichnung shelf1_concat
shelf1_concat = shelf1 + shelf1_update_tuple

#3 Vorkommen von "celery" in shelf1_concat in celery_count speichern
celery_count = shelf1_concat.count("celery")

#4 Index des ersten Vorkommens von "celery" in celery_index speichern
celery_index = shelf1_concat.index("celery")

print(f"Updated Shelf #1: {shelf1_concat}")
print(f"Number of Celery: {celery_count}")
print(f"Celery Index:     {celery_index}")