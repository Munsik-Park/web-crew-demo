from crewai.tools import BaseTool
import git
import os

class GitPushTool(BaseTool):
    name: str = "Git Push Tool"
    description: str = (
        "Initialize a git repository if needed, add all files, commit with a message, and push to the remote."
        "Use this tool when you have finished writing code and want to save it to the repository."
    )

    def _run(self, commit_message: str) -> str:
        repo_path = os.getcwd()
        remote_url = "https://github.com/Munsik-Park/web-crew-demo.git"
        
        try:
            try:
                repo = git.Repo(repo_path)
            except git.exc.InvalidGitRepositoryError:
                repo = git.Repo.init(repo_path)
                # Check if remote exists, if not add it
                if 'origin' not in repo.remotes:
                    repo.create_remote('origin', remote_url)
            
            # Ensure we are on main branch
            if repo.active_branch.name != 'main':
                try:
                    repo.git.checkout('-b', 'main')
                except:
                    repo.git.checkout('main')

            # Security Check: Ensure .env is ignored
            gitignore_path = os.path.join(repo_path, '.gitignore')
            if os.path.exists(os.path.join(repo_path, '.env')):
                if not os.path.exists(gitignore_path):
                    with open(gitignore_path, "w") as f:
                        f.write(".env\n")
                else:
                    with open(gitignore_path, "r") as f:
                        if ".env" not in f.read():
                            with open(gitignore_path, "a") as f:
                                f.write("\n.env\n")

            # Add all files
            repo.git.add('.')
            
            # Commit
            #Check if there are changes to commit
            if repo.is_dirty() or repo.untracked_files:
                repo.index.commit(commit_message)
                
                # Push
                # Note: This relies on local credentials being configured.
                # If using HTTPS with 2FA, it might fail without a token manager.
                # Since the user mentioned MCP connection, we assume their environment is set up.
                origin = repo.remote(name='origin')
                origin.push(refspec='main:main')
                
                return f"Successfully pushed code to {remote_url} with message: '{commit_message}'"
            else:
                return "No changes to commit."

        except Exception as e:
            return f"Error pushing to GitHub: {str(e)}"
