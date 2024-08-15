import xml.etree.ElementTree as ET

# Define namespaces
namespaces = {'hl7': 'urn:hl7-org:v3', 'sdtc': 'urn:hl7-org:sdtc'}

# Load and parse the XML file
tree = ET.parse('./CCD-Files/Inpatient-Summery-CCD-Sample.xml')
root = tree.getroot()

# Find and print all section templateIds
for section in root.findall('.//hl7:section', namespaces):
    template_id = section.find('hl7:templateId', namespaces)
    if template_id is not None:
        section_name = section.find('hl7:code', namespaces)
        section_display_name = section_name.get('displayName') if section_name is not None else "Unknown Section"
        print(f"Section: {section_display_name}, templateId: {template_id.get('root')}")

