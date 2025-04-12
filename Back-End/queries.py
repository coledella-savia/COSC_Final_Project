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

get_user_by_name = "SELECT name FROM users WHERE name = ?"
get_user_credentials = "SELECT salt, password FROM users WHERE name = ?"
create_user = "INSERT INTO users (name, salt, password, WeightGoal, DailyCalorie) VALUES (?, ?, ?, ?, ?)"
