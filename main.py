import subprocess as sp
import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="git cv")
    parser.add_argument("--cv", help="cv json", required=True)
    parser.add_argument("--out", help="output folder for the generated git repo", required=True)
    conf = parser.parse_args()

    def gitcmd(*args):
        c =  ["git", "-C", conf.out] + list(args)
        print(f"*** {' '.join(c)}")
        return c

    with open(conf.cv, "r") as f:
        data = json.loads(f.read())
        sp.run(["rm", "-rf", conf.out])
        sp.run(["git", "init", conf.out])
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

            if msg and branch and merge:
                sp.run(gitcmd("checkout", merge), env=env)
                sp.run(gitcmd("merge", branch, "--no-ff", "-m", msg), env=env)
            elif msg and branch:
                sp.run(gitcmd("branch", branch), env=env)
                sp.run(gitcmd("checkout", branch), env=env)
                sp.run(gitcmd("commit", "--allow-empty", "-m", msg), env=env)
            elif msg:
                sp.run(gitcmd("commit", "--allow-empty", "-m", msg), env=env)

