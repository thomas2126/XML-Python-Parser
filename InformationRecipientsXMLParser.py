import json
import xml.etree.ElementTree as ET

# Register the namespace to handle XML namespaces
namespaces = {'hl7': 'urn:hl7-org:v3', 'sdtc': 'urn:hl7-org:sdtc'}

def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    return {child.tag.split('}')[-1]: xml_to_dict(child) for child in element}

def parse_information_recipients(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    information_recipients_dict = [xml_to_dict(recipient) for recipient in root.findall('hl7:informationRecipient', namespaces)]
    information_recipients_json = json.dumps(information_recipients_dict)
    return information_recipients_json