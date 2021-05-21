<template>

  <div class="columns">

    <div class="column is-half">
      
      <!-- add todo -->
      <div class="field">
        <label class="label">Add Task</label>

        <div class="control">
          <input 
            class="input"
            type="text"
            placeholder="Search here and there"
            v-model="task">
        </div>
      </div>

      <div class="field is-grouped">
        <div class="control">
          <button
            class="button is-link"
            value="Add" 
            @click="addTodo({ task: task })">Add</button>
        </div>
      </div>
    </div>
    <!-- end add todo -->

    <!-- todos -->
    <div class="column is-half">

      <p class="pb-1">
        <strong>Current Tasks</strong>
      </p>
      
      <p v-if="todos.length === 0">None, yet!</p>
      <ul class="todo" v-for="(todo, index) in todos" :key="index">
          <li v-html="todo.task"></li>
      </ul>
    </div>
    <!-- end todos -->

  </div>

</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "Todos",
  data() {
    return {
      task: "",
    };
  },
  computed: mapState({
    todos: (state) => state.todos.todos,
  }),
  methods: mapActions("todos", ["addTodo", "deleteTodo"]),
  created() {
    this.$store.dispatch("todos/getTodos");
  },
};
</script>
