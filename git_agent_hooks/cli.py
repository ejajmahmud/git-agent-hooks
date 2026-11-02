"""Command line interface for git-agent-hooks."""
from .hooks import pre_commit_check

def main():
    code = "def foo():\n    print('Valid Python')\n"
    ok, errs = pre_commit_check(code)
    print("Pre-commit check status:", "PASS" if ok else "FAIL", errs)

if __name__ == "__main__":
    main()
