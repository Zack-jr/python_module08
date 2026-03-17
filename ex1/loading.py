import importlib


def check_dependencies(requirements):
    missing = []
    imported = {}
    for req in requirements:
        try:
            imported[req] = importlib.import_module(req)  # dynamic import
        except ModuleNotFoundError:
            missing.append(req)
    return missing, imported


def calculate_avg_temp(matrix_data, np) -> float:

    print("Processing 1000 data points...")
    temps = np.array(matrix_data["hourly"]["temperature_2m"])
    avg = round(np.mean(temps), 2)
    return avg


def compare():

    print("Checking dependencies:")
    print(f"[OK] pandas ({importlib.metadata.version('pandas')}) "
          "- Data manipulation ready")
    print(f"[OK] requests ({importlib.metadata.version('requests')}) - "
          "Network access ready")
    print(f"[OK] matplotlib ({importlib.metadata.version('matplotlib')})- "
          "Visualization ready\n")


def main():

    dep = ["pandas", "requests", "matplotlib.pyplot", "numpy"]
    missing_req, imported = check_dependencies(dep)

    if len(missing_req) == 0:
        print("LOADING STATUS: Loading programs\n")

        compare()
        url = ("https://api.open-meteo.com/v1/forecast?"
               "latitude=40.41&longitude=-3.70&hourly=temperature_2m")

        # store the imported modules in variables
        plt = imported["matplotlib.pyplot"]
        requests = imported["requests"]
        np = imported["numpy"]

        print("Analyzing Matrix data...")
        matrix_data = requests.get(url).json()
        avg = calculate_avg_temp(matrix_data, np)
        len_data = len(matrix_data["hourly"]["temperature_2m"])

        print("Generating visualization...\n")
        plt.title(f"Hourly temperatures in Madrid\n Last {len_data}"
                  f" hours avg temp = {avg} C")
        plt.plot(matrix_data["hourly"]["temperature_2m"])
        plt.xlabel("Hours")
        plt.ylabel("Temperature in C")
        plt.savefig("matrix_analysis.png")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")

    else:
        reqs = ', '.join(missing_req)
        print(f"Missing dependencies: {reqs}."
              f" Run pip install -r requirements.txt")


if __name__ == '__main__':
    main()
