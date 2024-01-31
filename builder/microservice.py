import os
from pathlib import Path

from builder.configuration import Configuration
from .arch import open_microservice, check_microservice, create_microservice
from .docker import run_via_docker, stop_via_docker
import typing as t



class Microservice:

    def __init__(self, name: str):
        
        main_path, protos, stubs = open_microservice(name)
        compose_file, executable_file, makefile = check_microservice(main_path, protos, stubs)

        self.__name = name
        self.__main_path = main_path

        self.__protos = protos
        self.__stubs = stubs
        
        self.__compose_file = compose_file
        self.__executable_file = executable_file
        self.__makefile = makefile

        self.__log_dir = self.__main_path / "logs"

        self.__init_logs()

    @property
    def name(self):
        return self.__name
    

    @property
    def main_path(self):
        return self.__main_path
    
    @property
    def protos(self):
        return self.__protos
    
    @property
    def stubs(self):
        return self.__stubs
    
    @property
    def compose_file(self):
        return self.__compose_file
    
    @property
    def executable_file(self):
        return self.__executable_file
    
    @property
    def makefile(self):
        return self.__makefile

    def info(self):
        print("Microservice {}".format(self.name))
        print("Main path: {}".format(self.main_path))
        print("Protos path: {}".format(self.protos))
        print("Stubs path: {}".format(self.stubs))
        print("Compose file path: {}".format(self.compose_file))
        print("Executable file path: {}".format(self.executable_file))
        print("Makefile path: {}".format(self.makefile))
    
    def __init_logs(self):
        if not self.__log_dir.exists():
            self.__log_dir.mkdir()

    def run(self):
        run_via_docker(self.compose_file, self.__log_dir)
    
    def stop(self):
        stop_via_docker(self.compose_file, self.__log_dir)

    @staticmethod
    def create(name: str):
        main_path, protos, stubs = create_microservice(name)


    @staticmethod
    def init_service(p):
        if Configuration.check():
            print("You already have a init file!")
            exit()

        p = Path(p)
        sub_dirs = next(os.walk(p))[1]
        for dir in sub_dirs:
            if "." in dir or "copy" in dir:
                continue
            same_path = p / dir
            if same_path.is_dir():
                print("Init service ", same_path)
                same_microservice = Microservice(dir)
                if same_microservice.main_path == same_path:
                    print("[{}] Init successfully!\n".format(dir))