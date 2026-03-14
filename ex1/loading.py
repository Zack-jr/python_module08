import pandas, requests, matplotlib, importlib.metadata

def check_dependencies(requirements):
    missing = []
    for req in requirements:
        try:
            importlib.metadata.version(req)
        except importlib.metadata.PackageNotFoundError:
            missing.append(req)
    return missing


def main():

    dep = {"pandas", "requests", "matplotlib"}
    print("LOADING STATUS: Loading programs")
    missing_req = check_dependencies(dep)
    if len(missing_req) == 0:
        print("Checking dependencies:")
        print(f"[OK] pandas ({importlib.metadata.version('pandas')}) - Data manipulation ready")
        print(f"[OK] requests ({importlib.metadata.version('requests')}) - Network access ready")
        print(f"[OK] matplotlib ({importlib.metadata.version('matplotlib')})- Visualization ready")


if __name__ == '__main__':
    main()