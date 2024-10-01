all: build-bin clean

build-bin:
	clear
	pyinstaller --onefile -n hlang src/*.py
	cp dist/hlang ~/hlang
	chmod +x ~/hlang

clean:
	rm build dist hlang.spec -r
	echo "cleanning..."
	clear                                                                                                                                            