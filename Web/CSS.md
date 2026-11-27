# 🎨 CSS Notes

CSS controls the visual presentation and layout of HTML.

## Selectors and box model

```css
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  line-height: 1.5;
}

.card {
  width: min(100% - 2rem, 40rem);
  margin: 2rem auto;
  padding: 1.5rem;
  border: 1px solid #ddd;
  border-radius: 1rem;
}
```

The box model includes content, padding, border, and margin.

## Flexbox

```css
.container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
```

Use Flexbox for one-dimensional layouts.

## Grid

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
}
```

Use Grid for two-dimensional layouts.

## Responsive design

```css
.content {
  padding: 1rem;
}

@media (min-width: 768px) {
  .content {
    padding: 2rem;
  }
}
```

## Topics checklist
- [ ] Selectors and specificity
- [ ] Cascade and inheritance
- [ ] Box model
- [ ] Display and positioning
- [ ] Flexbox
- [ ] Grid
- [ ] Responsive media queries
- [ ] Units and typography
- [ ] Transitions and transforms
- [ ] CSS variables
- [ ] Accessibility and focus states

Exercises: recreate a profile card, responsive navbar, dashboard layout, and landing page.

Resource: [MDN CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
