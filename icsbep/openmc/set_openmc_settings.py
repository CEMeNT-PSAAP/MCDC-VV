import os
import xml.etree.ElementTree as ET

def update_settings_xml(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Update values in settings.xml
        for elem in root.findall("batches"):
            elem.text = "200"
        for elem in root.findall("inactive"):
            elem.text = "20"
        for elem in root.findall("particles"):
            elem.text = "10000"
        
        # Write back changes
        tree.write(xml_file, encoding="utf-8", xml_declaration=True)
        print(f"Updated: {xml_file}")
    except Exception as e:
        print(f"Error updating {xml_file}: {e}")

def find_and_update_settings(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == "settings.xml":
                xml_path = os.path.join(dirpath, filename)
                update_settings_xml(xml_path)

root_directory = os.getcwd()  # Start search from current directory
find_and_update_settings(root_directory)