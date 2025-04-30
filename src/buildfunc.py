import os, shutil
import logging
from parse import *

# Create a logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Create a file handler that appends to the log file
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = root_dir + "/build.log"
file_handler = logging.FileHandler(log_file, mode='a')
file_handler.setLevel(logging.DEBUG)

# Define the logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

def delete_dest_files(path):
    #delete the contents of the dest directory
    for filename in os.listdir(path):
        file_path = path + filename
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
                rel_path = os.path.relpath(file_path)
                logger.info(f"{file_path} directory was deleted")
            else:
                os.remove(file_path)
                logger.info(f"{file_path} file was deleted")

def list_files_recursive(path):
    files = []
    for file in os.listdir(path):
        file_path = path + file
        if os.path.isfile(file_path):
            files.append(file_path)
        elif os.path.isdir(file_path):
            files.extend(list_files_recursive(file_path+"/"))
    return files

def copy_file_to(file_path,dest_file_path):
    os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
    shutil.copy(file_path,dest_file_path)
    logger.info(f"{file_path} was copied to directory {dest_file_path}")

def copy_static_to_public():
    #folder paths
    source = "/static/"
    dest = "/public/"
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    source_path = root_dir+source
    dest_path = root_dir+dest

    #empty/delete all files in destination folder
    delete_dest_files(dest_path)

    #list all files in source folder
    source_files = list_files_recursive(source_path)

    #copy each file
    for file in source_files:
        rel_path = os.path.relpath(file,source_path)
        dest_file = os.path.join(dest_path,rel_path)
        copy_file_to(file,dest_file)

def read_file_to_text(from_path):
    f = open(from_path)
    text = f.read()
    f.close()
    return text

def write_text_to_file(file, dest_path):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path,"w") as f:
        f.write(file)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    #read the markdown file and store contents in a variable
    md = read_file_to_text(from_path)
    template = read_file_to_text(template_path)

    #convert markdown to html and extract h1 title
    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    #Replace title and content in the template string
    template = template.replace("{{ Title }}",title)
    template = template.replace("{{ Content }}",html)

    write_text_to_file(template,dest_path)


def list_md_files_recursive(path):
    md_files = []
    for file in os.listdir(path):
        file_path = path + file
        if os.path.isfile(file_path):
            if os.path.splitext(file)[-1].lower() == ".md":
                md_files.append(file_path)
        elif os.path.isdir(file_path):
            md_files.extend(list_files_recursive(file_path+"/"))
    return md_files

def generate_page_recursive(dir_path_content,template_path, dest_dir_path):
    #get a list of paths of all md files
    md_files = list_md_files_recursive(dir_path_content)

    #generate a html page for each file in md_files
    for file in md_files:
        #new filename
        filename = os.path.split(file)[1]
        new_file = os.path.splitext(filename)[0] + ".html"

        #rel folder structure minus root and filename. if in root, relpath returns "." -> change to empty string
        rel_path = os.path.relpath(os.path.dirname(file),dir_path_content)
        if rel_path == ".":
            rel_path = ""
        from_path = file

        #dest path using dest folder, rel folder structure and new filename
        dest_path = os.path.join(dest_dir_path,rel_path,new_file)
        generate_page(from_path, template_path, dest_path)
