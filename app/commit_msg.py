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
        commit_message = commit_message.replace(
            "Here is the generated commit message:", " ")
        return commit_message.strip()
