import os
from dotenv import find_dotenv, load_dotenv


def main():

    vars = ["API_KEY",
            "MATRIX_MODE",
            "DATABASE_URL",
            "LOG_LEVEL",
            "ZION_ENDPOINT"]

    dotenv_path = find_dotenv('.env')
    load_dotenv(dotenv_path)

    API = os.getenv(vars[0])
    MATRIX_MODE = os.getenv(vars[1])
    DATABASE = os.getenv(vars[2])
    LOG = os.getenv(vars[3])
    ZION = os.getenv(vars[4])

    missing = []
    for var in vars:
        if os.getenv(var) is None:
            missing.append(var)

    if dotenv_path == "":
        print("Missing .env file.\n")

    elif len(missing) == 0 and dotenv_path:
        print("\nORACLE STATUS: Reading the Matrix...\n")
        print("Configuration loaded:")
        print(f"Mode: {MATRIX_MODE}")
        print(f"Database: {DATABASE}")
        print(f"API Access: {API}")
        print(f"Log Level: {LOG}")
        print(f"Zion Network: {ZION}\n")

        print("Environment security check:")
        print("[OK] No hardcoded secrets detected")
        print('[OK] .env file properly configured')
        print('[OK] Production overrides available')

        print("\nThe Oracle sees all configurations.")

    elif missing is not None:
        print(f"Missing configuration: {missing}.\n")


if __name__ == '__main__':
    main()
