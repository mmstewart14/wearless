# Wearless Backend

# Setup Steps

1.  Install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

2.  Install the AWS Toolkit Extension and [Authenicate with IAM Credentials](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-credentials.html)

    - Command Palette > AWS: Add a New Connection

    - Enter your credentials with the Profile Name: 'default'

    - Find your `.aws` folder and create a new `config` file there with the following contents:

    ```
    [default]
    region=us-east-2
    ```

3.  Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

    - Install the specified [Python Version](.python-version) using uv

      ```bash
      uv python install x.x
      ```

    - Initalize uv environment with the following commands

      ```bash
      $ uv venv
      $ source .venv/bin/activate
      $ uv sync
      ```

4.
