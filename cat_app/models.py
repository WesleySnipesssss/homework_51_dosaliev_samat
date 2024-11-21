from django.db import models

# Create your models here.

class Cat(models.Model):
    MAX_LEVEL = 100
    MIN_LEVEL = 0

    name = models.CharField(max_length=100, default="Kitty")
    age = models.PositiveIntegerField(default=1)
    satiety = models.PositiveIntegerField(default=40)
    happiness = models.PositiveIntegerField(default=40)
    sleeping = models.BooleanField(default=False)
    mood = models.CharField(max_length=50, default="neutral")

    HAPPY_IMAGES = {
        "sad": "/static/images/sad_cat.jpeg",
        "neutral": "/static/images/neutral_cat.jpeg",
        "happy": "/static/images/happy_cat.jpeg",
    }

    def feed(self):
        if self.sleeping:
            return
        self.satiety = min(self.MAX_LEVEL, self.satiety + 15)
        self.happiness = min(self.MAX_LEVEL, self.happiness + 5)
        if self.satiety > self.MAX_LEVEL:
            self.happiness = max(self.MIN_LEVEL, self.happiness - 30)

    def play(self):
        if self.sleeping:
            self.sleeping = False
            self.happiness = max(self.MIN_LEVEL, self.happiness - 5)
        else:
            import random
            if random.randint(1, 3) == 1:
                self.happiness = self.MIN_LEVEL
            else:
                self.happiness = min(self.MAX_LEVEL, self.happiness + 15)
            self.satiety = max(self.MIN_LEVEL, self.satiety - 10)

    def sleep(self):
        self.sleeping = True

    def get_image(self):
        return self.HAPPY_IMAGES.get(self.mood, "/static/images/neutral_cat.jpeg")