from pathlib import Path
import os
import shutil
from time import sleep

from builder import DEFINED_DIR_OF_SERVICE, \
                        STANDART_COMPOSE_FILE, \
                        STANDART_DATABASE_CONNECTION, \
                        STANDART_DIR_OF_SERVICES, \
                        STANDART_DOCKER_FILE, \
                        STANDART_EXECFILE_GATEWAY, \
                        STANDART_EXECUTABLE_FILE, \
                        STANDART_MAKEFILE, \
                        STANDART_REQUIREMENTS_FILE

def checking_compose_file(main: Path) -> Path:
    print("[0] Checking by compose file .....")
    compose_file = main / STANDART_COMPOSE_FILE
    if not compose_file.exists():
        print("[warning][NF-03] the compose file is not defined.")
        sleep(1.1)
        exit()
    return compose_file


def __checking_main_file(main: Path) -> Path:
    print("[1] Check the executable file...")
    executable_file = main / STANDART_EXECFILE_GATEWAY
    if not executable_file.exists():
        print("[ERROR] exec file for gateway not found.")
        exit()
    
    return executable_file

def open_gateway(api_gateway_path: Path):
    compose_file = checking_compose_file(api_gateway_path)
    exec_file = __checking_main_file(api_gateway_path)
        
    
def open_microservice(name: str) -> tuple[Path, Path, Path]:
    p = Path(name)

    main_path = STANDART_DIR_OF_SERVICES / p
    if not main_path.exists():
        print("[invalid][NF-00] the service is not defined.")
        exit()

    protos_path = STANDART_DIR_OF_SERVICES / p / "protos"
    if not protos_path.exists():
        print("[invalid][NF-01] the microservice generated with errors.")
                
    stubs_path = p / "stubs"
    if stubs_path.exists():
        print("[invalid][NF-02] the microservice generated with errors.")

    return (main_path, protos_path, stubs_path)



def check_microservice(main: Path, protos: Path, stubs: Path):
    print("[0] Checking by compose file .....")
    compose_file = main / STANDART_COMPOSE_FILE
    if not compose_file.exists():
        print("[warning][NF-03] the compose file is not defined.")
        compose_file = Path()
        sleep(1.1)
    
    print("[1] Checking by executable file .....")
    executable_file = main / STANDART_EXECUTABLE_FILE
    if not executable_file.exists():
        print("[invalid][NF-04] the executable file not found.")
        executable_file = Path()
        exit()

    print("[2] Checking by Makefile .....")
    makefile = main / STANDART_MAKEFILE
    if not makefile.exists():
        print("[invalid][NF-05] the Makefile not found.")
        makefile = Path()
        exit()
    return compose_file, executable_file, makefile


def stub_names(service_name: str) -> tuple[str, str, str]:
    return (
            f"{service_name.lower()}_pb2_grpc.py",
            f"{service_name.lower()}_pb2.py",
            f"{service_name.lower()}_pb2.pyi"
        )


def create_microservice(service_name: str):
    p = Path(DEFINED_DIR_OF_SERVICE)
    if not p.is_dir() and not p.exists():
        print("systemerror")
        exit()
    
    path_to_create = Path(STANDART_DIR_OF_SERVICES)
    create_dir_of_new_service = path_to_create / service_name
    create_dir_of_new_service.mkdir()
    shutil.copy(p / STANDART_COMPOSE_FILE, create_dir_of_new_service)
    shutil.copy(p / STANDART_EXECUTABLE_FILE, create_dir_of_new_service)
    shutil.copy(p / STANDART_MAKEFILE, create_dir_of_new_service)
    shutil.copy(p / STANDART_DATABASE_CONNECTION, create_dir_of_new_service)
    shutil.copy(p / STANDART_REQUIREMENTS_FILE, create_dir_of_new_service)
    shutil.copy(p / STANDART_DOCKER_FILE, create_dir_of_new_service)

    protos_dir = create_dir_of_new_service / "protos"
    protos_dir.mkdir()
    stubs_dir = create_dir_of_new_service / "stubs"
    stubs_dir.mkdir()

    shutil.copy(p / "protos" / "example.proto", protos_dir)
    return create_dir_of_new_service, protos_dir, stubs_dir
    
def set_depends(depends, protos_dir):
    print("[] getting the stubs folder from depends service...")
    print(f"[Depends] get the dependinces {depends}...")
    p = Path(STANDART_DIR_OF_SERVICES)

    depends_microservice_name = depends
    main, protos, stubs_depends = open_microservice(depends_microservice_name)
    all_protos_file = protos / f"{depends_microservice_name.lower()}.proto"
    shutil.copy(all_protos_file, protos_dir)

    print(f"[Depends] from {depends_microservice_name} successfully! ")