#!/usr/bin/env python3
"""
Hello World - Your first Python program!
This is where we start our coding journey together.
"""

def main():
    print("Hello, World! 🐉")
    print("Welcome to coding, Steven!")
    
    # Fun antigravity Easter egg (built into Python!)
    try:
        import antigravity
        print("Antigravity module imported successfully!")
    except ImportError:
        print("Antigravity module not available (that's okay!)")

if __name__ == "__main__":
    main()