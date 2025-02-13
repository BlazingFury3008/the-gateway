import axios from "axios";

// Use the correct environment variable
const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL;

const api = axios.create({
  baseURL: BACKEND_URL,
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true, // Enable cookies/session handling if needed
});

export default api;
