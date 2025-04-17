
import { buildGetRequest, buildPostRequest, buildDeleteRequest, buildPutRequest } from "./requests.factory";

export function postregister(baseUrl: string, name: string, password: string, height: number, age: number, gender: string, weightGoal: number, DailyCalorie: number) {
    return fetch(baseUrl + "/users/register", buildPostRequest({name: name, password: password, height: height, age: age, gender: gender, WeightGoal: weightGoal, DailyCalorie: DailyCalorie}));
  }
  
