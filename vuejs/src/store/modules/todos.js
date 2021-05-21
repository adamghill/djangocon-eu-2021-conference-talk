import todoService from "../../services/todoService";

const state = {
  todos: [],
};

const getters = {
  todos: (state) => {
    return state.todos;
  },
};

const actions = {
  getTodos({ commit }) {
    todoService.fetchTodos().then((todos) => {
      commit("setTodos", todos);
    });
  },
  addTodo({ commit }, todo) {
    todoService.postTodo(todo).then(() => {
      commit("addTodo", todo);
    });
  },
};

const mutations = {
  setTodos(state, todos) {
    state.todos = todos;
  },
  addTodo(state, todo) {
    state.todos.push(todo);
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
