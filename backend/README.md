# Wearless Backend

# Setup Steps

1.  Install the AWS CLI https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
2.  Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

    - Install the specified [Python Version](.python-version) using uv
      ```
      uv python install x.x
      ```
    - Initalize uv environment with the following commands

      ```
      $ uv venv
      $ source .venv/Scripts/activate
      $ uv sync
      ```
