#!/usr/bin/env python3
"""A small command-line wrapper for Nmap."""

import argparse
import shutil
import subprocess
import sys


def main() -> int:
	parser = argparse.ArgumentParser(
		description="Scan a host with Nmap. Only scan systems you are authorized to test."
	)
	parser.add_argument("target", help="hostname, IP address, or CIDR network")
	parser.add_argument("-p", "--ports", help="ports to scan, e.g. 22,80,443 or 1-1024")
	parser.add_argument("-sV", "--service-version", action="store_true", help="detect service versions")
	parser.add_argument("-O", "--os-detection", action="store_true", help="attempt OS detection")
	parser.add_argument("-T", "--timing", choices="012345", help="Nmap timing template")
	args = parser.parse_args()

	if shutil.which("nmap") is None:
		print("Error: nmap is not installed or is not on PATH.", file=sys.stderr)
		return 1

	command = ["nmap"]
	if args.service_version:
		command.append("-sV")
	if args.os_detection:
		command.append("-O")
	if args.timing:
		command.append(f"-T{args.timing}")
	if args.ports:
		command.extend(["-p", args.ports])
	command.append(args.target)

	try:
		return subprocess.run(command, check=False).returncode
	except KeyboardInterrupt:
		print("\nScan interrupted.", file=sys.stderr)
		return 130
	except OSError as error:
		print(f"Error starting nmap: {error}", file=sys.stderr)
		return 1


if __name__ == "__main__":
	raise SystemExit(main())
