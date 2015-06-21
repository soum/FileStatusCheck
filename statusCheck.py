import os

def get_filepaths(directory):
    
    file_paths = []

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:

            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths

# Run the above function and store its results in a variable.   Users/soumghosh/Desktop
full_file_paths = get_filepaths("Users/soumghosh/Desktop/AutomationFileStatusCheck/FileStatus")

_content = []

for x in full_file_paths:
    with open(x, 'r') as content_file:
        content = content_file.read()
        _content.append(content)

        
str_content = ','.join(_content)
# str_content = ','.join([str(i) for i in _content])

print(str_content)
text_file = open("Users/soumghosh/Desktop/AutomationFileStatusCheck/Output.json", "w")
text_file.write('['+ str_content +']')
text_file.close()
        
