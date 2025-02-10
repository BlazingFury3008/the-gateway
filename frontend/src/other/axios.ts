import axios from "axios";

// ✅ Set your backend URL here
const BACKEND_URL = "http://localhost:8000";  // Change for production

const api = axios.create({
  baseURL: BACKEND_URL,
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true, // Enable cookies/session handling if needed
});

export default api;
