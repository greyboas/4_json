# Prettify JSON

Данный проект созадн для приведения файла JSON в читабильный вид, при запуске скрипта необходимо указать путь к файлу, который надо вывестив читаемом виде

# Quickstart

Необходимо вызвать скрипт с указанием пути к файлу, который необходимо распарсить.

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "AdmArea": "Западный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Кунцево",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "09:30-22:30"
                },

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
