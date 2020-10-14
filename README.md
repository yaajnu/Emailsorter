# Emailsorter
This is a python program that sorts emails according to a specific keyword in the Subject("Thank you for applying")


It's a pretty simple program that uses Imaplib and email libraries to connect to your gmail id and then scrapes the emails in your inbox and searches for subject with matching keyword and then sorts these matched emails with a 'JOBS ' label on gmail

Also for some gmail ids one may have to allow access to less secure apps in the setting if it gives an error(I faced an issue with one of my emails but the other works fine).This can be solved by using oauth2 token but that's a more lengthier process for the user

