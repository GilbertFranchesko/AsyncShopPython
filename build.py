"""
Build file for gShop Microservices and Gateway
Author: Vlad Halaburda
Realese: 0.01a
"""

import argparse
from builder.microservice import Microservice

CONFIG = None

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--service", type=str, help="Select a service name")
parser.add_argument("-c", "--check", type=str, help="Check the status")
parser.add_argument("-a", "--add", type=str, help="Add service")
parser.add_argument("-g", "--generate", type=str, help="Generate the proto files by microservice")
parser.add_argument("-d", "--depends", type=str, help="Select the dependinces from another microservice.")

parser.add_argument("-l", "--list", type=str, help="List of services")
parser.add_argument("--init", type=str, help="Init the exists microservices")
parser.add_argument("--run", type=str, help="Start the microservice")
parser.add_argument("--stop", type=str, help="Stop the microservice")


args = parser.parse_args()

generate_command = args.generate
add_service_command = args.add
services_list = args.list

init_services = args.init

if init_services is not None:
	Microservice.init_service(init_services)

if args.run is not None:
	Microservice(args.run).run()

if add_service_command is not None:
	Microservice.create(add_service_command)

if args.stop is not None:
	Microservice(args.stop).stop()

if args.check:
	service_name = args.check
	service = Microservice(service_name)
	service.info()
	