import unittest

import python_repos_visual_rev as pr

URL = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}

class TestPythonRepos(unittest.TestCase):
    def setUp(self):
        """Generate data from python_repos for testing"""
        self.r = pr.get_data(URL, headers)
        self.status_code = self.r.status_code
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0] # for example

    def test_status_code(self):
        """Check response status code"""
        self.assertEqual(self.status_code, 200)

    def test_repo_dicts(self):
        """Test output data about repositories"""
        self.assertEqual(len(self.repo_dicts), 30)

        keys = ["name", "owner", "stargazers_count", "html_url"]
        for key in keys:
            self.assertIn(key, self.repo_dict.keys())


if __name__ == "__main__":
    unittest.main()