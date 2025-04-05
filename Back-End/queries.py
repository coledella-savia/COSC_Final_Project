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