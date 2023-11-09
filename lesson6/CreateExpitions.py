class BuildingError(Exception):
    def __str__(self):
        return f"Занадто мало матеріалів для того щоб побудувати будинок"