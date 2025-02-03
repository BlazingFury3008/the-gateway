import axios from "axios";

// Backend URL (Modify for production)
const BACKEND_URL = "http://localhost:8000";

// Create Axios instance
const api = axios.create({
  baseURL: BACKEND_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Automatically attach authentication token to requests (if available)
api.interceptors.request.use((config) => {
  if (typeof window !== "undefined") {
    const token = localStorage.getItem("access_token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
  }
  return config;
});

export default api;
