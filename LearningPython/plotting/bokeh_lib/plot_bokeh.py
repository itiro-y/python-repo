from bokeh.plotting import figure, output_file, show

# Creating a figure object
p = figure(width=300, height=300, tools="pan,reset,save")

# add a circle render
# circle([x-cord], [y-cord], radius, alpha)
p.circle([1, 2.5, 3, 2], [2, 3, 1, 1.5], radius=0.3, alpha=0.5)

# specify how to output the plot(s)
output_file("foo.html")

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
x2 = [1, 2, 3, 4, 5]
y2 = [1, 2, 3, 4, 5]
l = figure(title="wierd graph", x_axis_label='x', y_axis_label='y')

l.line(x,y,legend_label='Temp.', line_width=2)
l.line(x2, y2, legend_label='Shifted Temp.', line_width=3, alpha=0.5)

# Display the figure
show(l)



