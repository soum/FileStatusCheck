import os

def get_filepaths(directory):
    
    file_paths = []

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:

            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths("c:/Users/soum/Desktop/python prototypes/fileStatus")

_content = []

for x in full_file_paths:
    with open(x, 'r') as content_file:
        content = content_file.read()
        _content.append(content)

        
str_content = ','.join(_content)
# str_content = ','.join([str(i) for i in _content])

print(str_content)
text_file = open("c:/Users/soum/Desktop/python prototypes/Output.json", "w")
text_file.write('['+ str_content +']')
text_file.close()
        
        
