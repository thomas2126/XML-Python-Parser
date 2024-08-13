import json
import xml.etree.ElementTree as ET

# Register the namespace to handle XML namespaces
namespaces = {'hl7': 'urn:hl7-org:v3', 'sdtc': 'urn:hl7-org:sdtc'}

def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    return {child.tag.split('}')[-1]: xml_to_dict(child) for child in element}

def parse_record_target(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    record_target_dict = xml_to_dict(root.find('hl7:recordTarget', namespaces))
    record_target_json = json.dumps(record_target_dict)
    return record_target_json

