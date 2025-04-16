
import { buildGetRequest, buildPostRequest, buildDeleteRequest, buildPutRequest } from "./requests.factory";

export function postMeal(baseUrl: string, userId: number, mealName: string, calories: number, description: string, mealDate: string) {
    return fetch(baseUrl + "/meals", buildPostRequest({userId: userId, mealName: mealName, calories: calories, description: description, mealDate: mealDate}));
  }
  
  export function deleteMeal(baseUrl: string, userId: number, mealId: number) {
    return fetch(baseUrl + `/meals/${mealId}`, buildDeleteRequest(userId));
  }