# text-diff

Produces readable word-level diffs between two pieces of text.

## Why

I wanted something I could read in one sitting and vendor into a project if needed.

## Install

```bash
pip install text-diff
```

## Usage

```python
from text_diff import textDiff

result = textDiff("example")
print(result)
```

## Notes

- No runtime dependencies outside the standard library.
- Tested on Python 3.9 and newer.

## License

MIT
