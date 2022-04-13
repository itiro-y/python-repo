# Birthday Plots
from ex35 import countMonthDup
from bokeh.plotting import figure, output_file, show
import math

def main():
    months_num = countMonthDup()
    months_label = ["January","February","March","April","May","June","July",
                    "August","September","October","November","December"]

    x = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5]
    plot = figure(title='Ex 36 - Birthday Plots',width=800,height=500,x_range=months_label,x_axis_label='Months', y_axis_label='Number of similarities',tools="pan,reset,save")
    plot.vbar(x=x, top=months_num, width=0.5, color='blue', bottom=0)
    show(plot)


if __name__ == '__main__':
    main()