import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from model import ForestFireModel


def run_multiple_simulations(humidity, runs=30, size=100):

    final_burned = []

    for i in range(runs):
        model = ForestFireModel(size=size, wind=(1,0), fixed_humidity=humidity)

        while True:
            burning = np.sum(model.grid == 2)
            if burning == 0:
                break
            model.step()

        burned = np.sum(model.grid == 3)
        final_burned.append(burned)

    return np.mean(final_burned), np.std(final_burned)


def main():

    humidities = [0.2, 0.5, 0.8]
    results = []

    for h in humidities:
        mean, std = run_multiple_simulations(h, runs=30)
        results.append([h, mean, std])
        print(f"H={h} → mean={mean:.2f}, std={std:.2f}")

    df = pd.DataFrame(results, columns=["humidity", "mean_burned", "std_burned"])
    df.to_csv("humidity_summary.csv", index=False)

    # Plot
    plt.figure()
    plt.errorbar(df["humidity"], df["mean_burned"],
                 yerr=df["std_burned"], marker='o')
    plt.xlabel("Humidity")
    plt.ylabel("Final Burned Area")
    plt.title("Effect of Humidity on Fire Spread")
    plt.savefig("humidity_analysis.png")
    plt.show()


if __name__ == "__main__":
    main()
