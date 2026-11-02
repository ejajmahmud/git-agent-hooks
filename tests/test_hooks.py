"""Unit tests for git_agent_hooks."""
import unittest
from git_agent_hooks.hooks import pre_commit_check

class TestHooks(unittest.TestCase):
    def test_valid_code(self):
        ok, errs = pre_commit_check("x = 10\n")
        self.assertTrue(ok)
        self.assertEqual(errs, [])

    def test_syntax_error(self):
        ok, errs = pre_commit_check("def unclosed(", is_python=True)
        self.assertFalse(ok)
        self.assertTrue(any("syntax error" in e.lower() for e in errs))

if __name__ == "__main__":
    unittest.main()
