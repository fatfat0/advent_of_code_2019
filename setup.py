from setuptools import setup, find_packages

packages = find_packages(where=".")

setup(packages=packages, package_dir={"": "."})

# setup(
#     name="advent_of_code_2019",
#     version="0.1",
#     description="Python OO rewrite of (some) AOC 2019 exercises",
#     author="Fatih & Ignacio & Pooja",
#     packages=["aoc_2019"],
# )
