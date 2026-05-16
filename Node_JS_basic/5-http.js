const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url === '/students') {
    try {
      const studentsOutput = await countStudents(database);
      res.end(`This is the list of our students\n${studentsOutput}`);
    } catch (_) {
      res.end('This is the list of our students\nCannot load the database');
    }
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;
