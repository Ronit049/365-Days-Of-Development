# 🌐 HTML Notes

HTML defines the structure and meaning of web content.

## Basic document

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Page</title>
</head>
<body>
  <header>
    <h1>My Portfolio</h1>
    <nav><a href="#about">About</a></nav>
  </header>
  <main>
    <section id="about">
      <h2>About me</h2>
      <p>I am learning web development.</p>
    </section>
  </main>
  <footer>Made while learning HTML.</footer>
</body>
</html>
```

## Important elements
- Headings: `h1` to `h6`
- Text: `p`, `strong`, `em`
- Links and media: `a`, `img`, `video`
- Lists: `ul`, `ol`, `li`
- Structure: `header`, `nav`, `main`, `section`, `article`, `footer`
- Forms: `form`, `label`, `input`, `textarea`, `button`
- Tables: `table`, `thead`, `tbody`, `tr`, `th`, `td`

## Good practices
- Use semantic elements.
- Provide meaningful `alt` text for informative images.
- Associate labels with form controls.
- Keep heading levels logical.
- Use accessible names and keyboard-friendly controls.

## Exercises
Build a semantic profile page, a contact form, and a small multi-section portfolio page.

Resource: [MDN HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
