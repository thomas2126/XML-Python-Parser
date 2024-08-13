import json
import xml.etree.ElementTree as ET

# Register the namespace to handle XML namespaces
namespaces = {'hl7': 'urn:hl7-org:v3', 'sdtc': 'urn:hl7-org:sdtc'}

def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    return {child.tag.split('}')[-1]: xml_to_dict(child) for child in element}

def parse_authors(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    authors_dict = [xml_to_dict(author) for author in root.findall('hl7:author', namespaces)]
    authors_json = json.dumps(authors_dict)
    return authors_json
