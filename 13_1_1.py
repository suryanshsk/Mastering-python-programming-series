import os  
# Def fxn to rename files
def rename_files(directory, prefix):
    # Get all files in folder
    files = os.listdir(directory)  
    count = 0  # counter from 0

    for file in files:  # Loop through each file
        #new file name
        new_name = f"{prefix}_{count}"  
        # full path of the old file
        old_path = os.path.join(directory, file)
        #full path of the new file
        new_path = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed '{file}' to '{new_name}'")  
        count += 1  # Increase the counter by 1

# Call the function with your folder path and prefix
rename_files(r"C:\Users\admin\OneDrive - MSFT\Rename Automation", "file")
