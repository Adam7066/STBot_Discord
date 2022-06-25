import json


class tool:
    def getSettingJson():
        with open('./setting.json', 'r', encoding='UTF-8') as f:
            settingJson = json.load(f)
        return settingJson

    def setSettingJson(settingJson):
        with open('./setting.json', 'w') as f:
            json.dump(settingJson, f, indent=4)
