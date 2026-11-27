# 🗄️ SQL and Database Fundamentals

SQL is used to define, query, and modify relational data.

## Example schema

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    score DECIMAL(5, 2)
);

INSERT INTO students (id, name, department, score)
VALUES (1, 'Ronit', 'CSE', 92.50);
```

## Read data

```sql
SELECT name, score
FROM students
WHERE score >= 80
ORDER BY score DESC;
```

## Update and delete

```sql
UPDATE students
SET score = 95
WHERE id = 1;

DELETE FROM students
WHERE id = 1;
```

Always check the `WHERE` condition before running an update or delete.

## Aggregate functions

```sql
SELECT department, AVG(score) AS average_score, COUNT(*) AS total
FROM students
GROUP BY department
HAVING COUNT(*) >= 2;
```

## Joins

```sql
SELECT students.name, courses.course_name
FROM students
JOIN enrollments ON enrollments.student_id = students.id
JOIN courses ON courses.id = enrollments.course_id;
```

Learn `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN` where supported.

## Topics checklist
- [ ] SELECT, WHERE, ORDER BY
- [ ] INSERT, UPDATE, DELETE
- [ ] Aggregate functions
- [ ] GROUP BY and HAVING
- [ ] Joins and subqueries
- [ ] Primary and foreign keys
- [ ] Constraints
- [ ] Normalization
- [ ] Indexes
- [ ] Transactions and ACID
- [ ] Views

Practice with [PostgreSQL documentation](https://www.postgresql.org/docs/) or [SQLite](https://www.sqlite.org/docs.html).
