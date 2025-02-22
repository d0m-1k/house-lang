all: clean build-bin

build-bin:
	clear
	pyinstaller --onefile -n hlang src/*.py
	cp dist/hlang ./hlang

clean:
	rm build dist hlang.spec -r
	echo "cleanning..."
	clear

install:
	cp dist/hlang ~/../usr/bin/hlang
	chmod +x ~/../usr/bin/hlang
	echo "Done. Use 'hlang'"
