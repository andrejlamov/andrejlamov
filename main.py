import subprocess as sp
import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="git cv")
    parser.add_argument("--cv", help="cv json", required=True)
    parser.add_argument("--out", help="output folder for the generated git repo", required=True)
    parser.add_argument("--verbose", help="log everything", action="store_true")

    conf = parser.parse_args()

    run_flags = {} if conf.verbose else {"stderr": sp.DEVNULL, "stdout": sp.DEVNULL}

    def gitcmd(*args, **kwargs):
        c =  ["git", "-C", conf.out] + list(args)
        sp.run(c, **run_flags, **kwargs)
        if conf.verbose:
            print(f"*** {' '.join(c)}")
        return c

    with open(conf.cv, "r") as f:
        data = json.loads(f.read())
        sp.run(["rm", "-rf", conf.out])
        sp.run(["git", "init", conf.out], **run_flags)
        gitcmd("config", "--local", "user.email", data.get("email"))
        gitcmd("config", "--local", "user.name", data.get("name"))

        for d in data.get("cv"):
            date = d.get("date")
            msg = d.get("message")
            branch = d.get("branch", None)
            merge = d.get("merge", None)

            env = {
                    "GIT_COMMITTER_DATE": date,
                    "GIT_AUTHOR_DATE": date
            }
            
            gitcmd2 = lambda *args, **kwargs: gitcmd(*args, **{**{"env": env}, **kwargs})

            if msg and branch and merge:
                gitcmd2("checkout", merge)
                gitcmd2("merge", branch, "--no-ff", "-m", msg)
            elif msg and branch:
                gitcmd2("branch", branch)
                gitcmd2("checkout", branch)
                gitcmd2("commit", "--allow-empty", "-m", msg)
            elif msg:
                gitcmd2("commit", "--allow-empty", "-m", msg)

