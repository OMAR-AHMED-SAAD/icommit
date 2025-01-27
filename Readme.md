# ICOMMIT

Icommit is a simple command-line tool to generate commit messages for Git repositories. It analyzes the staged changes in your files and generates meaningful commit messages using Groq’s AI-powered Llama models.

![PyPI - Downloads](https://img.shields.io/pypi/dd/icommit)

## Features

- Generates commit messages for staged Git changes
- Uses Groq’s AI model to analyze code diffs
- Easy setup and integration with Git workflow
- Simple CLI commands for quick use
- Secure, non-environment-based API key handling

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

This will save the API key to a configuration file on your local system, ensuring it is kept secure and used only for your Icommit requests.

## Usage

### Generating a Commit Message

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

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE.txt) file for details.
