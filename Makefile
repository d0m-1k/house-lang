all: clean build-bin

build-bin:
	clear
	pyinstaller --onefile -n hlang src/*.py
	cp dist/hlang ./hlang

clean:
	rm build dist hlang.spec -r
	echo "cleanning..."
	clear                                                                                                                                                              