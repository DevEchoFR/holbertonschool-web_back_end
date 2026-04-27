# ES6 Classes

## Description

This project covers the fundamentals of ES6 classes in JavaScript. Each task focuses on a specific concept such as class declaration, inheritance, getters/setters, static methods, and symbols.

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

### 0. You used to attend a place like this at some point
**File:** `0-classroom.js`

Implement a class `ClassRoom` that accepts a `maxStudentsSize` attribute stored as `_maxStudentsSize`.

```bash
node 0-main.js
```

---

### 1. Let's make some classrooms
**File:** `1-make_classrooms.js`

Implement a function `initializeRooms` that returns an array of 3 `ClassRoom` objects with sizes 19, 20, and 34.

```bash
node 1-main.js
```

---

### 2. A Course, Getters, and Setters
**File:** `2-hbtn_course.js`

Implement a class `HolbertonCourse` with attributes `name` (String), `length` (Number), and `students` (Array of Strings). Includes type validation and getters/setters for each attribute.

```bash
node 2-main.js
```

---

### 3. Methods, static methods, computed methods names..... MONEY
**File:** `3-currency.js`

Implement a class `Currency` with attributes `code` and `name`, and a method `displayFullCurrency` that returns `name (code)`.

```bash
node 3-main.js
```

---

### 4. Pricing
**File:** `4-pricing.js`

Implement a class `Pricing` with attributes `amount` and `currency`. Includes a `displayFullPrice` method and a static `convertPrice` method.

```bash
node 4-main.js
```

---

### 5. A Building
**File:** `5-building.js`

Implement an abstract class `Building` with attribute `sqft`. Any subclass must override the `evacuationWarningMessage` method or an error is thrown.

```bash
node 5-main.js
```

---

### 6. Inheritance
**File:** `6-sky_high.js`

Implement a class `SkyHighBuilding` that extends `Building`, adds a `floors` attribute, and overrides `evacuationWarningMessage`.

```bash
node 6-main.js
```

---

### 7. Airport
**File:** `7-airport.js`

Implement a class `Airport` with attributes `name` and `code`. The default string description returns the airport code using `Symbol.toStringTag`.

```bash
node 7-main.js
```

---

### 8. Primitive - Holberton Class
**File:** `8-hbtn_class.js`

Implement a class `HolbertonClass` that casts to a `Number` (returns `size`) or a `String` (returns `location`) using `Symbol.toPrimitive`.

```bash
node 8-main.js
```

---

### 9. Hoisting
**File:** `9-hoisting.js`

Fix a broken implementation of `HolbertonClass` and `StudentHolberton` that suffered from hoisting issues, a missing constructor parameter, incorrect use of `self`, and an infinite getter loop.

```bash
node 9-main.js
```

---

### 10. Vroom
**File:** `10-car.js`

Implement a class `Car` with attributes `brand`, `motor`, and `color`. Add a `cloneCar` method that returns a new instance of the same class using `Symbol.species`.

```bash
node 10-main.js
```

---

## Author

David ROSET
