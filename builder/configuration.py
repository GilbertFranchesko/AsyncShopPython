from pathlib import Path
from time import sleep
import typing as t
import json

# from builder.microservice import Microservice


class Configuration:
    config_path = Path(".") / ".micro-conf"

    def __init__(self, 
            services_dir: t.Optional[Path],
            api_gateway_dir: t.Optional[Path],
            services: t.List[t.Optional[object]] = [],
            kernel_folder: Path = Path(".")):
        
        if services_dir is not None:
            self.__services_dir = services_dir

        if api_gateway_dir is not None:
            self.__api_gateway_dir = api_gateway_dir

        self.__kernel_folder = kernel_folder
        self.__services = services

    @property
    def api_gateway_dir(self):
        return self.__api_gateway_dir
    
    @property
    def services_list(self):
        return self.__services

    def save(self):
        conf_dict = {
            "services_dir": str(self.__services_dir),
            "api_gateway_dir": str(self.__api_gateway_dir)
        }

        if self.__kernel_folder.exists():
            with open(self.__kernel_folder / ".micro-conf", "w+") as f:
                f.write(json.dumps(conf_dict))

    def add_microservice(self, microservice: object):
        self.__services.append(microservice)

    @staticmethod
    def init():
        check_status = Configuration.check()
        if check_status:
            return Configuration.config_path.iterdir()

    @staticmethod
    def check() -> bool:
        config_path = Path(".") / ".micro-conf"
        return config_path.exists()

    def __repr__(self):
        return repr("Config["+str(self.__services_dir)+", "+str(self.__api_gateway_dir)+"]")
