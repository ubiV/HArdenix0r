import utils.SystemDetector as SysDec
import json

gap = True

import os
SysInfo = SysDec.getSystemInfo()

print(SysInfo.version, SysInfo.type)

def getCompatibleCommand(c):
    #concat all elements and check if my cuirrent major version is in string
    for cV in c['comp']:
        "".join(cV['version'])
    #blah blabh blah FIXME
    return c['comp'][0]


def executeCommand(command):
    return os.system(command)
def executeRemediation(node, resp):
    if(node['response']['format'] == "text"):
        if(resp != node['response']['text']):
            return "Remediation Executed:", executeCommand(node['remediation'])
        else:
            return "No remediation needed"
    if (node['response']['format'] == "json"):
        print("text")
    print(node)


with open(SysInfo.commandFilePath) as json_file:
    data = json.load(json_file)
    for c in data['commands']:
        command = getCompatibleCommand(c)
        print("CHECKING: ",c['desc'])
        resp = (executeCommand(command['command']))
        executeRemediation(c, resp)


