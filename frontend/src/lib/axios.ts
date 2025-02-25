import axios from "axios";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL
const API_KEY = process.env.NEXT_PUBLIC_API_KEY

// Create Axios instance
const api = axios.create({
  baseURL: BACKEND_URL,
  headers: {
    "Content-Type": "application/json",
    "X-API-KEY":API_KEY,

  },
  withCredentials: true, // Ensures cookies/session handling
});

// Attach authentication token automatically to requests
api.interceptors.request.use(
  (config) => {
    if (typeof window !== "undefined") {
      try {
        const token = localStorage.getItem("access_token")?.replace(/^"(.*)"$/, "$1"); // Remove quotes
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
      } catch (error) {
        console.error("Error retrieving token:", error);
      }
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
