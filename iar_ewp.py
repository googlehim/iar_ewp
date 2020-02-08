#!/usr/local/python
import os
import sys
from xml.dom.minidom import Document

class myfile:
    def __init__(self):
        self.name = ""

filter = [".c",".h"]
xml = "tree.xml"
doc = Document()
filecnts = 0

def search(folder, group):
    folders = os.listdir(folder)

    for name in folders:
        curname = os.path.join(folder, name)
        isfile = os.path.isfile(curname)
        if isfile:
            ext = os.path.splitext(curname)[1]
            count = filter.count(ext)
            global filecnts
            filecnts += count
            if count>0:
                file = doc.createElement("file")
                group.appendChild(file)

                name = doc.createElement("name")
                file.appendChild(name)
                namevalue = doc.createTextNode(os.path.abspath(curname))
                name.appendChild(namevalue)
        else:
            newgroup = doc.createElement("group")
            group.appendChild(newgroup)

            name = doc.createElement("name")
            newgroup.appendChild(name)

            namevalue = doc.createTextNode(os.path.basename(curname))
            name.appendChild(namevalue)

            search(curname, newgroup)

    return None



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error! Usage: generateDir.py path')
        sys.exit(0)
    else:
        folder = sys.argv[1]
            
    #folder = os.getcwd()
    root = doc.createElement("root")
    doc.appendChild(root)

    search(folder, root)
    #print(doc.toprettyxml(indent="  "))
    print('Done! Total %d files' %filecnts)
    f = open(xml, 'w')
    f.write(doc.toprettyxml(indent="  "))
    f.close()
