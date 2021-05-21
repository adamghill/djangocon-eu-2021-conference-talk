import api from "@/services/api";

export default {
  fetchTodos() {
    return api.get(`todos/`).then((response) => response.data);
  },
  postTodo(payload) {
    return api.post(`todos/`, payload).then((response) => response.data);
  },
};
