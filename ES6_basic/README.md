# ES6 Basics

## Description

This project covers the fundamentals of ES6 (ECMAScript 2015) JavaScript features. Each task focuses on a specific modern syntax or feature introduced in ES6.

## Requirements

- Node.js 20.x
- npm
- All files use the `.js` extension
- Code will be tested using **Jest** and analyzed with **ESLint**

## Setup

```bash
npm install
```

## Tasks

### 0. Const or let?
**File:** `0-constants.js`

Use `const` for variables that won't be reassigned, and `let` for variables that will.

```bash
node 0-main.js
```

---

### 1. Block Scope
**File:** `1-block-scoped.js`

Modify variables to use block scoping with `let` so they are not overwritten inside a conditional block.

```bash
node 1-main.js
```

---

### 2. Arrow Functions
**File:** `2-arrow.js`

Rewrite a standard function to use ES6 arrow function syntax, preserving the correct `this` context.

```bash
node 2-main.js
```

---

### 3. Default Parameters
**File:** `3-default-parameter.js`

Condense a function to one line using default parameter values.

```bash
node 3-main.js
```

---

### 4. Rest Parameter Syntax
**File:** `4-rest-parameter.js`

Use the rest parameter (`...args`) to return the number of arguments passed to a function.

```bash
node 4-main.js
```

---

### 5. Spread Operator
**File:** `5-spread-operator.js`

Use the spread operator to concatenate two arrays and spread each character of a string into a single array.

```bash
node 5-main.js
```

---

### 6. Template Literals
**File:** `6-string-interpolation.js`

Use template literals (backtick strings) to build a dynamic description string.

```bash
node 6-main.js
```

---

### 7. Object Property Shorthand
**File:** `7-getBudgetObject.js`

Use ES6 object property value shorthand to simplify object creation when variable names match key names.

```bash
node 7-main.js
```

---

### 8. Computed Property Names
**File:** `8-getBudgetCurrentYear.js`

Use computed property names (dynamic keys) to create an object whose keys include the current year.

```bash
node 8-main.js
```

---

### 9. ES6 Method Properties
**File:** `9-getFullBudget.js`

Use ES6 method shorthand syntax inside an object literal instead of the traditional `key: function()` form.

```bash
node 9-main.js
```

---

### 10. For...of Loops
**File:** `10-loops.js`

Rewrite a function using the `for...of` loop instead of `for...in`.

```bash
node 10-main.js
```

---

### 11. Iterator / Create Employees Object
**File:** `11-createEmployeesObject.js`

Write a function that creates an object with a dynamic department name as the key and an array of employees as the value.

```bash
node 11-main.js
```

---

### 12. Create Report Object
**File:** `12-createReportObject.js`

Write a function that returns a report object containing all employees grouped by department, and a method to count the number of departments.

```bash
node 12-main.js
```

---

## Author

David ROSET
