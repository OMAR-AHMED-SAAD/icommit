import re
class CommitMsg:
    """
    Class to handle the commit message transformations 
    """
    @staticmethod
    def clean_commit_message(commit_message: str) -> str:
        """
        Clean the commit message by removing any trailing whitespace and newlines or invalid ai generated text
        Parameters:
            commit_message (str): The commit message to clean
        Returns:
            str: The cleaned commit message
        """
        prefixes = r"(feat|refactor|perf|docs|test|chore|style|build)"

        # Use regex to remove everything before the prefix
        match = re.search(rf"\b{prefixes}\b.*", commit_message, re.IGNORECASE)
        if match:
            return match.group(0).strip()
        return commit_message.strip()
