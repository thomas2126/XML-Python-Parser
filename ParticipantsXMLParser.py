import json
import xml.etree.ElementTree as ET

# Register the namespace to handle XML namespaces
namespaces = {'hl7': 'urn:hl7-org:v3', 'sdtc': 'urn:hl7-org:sdtc'}

def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    return {child.tag.split('}')[-1]: xml_to_dict(child) for child in element}

def parse_participants(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    participants_dict = [xml_to_dict(participant) for participant in root.findall('hl7:participant', namespaces)]
    participants_json = json.dumps(participants_dict)
    return participants_json
