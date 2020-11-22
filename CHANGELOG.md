v0.0.6
 - Start of rewrite and polish
 - Started working on the warframe command shit

v0.0.5
 - Split ``info`` cog into ``user`` and ``server`` cogs
 - some other shit

v0.0.4.7
 - Added ``listToSpacedString`` to ``gen functions``
 - Started framework for ``delete_inv``, ``create_tenp_inv`` and worked further on ``create_inv`` to setup some dynamic input and processing
 - probably other shit too idk im high
 - Also set up some shit to get heroku going

v0.0.4.6
 - Started working on the invite manager class
 - Added the check invite function
 - Created the ``InvitePolish`` which wil be used to clean and return information to be posted to the front end
 - probably some other shit was added

v0.0.4.5.5
 - Some more general shit which i dont remember

v0.0.4.5
 - Completed info command convertion to use the new ``Guild`` and ``embedC`` class
 - Refactored the ``user permsin`` command to something which works

v0.0.4.4.5
 - Started intigrating cardinal into the bot
 - Intigrating other older bot stuff of mine into this bot
 - General file movements and cleanup
 - Added the ``version`` file
 - "Setup" the pyinstaller code (unsure if 100% correct)
 - Added the coinflip command and started the rock paper scissors command

v0.0.4.3
 - Converted ``server detailedinfo`` and ``server roles`` to use the new embed builder and ``Guild`` class
 - Shifted some of the properties to be defined during class ``__init_`` for an easier load
 - Added some more stuff to the ``Guild`` class
 - Removed ``credits.md``

v0.0.4.2
 - Fixed the ``say`` command, 100% functional
 - Created the ``Guild`` class as a wrapper for some additional stuff
 - Converted ``server info`` to use the new embed builder and ``Guild`` class

v0.0.4.1
 - Fixed ``requirements.txt``
 - Added the ``say`` command in the ``misc`` cog (not 100% functional)
 - Fixed the ``info`` command to work with the ``data.json`` change

v0.0.3
 - Renamed Project to Green Bot
 - Added the AM/PM denoter for the ``12h-timestamp`` in Date
 - Completed the basic setup for the ``Date`` class
 - Added the ``Embed`` Class and made some basic functionality w it
 - Converted the ``User Info`` command to use the new ``Date`` and ``Embed`` class when making the embed to send
 - Fixed the issue with ``cardinal.is_owners`` now it works

v0.0.2
 - Started work on the Date Class
 - Added the beginnings of the math cog
 - Merged the core and devtools cog into botManager
 - Created the Misc cog

v0.0.1
 - Initial stuff