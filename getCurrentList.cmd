set this_date=%date%
set this_time=%time%

echo datetime:  %this_date% %this_time%>> results.log
qbt torrent list --username jgarza --password decay9788 --url http://localhost:8080 --verbose >> results.log