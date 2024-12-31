const taskInput = document.getElementById("taskInput");
const addTaskButton = document.getElementById("addTaskButton");
const taskList = document.getElementById("taskList");

addTaskButton.addEventListener("click", addTask);

function addTask() {
  const taskText = taskInput.value.trim();
  if (taskText) {
      const taskItem = document.createElement("li");
      taskItem.textContent = taskText;

      const deleteButton = document.createElement("button");
      deleteButton.textContent = "Delete";
      deleteButton.addEventListener("click", () => taskItem.remove());

      taskItem.appendChild(deleteButton);
      taskList.appendChild(taskItem);

      taskInput.value = "";
  }
}

const tasks = [];

function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText) {
        tasks.push(taskText);
        renderTasks();
        taskInput.value = "";
    }
}

function renderTasks() {
    taskList.innerHTML = "";
    tasks.forEach((task) => {
        const taskItem = document.createElement("li");
        taskItem.textContent = task;

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.addEventListener("click", () => {
            const index = tasks.indexOf(task);
            tasks.splice(index, 1);
            renderTasks();
        });

        taskItem.appendChild(deleteButton);
        taskList.appendChild(taskItem);
    });
}


taskItem.addEventListener("click", () => {
  taskItem.classList.toggle("completed");
});


function saveTasks() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
  const savedTasks = JSON.parse(localStorage.getItem("tasks"));
  if (savedTasks) {
      tasks.push(...savedTasks);
      renderTasks();
  }
}

window.addEventListener("load", loadTasks);