import fs from 'fs';

export default function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = {};

      for (const line of lines.slice(1)) {
        const fields = line.split(',');
        if (fields.length >= 4) {
          const [firstname, , , field] = fields;
          if (!students[field]) students[field] = [];
          students[field].push(firstname);
        }
      }

      resolve(students);
    });
  });
}
