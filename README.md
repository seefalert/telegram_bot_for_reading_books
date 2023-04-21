# telegram_bot_for_reading_books
Telegram bot for reading books Currently in the functionality: 
-read a book with paginator
-create and delete bookmarks

The entry point to the program file 'bot_reader.py'.
'config.py' unpack '.env' with bot api key and admins ids.
'database.py' this is a pseudo db, which you need to hush up,
othetwise all bookmarks will fly off when you restart.
Fileters stored in 'filters.py' designed to filter callbacks into handlers.
All handlers for the main logic in 'user_handlers.py',
and for all other requsts in 'other_handlers.py'.
Keyboards for bookmarks and paginator in 'bookmarks_kb.py' and
'paginator_kb.py', respecively.
And in 'main_menu.py' commands like /start are created.
The 'lexicon.py' contains all the phrases that the bot says and
all the commands + description for the menu button in the form of a dictionary.
'file_handling.py' contains functions for preparing a book for
reading (breacks it into pages and collects it into a dictionary).
