#!/usr/bin/bash
install_all() {
	echo "test"
}
driver_help() {
	. ./driver_help.sh
}
interactive() {
	/usr/bin/python interactive.py
}
case $1 in
	"-a") install_all
	;;
	"--all") install_all
	;;
	"-in") interactive
	;;
	"--interactive") interactive
	;;
	"-i") /usr/bin/python install.py $2
	;;
	"--install") /usr/bin/python install.py $2
	;;
	"-h") driver_help
	;;
	"--help") driver_help
	;;
	*) driver_help;
	exit
	;;
esac
