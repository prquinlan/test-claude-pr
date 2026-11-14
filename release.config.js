module.exports = {
    "branches": ["main"],
    "tagFormat": "${version}",
    "preset": "angular",
    "repositoryUrl": "https://github.com/prquinlan/test-claude-pr.git",
    plugins: [
      '@semantic-release/commit-analyzer',
      '@semantic-release/release-notes-generator',
      '@semantic-release/exec',
      '@semantic-release/github',
    ]
};
