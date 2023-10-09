from pathlib import Path

def findTemplatePath(templatesPath):
        templatesPath = Path(templatesPath)
        if templatesPath.exists():
            return templatesPath
        if Path("../templates").exists():
            return Path("../templates")
        if Path("./templates").exists():
            return Path("./templates")
        
        return templatesPath

def findDataPath(DataPath):
        DataPath = Path(DataPath)
        if DataPath.exists():
            return DataPath
        if Path("../data").exists():
            return Path("../data")
        if Path("./data").exists():
            return Path("./data")
        
        return DataPath