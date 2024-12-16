Nested Structures
====================

+ Consider the telephone company "Chao". Below 200 minutes, the company charges ``$0.20`` per minute. Between 200 and 400 minutes, the price is ``$0.18``. Above 400 minutes, the price per minute is ``$0.15``. Calculate your phone bill with these conditions.
+ The company's conditions can be visually represented by the path of a road like the following image.

.. image:: ../img/TWP10_011.jpg
    :height: 9.754cm
    :width: 22.859cm
    :align: center
    :alt:

+ Nested conditions can be created.
+ Remember to indent nested portions of code.

.. codelens:: cl_l10_5a_en

    minutes = 800
    if minutes < 200:
        price = 0.20
    else:
        if minutes <= 400:
            price = 0.18
        else:
            price = 0.15
    print("Telephone bill : $%6.2f" % (minutes * price))

+ Note the double indentation to satisfy the second condition.
+ Now we modify the "Chao" company program for a promotion where the rate is ``$0.08`` when you use more than 800 minutes.

.. codelens:: cl_l10_5b_en

    minutes = 1000
    if minutes < 200:
        price = 0.2
    else:
        if minutes <= 400:
            price = 0.18
        else:
            if minutes <= 800:
                price = 0.15
            else:
                price = 0.08
    print("Telephone bill : $%6.2f" % (minutes * price))

+ Note that nested structures can grow.
+ Python, given its characteristics, provides the ``elif`` clause.
+ It is used to check multiple conditions.
