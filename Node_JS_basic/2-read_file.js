const fs = require('fs');

module.exports = function countStudents(filePath) {
  try {
    const data = fs.readFileSync(filePath, 'utf-8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = {};
    lines.slice(1).forEach((line) => {
      const [firstName, , , field] = line.split(',');
      if (!students[field]) {
        students[field] = [];
      }
      students[field].push(firstName);
    });
    console.log(`Number of students: ${lines.length - 1}`);
    Object.keys(students).forEach((field) => {
      console.log(`Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`);
    });
  } catch (_) {
    throw new Error('Cannot load the database');
  }
};
