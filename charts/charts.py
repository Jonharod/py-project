import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A","B","C"]
    values = [300, 34, 140]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()
