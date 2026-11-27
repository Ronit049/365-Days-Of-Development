# 🟨 JavaScript Notes

JavaScript adds behavior and interactivity to web pages and can also run on servers using Node.js.

## Variables and types

```javascript
const username = "Ronit";
let score = 10;
score += 5;

const isLearning = true;
const skills = ["Python", "JavaScript"];
const profile = { username, score };
```

Use `const` by default and `let` when reassignment is needed. Avoid `var` in modern code.

## Functions

```javascript
function add(a, b) {
  return a + b;
}

const multiply = (a, b) => a * b;
```

## Arrays and objects

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(number => number * 2);
const evens = numbers.filter(number => number % 2 === 0);

const user = { name: "Ronit", role: "Developer" };
console.log(user.name);
```

## DOM interaction

```javascript
const button = document.querySelector("#action");
const output = document.querySelector("#output");

button.addEventListener("click", () => {
  output.textContent = "Button clicked!";
});
```

## Async JavaScript

```javascript
async function loadUser() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/users/1");
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    const user = await response.json();
    console.log(user);
  } catch (error) {
    console.error("Could not load user:", error);
  }
}
```

## Topics checklist
- [ ] Types, coercion, and equality
- [ ] Scope and closures
- [ ] Functions and callbacks
- [ ] Arrays and objects
- [ ] Destructuring and spread
- [ ] DOM and events
- [ ] Promises and async/await
- [ ] Modules
- [ ] Error handling
- [ ] Fetch and JSON
- [ ] Browser storage and security basics

Exercises: calculator, quiz app, searchable list, weather interface, and API dashboard.

Resource: [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
