============================================
Mastering Data Visualization with Matplotlib
============================================

.. image:: ../img/TWP68_001.png
    :height: 14.925cm
    :width: 9.258cm
    :align: center
    :alt:

Introduction
------------
This comprehensive lecture series focuses on mastering Matplotlib, one of the most popular libraries in Python for data visualization. We will explore various functionalities of Matplotlib, understanding how to create a wide array of plots to effectively communicate data insights.

Part 1: Understanding Matplotlib Basics
---------------------------------------

.. contents::
   :local:

Overview
~~~~~~~~
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It provides a low-level interface for creating a variety of plots, giving you full control over every aspect of the figure.

Installing Matplotlib
~~~~~~~~~~~~~~~~~~~~~
Install Matplotlib using pip::

    pip install matplotlib

Importing Matplotlib
~~~~~~~~~~~~~~~~~~~~
Import Matplotlib in your Python script::

    import matplotlib.pyplot as plt

Creating Basic Plots
~~~~~~~~~~~~~~~~~~~~
**Line Plot**::

    # Sample Data
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 25, 30, 35]

    # Plot
    plt.plot(x, y)
    plt.title('Line Plot Example')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

**Bar Plot**::

    # Sample Data
    categories = ['A', 'B', 'C', 'D']
    values = [4, 7, 1, 8]

    # Plot
    plt.bar(categories, values)
    plt.title('Bar Plot Example')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

**Scatter Plot**::

    # Sample Data
    x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
    y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]

    # Plot
    plt.scatter(x, y)
    plt.title('Scatter Plot Example')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

Part 2: Advanced Plotting Techniques
------------------------------------

.. contents::
   :local:

Histograms
~~~~~~~~~~
**Histogram**::

    # Sample Data
    data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

    # Plot
    plt.hist(data, bins=4)
    plt.title('Histogram Example')
    plt.xlabel('Data Bins')
    plt.ylabel('Frequency')
    plt.show()

Box Plots
~~~~~~~~~
**Box Plot**::

    # Sample Data
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Plot
    plt.boxplot(data)
    plt.title('Box Plot Example')
    plt.ylabel('Values')
    plt.show()

Pie Charts
~~~~~~~~~~
**Pie Chart**::

    # Sample Data
    labels = 'A', 'B', 'C', 'D'
    sizes = [15, 30, 45, 10]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    # Plot
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart Example')
    plt.show()

Part 3: Customizing Plots
-------------------------

.. contents::
   :local:

Adding Grid
~~~~~~~~~~~
Add grid to your plot::

    plt.plot(x, y)
    plt.grid(True)
    plt.show()

Changing Line Styles and Colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Change line style and color::

    plt.plot(x, y, linestyle='--', color='r')
    plt.show()

Adding Annotations
~~~~~~~~~~~~~~~~~~
Add annotations to your plot::

    plt.plot(x, y)
    plt.annotate('Highest Point', xy=(4, 30), xytext=(3, 35),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()

Part 4: Real-world Applications and Case Studies
------------------------------------------------

.. contents::
   :local:

Healthcare Data Analysis
~~~~~~~~~~~~~~~~~~~~~~~~
- Visualize patient wait times using histograms.
- Analyze service distribution with bar plots.

Financial Data Analysis
~~~~~~~~~~~~~~~~~~~~~~~
- Visualize stock market trends with line charts.
- Analyze portfolio performance using scatter plots.

Social Media Data Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~
- Perform sentiment analysis with bar plots.
- Detect trends using time series visualizations.

Part 5: Best Practices for Data Visualization
---------------------------------------------

.. contents::
   :local:

Clarity
~~~~~~~
Ensure your visualization is easy to understand.

Accuracy
~~~~~~~~
Represent data accurately without misleading.

Aesthetics
~~~~~~~~~~
Use color and design effectively but avoid over-complicating.

Context
~~~~~~~
Provide context with titles, labels, and legends.

Part 6: Example
---------------

.. contents::
   :local:

Here is an example of visualizing sales data using Matplotlib. The example uses sales data from a CSV file and then visualizes it using various types of plots.

.. activecode:: ac_l68_1a_en
   :nocodelens:
   :language: python3
   :python3_interpreter: pyscript

   import pandas as pd
   import matplotlib.pyplot as plt

   from pyscript import display

   # Sample data
   sales_data = pd.DataFrame({
       'class': ['First', 'Second', 'Third', 'First', 'Second', 'Third', 'First', 'Second', 'Third', 'First', 'Second', 'Third', 'First', 'Second', 'Third'],
       'fare': [71.2833, 10.5, 7.25, 53.1, 8.05, 7.8542, 51.8625, 21.0, 11.1333, 26.55, 31.275, 7.8542, 61.3792, 14.4542, 7.7417]
   })

   # Create the plot
   fig, ax = plt.subplots(figsize=(10, 6))
   ax.bar(sales_data['class'], sales_data['fare'], color='skyblue')
   ax.set_title("Sales Data Visualization")
   ax.set_xlabel("Class")
   ax.set_ylabel("Fare")

   # Display the plot
   display(fig)


.. activecode:: ac_l68_1b_en
   :nocodelens:
   :language: python3
   :python3_interpreter: pyscript

   import matplotlib.pyplot as plt
   import matplotlib.tri as tri
   import numpy as np

   from pyscript import display

   # First create the x and y coordinates of the points.
   n_angles = 36
   n_radii = 8
   min_radius = 0.25
   radii = np.linspace(min_radius, 0.95, n_radii)

   angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
   angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
   angles[:, 1::2] += np.pi / n_angles

   x = (radii * np.cos(angles)).flatten()
   y = (radii * np.sin(angles)).flatten()
   z = (np.cos(radii) * np.cos(3 * angles)).flatten()

   # Create the Triangulation; no triangles so Delaunay triangulation created.
   triang = tri.Triangulation(x, y)

   # Mask off unwanted triangles.
   triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                               y[triang.triangles].mean(axis=1))
                   < min_radius)

   fig1, ax1 = plt.subplots()
   ax1.set_aspect('equal')
   tpc = ax1.tripcolor(triang, z, shading='flat')
   fig1.colorbar(tpc)
   ax1.set_title('tripcolor of Delaunay triangulation, flat shading')

   display(fig1)

