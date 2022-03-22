from dataclasses import dataclass

@dataclass
class Datapoint:
    x: float
    y: float

    def __init__(self, x, y):
      self.x = float(x)
      self.y = float(x)

def main():
  datapoints = []

  with open("data.csv", "r", encoding="utf-8-sig") as file:
    datapoints = [Datapoint(*values) for values in [line.strip().split(",") for line in file]]

  with open("pik.txt", "w+") as file:
    for dp in datapoints:
      file.write(f"({dp.y}-(a*{dp.x}^2+b*{dp.x}+c))^2+")

if __name__ == "__main__":
    main()