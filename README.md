# unsubscribe_mass-mails
script for automatic unsubscribing from postfix log files

unsubscribe_mass-mails [![Python 3.4, 3.5, 3.6](https://img.shields.io/pypi/pyversions/3)
=================================================================================================================================================================================
**unsubscribe_mass-mails** – скрипт для автоматической отписки от массовой рассылки по лог файлам postfix пользователей, которым не доставлены письма.


```


Подготовка
------------
    $ grep "status=bounced" /var/log/mail.log | grep -o -P "to=<(.+?)>" | sort | uniq -c > /home/mail_bounced.txt

```

Установка
------------
    $ python3 unsubscribe_mass-mails.py