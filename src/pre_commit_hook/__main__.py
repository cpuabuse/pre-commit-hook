"""
Main file for pre_commit_hook package.
"""

# Bootstrap to be able to perform absolute imports as standalone code
if __name__ == "__main__":
	from pathlib import Path
	from sys import path
	parent_path: str = Path(__file__).parent.joinpath("..").as_posix()
	if parent_path not in path:
		path.append(parent_path)

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pre_commit_hook.defaults import description, epilog

def parse_args():
	"""
	Parses the arguments
	"""
	parser = ArgumentParser(description=description, epilog=epilog, formatter_class=RawDescriptionHelpFormatter)

def main():
	"""
	Main function.
	"""
	script_location = parse_args()

if __name__ == "__main__":
	main()