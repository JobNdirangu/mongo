# 📘 Day 1: MongoDB Basics – Databases, Collections & Inserts

Setting up databases, creating collections by inserting documents, and viewing data.

---

## 🧠 Objectives
By the end of this lesson, you should be able to:

- Understand MongoDB's structure: **Database → Collection → Document**
- Create and switch databases using MongoDB Shell or Compass
- Insert single and multiple documents into collections
- View basic inserted data

---

## 🏗️ MongoDB Structure Overview

| Concept     | Equivalent In SQL | Example                            |
|-------------|-------------------|------------------------------------|
| Database    | Database           | `use school`                      |
| Collection  | Table              | `students`, `books`               |
| Document    | Row (record)       | `{ name: "Alice", age: 20 }`      |

---

## ⚙️ Mongo Shell Commands

### 🔹 Show All Databases
```bash
show dbs
```

## 🔹 Create or Switch to a Database
``` bash
use school
```
## 📥 Insert Documents
### 🔸 Insert One Document

``` bash
db.students.insertOne({ name: "Alice", age: 20, course: "Math" })
```
### 🔸 Insert Many Document

```bash
db.students.insertMany([
  { name: "Bob", age: 22, course: "Physics" },
  { name: "Clara", age: 21, course: "Biology" }
])
```
Note: Collections are created automatically when you insert the first document.

## 👀 View Collections and Documents
### 🔸 Show Collections

```bash
show collections
```

### 🔸 View All Documents in a Collection

```bash
db.students.find()
```
Task 1: Create student_portal DB and students, teacher Collection
Task 2: Create a New Database inventory

### Bonus Challenge
Go back to student_portal

Create a staff collection
Insert at least 3 staff members with name, role, and department

### ERD Diagram
![alt text](image.png)