##XML
# Import Pandas and a part of the xml module.
import pandas
import xml.etree.ElementTree as ET


# Load and parse the XML file into a tree.
tree = ET.parse('purchases.xml')

# Find the root of the tree. This is the node of the tree where we'll
# start our iteration.
root = tree.getroot()

# Define a custom function to loop over our tree, extract values, and
# return a two-dimensional list.
def xml_to_list(root):
    result = []
    for row in root:
        row_list = []
        for column in row:
            row_list.append(column.text)
        result.append(row_list)
    return result
    
# Feed our two-dimensional list into Pandas.
df = pandas.DataFrame(xml_to_list(root))
print(df)




#
#
## PYTHON open( )
# Let's open the poem.txt file, create a file object, and print out the
# file text line by line.
# Note the poem.txt tab above.
with open('poem.txt') as poem_file:
    text = poem_file.readlines()
    print("This file is {} lines long".format(len(text)))
    for line in text:
        print(line)

# Try loading and printing the purchases.csv file line by line just
# just like we did for poem.txt.




