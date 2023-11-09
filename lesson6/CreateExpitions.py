class BuildingError(Exception):
    def __str__(self):
        return f"Занадто мало матеріалів для того щоб побудувати будинок"
def check_material(amount_of_material,limit_value):
    if amount_of_material > limit_value:
        return ("матеріалів достатньо")
    else:
        raise BuildingError(amount_of_material)
matterial = 100
print(check_material(matterial, limit_value=300))