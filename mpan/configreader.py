import xml.etree.ElementTree


class ConfigReader:
    def __init__(self, filename):
        self.name = filename

    def read(self):
        self.categories = []
        e = xml.etree.ElementTree.parse(self.name)
        for category in e.iter(tag="category"):
            modules = []
            not_title = True
            for module in category.iter(tag="module"):
                mod_dict = {"widget": None}
                for elem in module.iter():
                    if elem.tag == "title" and not_title:
                        mod_dict["title"] = elem.text
                        not_title = False
                    if elem.tag != "module" and elem.tag != "title":
                        mod_dict[elem.tag] = elem.text
                modules.append(mod_dict)
                not_title = True
            icon = category.find("icon").text
            self.categories.append(
                {
                    "title": category.find("title").text,
                    "icon": icon,
                    "modules": modules,
                    "active": False,
                    "widget": None,
                }
            )
        return self.categories
