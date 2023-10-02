
---

**Description:**

This script will display the public gists for a given GitHub username.

- Requires Python 3.
- No GitHub token is required, as public gists can be accessed anonymously.

**Installation:**

Install the required dependencies:

```shell
pip3 install -r requirements.txt
```

**How to Use:**

Run the script with the following command:

```shell
python3 user-gists.py github-username
```

On the first run, it will retrieve all gists for the supplied username and display some details about them. The script will store the creation time of the latest gist, and on subsequent runs, it will only display gists that were created since that creation time.

**Note:** The current directory must be writable, as the latest gist creation time will be stored in a file named `<github-username>-latest_gist.yaml`. Removing this file will force the script to pull in all gists for the specified username.

---