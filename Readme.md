[![Icommit](https://i.postimg.cc/02bFw0zk/temp-Image3-LGD2m.avif)](https://postimg.cc/kBPTr8Nz)
---
## ICOMMIT - AI-Driven Git Commit Messages

**Icommit** is a simple command-line tool that generates meaningful commit messages for your Git repositories. By analyzing staged changes, it leverages Groq’s AI-powered Llama models to produce high-quality messages.

![Icommit Badge](https://img.shields.io/badge/Icommit-8A2BE2) ![PyPI - Downloads](https://img.shields.io/pypi/dm/icommit)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
  - [Install Icommit](#install-icommit)
  - [Set Up the API Key](#set-up-the-api-key)
- [Usage](#usage)
  - [Generating Commit Messages](#generating-commit-messages)
  - [CLI Commands](#cli-commands)
- [Configuration](#configuration)
- [Example Usage](#example-usage)
- [Troubleshooting](#troubleshooting)
- [Release Notes](#release-notes)
- [License](#license)

## Features

- Generates AI-driven commit messages from staged Git changes
- Uses Groq’s AI model to analyze code diffs
- Easy Git integration with minimal setup
- Secure API key handling (no environment variables)
- Simple CLI commands for quick use

## Installation

To start using ICOMMIT, follow these steps:

### 1. Install Icommit

You can install ICOMMIT via pip:

```bash
pip install icommit
```

### 2. Set up the API Key

To use the AI-powered commit message generation, you need to configure your API key:

1. Visit [Groq Console](https://console.groq.com/) and create an account.
2. Generate a new API key and copy it.
3. Run the following command to store your API key:
```bash
icommit-key <api-key>
```
This securely saves your API key in a local configuration file.

## Usage

### Generating Commit Messages

Once you’ve set up the API key, you can generate commit messages based on your staged changes in any Git repository.

1. Stage your changes:

```bash
git add .
```

2. Generate a commit message:

```bash
icommit
```

This command will analyze the staged files and suggest a concise, AI-generated commit message for you.

### CLI Commands

#### `icommit`

This command generates a commit message based on the changes in the current directory (specifically staged Git files).

```bash
icommit
```

- The AI model analyzes the diffs and generates a summary of the changes.
- It automatically uses the Groq AI model for analysis.

#### `icommit-key`

This command allows you to set your API key, which is needed for the AI-powered functionality.

```bash
icommit-key <your-api-key>
```

- The API key is stored locally, ensuring security without relying on environment variables.
- This command is essential before you can run the `icommit` command.

## Configuration

ICOMMIT stores your API key in a local configuration file for security. You can view or modify the configuration file directly if needed (location depends on your OS, e.g., `~/.icommit_config` or similar).

## Example Usage

### Stage Your Files:

```bash
git add src/example_file.py
```

### Generate a Commit Message:

```bash
icommit
```

### Output:

```
feat(api): add user authentication endpoint

- Added POST route for user login
- Implemented JWT token generation for secure sessions
- Updated user model to include password hashing

The API now supports secure user login with JWT authentication.
```
## Troubleshooting

- If the API key is missing or invalid, you’ll be prompted to set it using the `icommit-key` command before generating commit messages.
- Ensure that you have staged changes using `git add` before running the `icommit` command.
- If the tool doesn’t seem to work as expected, check the configuration file for your API key, or reset it by running `icommit-key <new-api-key>`.

## Release Notes

For details on the latest releases, see the [Releases Notes](./Releasenotes.md) here.

## License

This project is licensed under the MIT License - see the [LICENSE](./License.txt) file for details.
