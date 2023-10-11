import configparser
import os


class DefaultConfigKeys:
    DATA_SHEET_NAME = 'data_sheet_name'
    CLIENT_FIELD_NAME = 'client_field_name'
    FONT_SIZE = 'font_size'


DEFAULT_SECTION = 'Default'
CONFIG_FILE_NAME = 'config.cfg'
DEFAULT_CONFIG = {
    DefaultConfigKeys.DATA_SHEET_NAME: 'Python Data',
    DefaultConfigKeys.CLIENT_FIELD_NAME: 'clientname1_field',
    DefaultConfigKeys.FONT_SIZE: 8
}


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        if not os.path.exists(CONFIG_FILE_NAME):
            self.CreateDefaultConfig()
        self.config.read(CONFIG_FILE_NAME)
        self.VerifyConfigFile()

    def CreateDefaultConfig(self):
        self.config['Default'] = DEFAULT_CONFIG
        self.SaveConfigFile()

    def SaveConfigFile(self):
        with open(CONFIG_FILE_NAME, 'w') as configfile:
            self.config.write(configfile)

    def VerifyConfigFile(self):
        valid_config = True
        if self.config.has_section(DEFAULT_SECTION):
            for key in DEFAULT_CONFIG:
                if not self.config.has_option(DEFAULT_SECTION, key):
                    # populate the config with the option and default value if not present
                    self.config[DEFAULT_SECTION][key] = str(DEFAULT_CONFIG[key])
                    valid_config = False
        else:
            self.CreateDefaultConfig()  # re-create the entire config if the section is wrong
        
        if not valid_config:
            self.SaveConfigFile()  # Needed to make changed to config file, save those changes

    def GetConfigValue(self, value: str):
        return self.config.get('Default', value)
