> Wildcard also called globbing allows us to select filenames
based on patterns of characters:

| Wildcard | Meaning |
| :------- | :------ |
| *	   | Matches any character |
| ?	   | Matches any single character |
| [characters]	   | Matches any character that is a member of the set characters |
| [!characters]    | Matches any character that is not a member of the set characters |
|  [[:class:]]	   | Matches any character that is a member of the specified class |


|  Character class | Meaning |
| :------- | :------ |
| [:alnum:]| Matches any alphanumeric character |
| [:alpha:]| Matches any alphabetic character |
| [:digit:]| Matches any numeral |
| [:lower:]| Matches any lowercase letter |
| [:upper:]| Matches any uppercase letter |


|  Pattern | Matches |
| :------- | :------ |
| *	   | All Files |
| g*	   | Any file beginning with "g"|
| b*.text  | Any file beginning with "b" followe by any characters and ending with "txt" |
| Data???  | Any character beginning with "Data" followed by exactly three characters |
| [abc]*   | Any file beginning with either an "a", "b", "c" |
| BACKUP.[0-9] [0-9] [0-9]| Any file beginning with "BACKUP" followed by exactly three numerals |
| [[:upper:]] | Any file beginning with an uppercase letter |
| [[:digit:]] | Any file not beginning with a numeral |
| [[:lower:]123] | Any file ending with a lowercase letter or the numerals "1", "2", "3" |
