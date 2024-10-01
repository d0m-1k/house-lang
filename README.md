# houseLang

## Синтаксис
### Команды
`var` - установить переменную\
`print` - вывод текста на экран\
`exit` - выход из программы
### Данные
`"hello"` - строка\
`10` - число
### Символы
`_` - Пробел ( )\
`&_` - Нижнее подчёркивание (\_)

## Примеры
### Hello, world
```
var text = "Hello,\_World!"
print text
```

## Сборка
### Linux
```
sudo apt install python python-pip make git -y
git clone https://github.com/d0m-1k/house-lang.git
cd house-lang
python3 -m pip install pyinstaller
make
```
### Windows
 * скачиваем python
 * устанавливаем python
 * скачиваем git
 * устанавливаем git
 * `git clone https://github.com/d0m-1k/house-lang.git`
 * `python -m pip install pyinstaller`
 * `pyinstaller --onefile -n hlang src/*.py`

теперь в папке dist есть `hlang` или `hlang.exe`
