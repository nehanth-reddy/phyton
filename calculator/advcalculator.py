import subprocess

def run_applescript(script, *args):
    """Run an AppleScript script with arguments"""
    args_str = " ".join(f'"{arg}"' for arg in args)
    command = f"osascript -e '{script}' {args_str}"
    subprocess.run(command, shell=True, check=True)

def main():
    # Get the user input
    user_input = input("Enter a mathematical expression: ")

    # AppleScript script to perform the calculation
    applescript = """
    on run {userInput}
        tell application "Chrome"
            activate
            delay 1
            set the clipboard to userInput
            tell application "System Events"
                keystroke "v" using command down
                keystroke "="
            end tell
            delay 1
        end tell
    end run
    """

    # Run the AppleScript with the user input
    run_applescript(applescript, user_input)
    print("operation executed")
if __name__ == "__main__":
    main()