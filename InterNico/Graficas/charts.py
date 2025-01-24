import matplotlib.pyplot as plt
import random

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(l, v):
    fig, ax = plt.subplots()
    ax.pie(v, labels=l)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = [x for x in 'abcdefghijklmno']
    values = [random.randint(1,20) for x in range(1, 16)]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)




