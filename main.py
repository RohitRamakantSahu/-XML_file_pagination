import requests
import xml.etree.ElementTree as ET

def parse_xml_feed(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        xml_content = response.content

        root = ET.fromstring(xml_content)
        image_urls = []

        # <image><url> pattern
        for image_tag in root.findall(".//image"):
            url_tag = image_tag.find("url")
            if url_tag is not None and url_tag.text:
                image_urls.append(url_tag.text.strip())

        # <item><image><url> pattern
        for item in root.findall(".//item"):
            image = item.find("image")
            if image is not None:
                url = image.find("url")
                if url is not None and url.text:
                    image_urls.append(url.text.strip())

        return image_urls
    except Exception as e:
        raise RuntimeError(f"Error: {str(e)}") 