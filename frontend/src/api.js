const API_URL = 'http://localhost:5000/api';

export async function fetchData() {
  const response = await fetch(`${API_URL}/data`);
  return response.json();
}