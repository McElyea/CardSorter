# Commit attribution

The project owner requests attribution for Codex's contributions to commits.

- When Codex creates a commit containing its contributions, append this trailer
  after a blank line in the commit message:

  ```text
  Co-authored-by: Codex <noreply@openai.com>
  ```

- Keep the owner's configured Git author identity and preserve other contributors'
  attribution. Do not add duplicate trailers.
- Pushing an existing commit alone does not constitute co-authorship.
- Apply this to future commits. Do not amend published history to add attribution
  unless the owner explicitly requests it.
