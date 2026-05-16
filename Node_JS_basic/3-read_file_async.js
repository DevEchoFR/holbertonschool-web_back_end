const fs = require('fs');

module.exports = async function countStudents(filePath) {
  try {
    const data = await fs.promises.readFile(filePath, 'utf-8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = {};
    lines.slice(1).forEach((line) => {
      const [firstName, , , field] = line.split(',');
      if (!students[field]) {
        students[field] = [];
      }
      students[field].push(firstName);
    });
    const outputLines = [`Number of students: ${lines.length - 1}`];
    Object.keys(students).forEach((field) => {
      outputLines.push(`Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`);
    });
    outputLines.forEach((line) => console.log(line));
    return outputLines.join('\n');
  } catch (_) {
    throw new Error('Cannot load the database');
  }
};
