import subprocess as sp
import json

out_dir = "out"
cv_json = "cv.json"

def gitcmd(*args):
    c =  ["git", "-C", out_dir] + list(args)
    print(f"*** {' '.join(c)}")
    return c

with open(cv_json, "r") as f:
    data = json.loads(f.read())
    sp.run(["rm", "-rf", out_dir])
    sp.run(["git", "init", out_dir])
    sp.run(gitcmd("config", "--local", "user.email", data.get("email")))
    sp.run(gitcmd("config", "--local", "user.name", data.get("name")))

    for d in data.get("cv"):
        date = d.get("date")
        msg = d.get("message")
        branch = d.get("branch", None)
        merge = d.get("merge", None)

        env = {
                "GIT_COMMITTER_DATE": date,
                "GIT_AUTHOR_DATE": date
        }

        sp.run(gitcmd("checkout", "master"), env=env)

        if date and msg and branch and merge:
            sp.run(gitcmd("checkout", merge), env=env)
            sp.run(gitcmd("merge", branch, "--no-ff", "-m", msg), env=env)
        elif date and msg and branch:
            sp.run(gitcmd("checkout", "-b", branch), env=env)
            sp.run(gitcmd("commit", "--allow-empty", "-m", msg), env=env)
        elif date and msg:
            sp.run(gitcmd("checkout", "master"), env=env)
            sp.run(gitcmd("commit", "--allow-empty", "-m", msg), env=env)

