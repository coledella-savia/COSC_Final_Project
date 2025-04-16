export function buildPostRequest(body: any): RequestInit {
    return {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
      mode: "cors",
      credentials: "include",
    };
  }
  
  export function buildPutRequest(body: any): RequestInit {
    return {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
      mode: "cors",
      credentials: "include",
    };
  }
  
  export function buildGetRequest(): RequestInit {
    return {
      method: "GET",
      headers: { "Content-Type": "application/json" },
      mode: "cors",
      credentials: "include",
    };
  }
  
  export function buildDeleteRequest(body: any): RequestInit {
    return {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
      mode: "cors",
      credentials: "include",
    };
  }