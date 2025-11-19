/**
 * API Configuration
 * Centralized API URL management to prevent double-slash issues
 */

// Get backend URL and ensure no trailing slash
const getBackendURL = () => {
  const url = process.env.REACT_APP_BACKEND_URL || '';
  return url.replace(/\/+$/, ''); // Remove all trailing slashes
};

// Export the clean backend URL
export const BACKEND_URL = getBackendURL();

// Export the API base URL (backend URL + /api)
export const API_BASE_URL = `${BACKEND_URL}/api`;

// Export default
export default {
  BACKEND_URL,
  API_BASE_URL,
};
