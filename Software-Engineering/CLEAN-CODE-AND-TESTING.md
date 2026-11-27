# 🧪 Clean Code, Debugging, and Testing

## Clean code habits
- Use names that communicate intent.
- Keep functions focused and reasonably small.
- Avoid unexplained constants.
- Reduce duplication when a shared abstraction genuinely helps.
- Validate external input.
- Handle errors explicitly.
- Document why a non-obvious decision was made.

## Debugging workflow
1. Reproduce the issue reliably.
2. Read the complete error message and stack trace.
3. Identify the smallest failing example.
4. Inspect assumptions and variable values.
5. Change one thing at a time.
6. Add a regression test.
7. Confirm the fix does not break nearby behavior.

## Testing levels
- **Unit tests:** test a small function or component.
- **Integration tests:** test interactions between components.
- **End-to-end tests:** test a user workflow through the application.

## Example: Python unit test

```python
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

Run with pytest after installing it:

```bash
python -m pip install pytest
pytest
```

## Before marking a task complete
- [ ] Normal case tested
- [ ] Edge cases considered
- [ ] Errors handled
- [ ] Tests pass
- [ ] No secrets committed
- [ ] Documentation updated
