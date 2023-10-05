const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const taskManager = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (taskManager[task.userId]) {
        if (task.completed) {
          taskManager[task.userId] += 1;
        }
      } else {
        taskManager[task.userId] = 0;

        if (task.completed) {
          taskManager[task.userId] += 1;
        }
      }
    }

    console.log(taskManager);
  } else {
    console.log(err);
  }
});
