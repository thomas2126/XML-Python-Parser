import json
import xml.etree.ElementTree as ET

# Register the namespace to handle XML namespaces
namespaces = {'hl7': 'urn:hl7-org:v3', 'sdtc': 'urn:hl7-org:sdtc'}

# Helper function to convert XML element to a dictionary
def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    return {child.tag.split('}')[-1]: xml_to_dict(child) for child in element}

def parse_clinical_document(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    clinical_document_dict = xml_to_dict(root)
    clinical_document_json = json.dumps(clinical_document_dict)
    return clinical_document_json
