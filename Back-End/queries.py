###
#
# Meal Queries
#
##

post_meal = """
INSERT INTO Meals
(userId, mealName, calories, description, mealDate)
VALUES(?, ?, ?, ?, ?);
"""

get_meal_by_id = """
SELECT id, userId, mealName, calories, description, mealDate
FROM Meals WHERE id = ?;
"""

# User Queries

register_user = """
INSERT INTO Users
(name, password, height, age, gender, WeightGoal, DailyCalorie)
VALUES(?, ?, ?, ?, ?, ?, ?);
"""

get_user_by_name = """
SELECT id, password FROM Users WHERE name = ?;
"""

