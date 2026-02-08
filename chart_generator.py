import matplotlib.pyplot as plt

def generate_chart(data, title='Chart', xlabel='X-axis', ylabel='Y-axis'):
    plt.figure(figsize=(10, 5))
    plt.plot(data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.savefig('chart.png')
    plt.show()

# Example data
if __name__ == "__main__":
    example_data = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    generate_chart(example_data, title="Example Chart")