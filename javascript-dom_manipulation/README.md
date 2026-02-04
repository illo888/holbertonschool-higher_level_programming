## Project Description
This project demonstrates basic DOM manipulation using JavaScript, including changing header colors, toggling classes, adding list items, and updating header text based on button clicks.

---

## JavaScript Functions

### **1. changeColour()**
Changes the color of the element with id `red_header` to red when clicked.

```javascript
function changeColour() {
  let redHeader = document.getElementById("red_header");
  redHeader.style.color = "#FF0000";
}
```

---

### **2. toggleColour()**
Toggles between the CSS classes `red` and `green` on the `<header>` element.

```javascript
function toggleColour() {
  const header = document.querySelector("header");
  header.classList.toggle("red");
  header.classList.toggle("green");
}
```

---

### **3. addLi()**
Creates a new `<li>` element with the text "Item" and appends it to the list `.my_list`.

```javascript
function addLi() {
  let newListItem = document.createElement("li");
  newListItem.textContent = "Item";
  let myList = document.querySelector(".my_list");
  myList.appendChild(newListItem);
}
```

---

### **4. updateText()**
Updates the text inside the `<header>` element to `"New Header!!!"`.

```javascript
function updateText() {
  document.querySelector("header").textContent = "New Header!!!";
}
```

---

## Requirements

### HTML
```html
<header></header>
<button id="red_header">Red Header</button>
<button id="toggle_header">Toggle Header</button>
<button id="add_item">Add Item</button>
<button id="update_header">Update Header</button>

<ul class="my_list"></ul>
```

### CSS
```css
.red { color: red; }
.green { color: green; }
```

---

## Purpose
Practice JavaScript DOM manipulation and event handling.
