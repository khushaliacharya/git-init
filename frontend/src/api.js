import axios from 'axios';
const api = axios.create({ baseURL: 'http://localhost:5000/api/tasks' });
export const fetchTasks = () => api.get('/');
export const createTask = (title) => api.post('/', { title });
export const updateTask = (id, data) => api.patch(`/${id}`, data);
export const logSession = (id, minutes) => api.post(`/${id}/sessions`, { duration_minutes: minutes });
