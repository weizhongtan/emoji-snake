import random, emojis

food_emojis = [
    em.emoji
    for em in list(emojis.db.get_emojis_by_category('Food & Drink'))
    if em.unicode_version and float(em.unicode_version) <= 9.0
]

class Food:
    def __init__(self, limit_x, limit_y):
        self._limit_x = limit_x
        self._limit_y = limit_y

    def position(self):
        return self._x, self._y

    def spawn(self):
        self.token = random.choice(food_emojis)
        self._x = random.randint(0, self._limit_x - 1)
        self._y = random.randint(0, self._limit_y - 1)

