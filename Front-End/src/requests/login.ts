import { buildPostRequest } from "./requests.factory";

export function buildLoginRequest(
  _name: string,
  _password: string
): RequestInit {
  return buildPostRequest({ name: _name, password: _password });
}

export function buildLogoutRequest(): RequestInit {
  return buildPostRequest("");
}