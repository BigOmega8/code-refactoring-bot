import argparse

def main():
    parser = argparse.ArgumentParser(description = "Code Refactoring Bot")
    parser.add_argument(
        "filepath",
        type=str,
        help = "Path to Python file you want to analyze or refactor",
    )
    args = parser.parse_args()

    print(f"Code Refactoring bot: Ready to analyze: {args.filepath}")

if __name__ == '__main__':
    main()