#!/usr/bin/bash
if [ $UID != 0 ]; then
	echo "Insufficient Priviledges"
	echo "please run as root using sudo or other means"
	echo -e "\n fakeroot wont work boo boo bear"
	exit
fi

install_all() {
	/usr/bin/python install.py all
}

driver_help() {
	echo -e "unknown tag $2 \n"
	cat ./drivers.sh.help
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
	"-u") /usr/bin/python uninstall.py uninstall
	;;
	"--uninstall") /usr/bin/python install.py uninstall
	;;
	"-h") driver_help
	;;
	"--help") driver_help
	;;
	*) driver_help $2;
	exit
	;;
esac
