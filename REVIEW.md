# Review standards

Used by the automated Claude PR review (`.github/workflows/claude-pr-review.yml`).

## Flag
- Logic bugs: wrong results, off-by-one errors, unhandled edge cases (empty input, `None`, missing files).
- Security issues: secrets in code, unsafe use of user input (shell, SQL, file paths), insecure defaults.
- Missing or swallowed error handling (bare `except:`, errors silently ignored).
- Race conditions: shared state or files touched concurrently without locking, check-then-act bugs.
- GitHub Actions: secrets or `${{ }}` untrusted input interpolated directly into `run:` scripts,
  overly broad `permissions`, third-party actions not pinned to a commit SHA.

## Don't flag
- Formatting or naming preferences.
- Missing comments or docstrings.
- Suggestions to refactor working code without a concrete defect.

## Also mention (in the PR comment, not inline)
- Open Dependabot PRs (`gh pr list --author app/dependabot`) that could be merged alongside
  this one, e.g. bumps to the same files or dependencies. List each by number and title.
