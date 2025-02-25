import axios from "axios";

// Use the correct environment variable
const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL;
const API_KEY = process.env.NEXT_PUBLIC_API_KEY

const api = axios.create({
  baseURL: BACKEND_URL,
  headers: {
    "Content-Type": "application/json",
    "X-API-KEY":API_KEY,
  },
  withCredentials: true, // Enable cookies/session handling if needed
});

export default api;
