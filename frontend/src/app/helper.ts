const base = process.env.NEXT_PUBLIC_FLASK_API_BASE ?? "";

export async function fetchData<T>(url: string): Promise<T> {
  const headers: HeadersInit = {
    "Content-Type": "application/json",
    "X-API-Key": process.env.NEXT_PUBLIC_DATA_API_KEY ?? "",
  };

  const response = await fetch(`${base}/data/${url}`, {
    method: "GET",
    headers,
  });

  if (!response.ok) {
    throw new Error(`Failed to fetch ${url}: ${response.status} ${response.statusText}`);
  }

  return response.json() as Promise<T>;
}
