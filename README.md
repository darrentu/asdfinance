# asdfinance

asdfinance is a play on words using "asdf" and "finance". We came up with the idea when we were brainstorming cool ways to use Corsair's LED keyboard in our hack. We decided that the keyboard could be used beyond it's typical realm of gaming to help visualize financial information for users.

The keyboard LED serves as a display for multiple dynamic graphs, each corresponding to data presented in the web interface. Though this is a demo, the web interface allows the user to set their budget and view multiple breakdowns of that information in their browser. The web interface is meant to pair with the keyboard display as a control panel and launching mechanism.

The keyboard is an extension of the web interface demo we built, but also a totally new way to view financial data. Since the keyboard is always being interfaced with, it forces the user to constantly engage with the information being displayed to them. The user can manipulate their keyboard to display the visual data they want, then simply close the demo and it will persist. 

In this sense, the keyboard becomes a totally new mode of delivering information for the user. This is particularly useful for people who are bad at budgeting and need constant reminders, especially because these people are precisely those who are more likely to get discouraged and stop checking their budgeting software in the first place!

Marko Fejzo worked on backend, creating the server in python for communication with the web interface and for templating user data to be displayable on the keyboard. Monica Black worked with the Cue SDK to interface with the keyboard. David Woldenberg developed the front end and worked with multiple javascript frammeworks to communicate with the server. He also wrote this dope README with some help from Marko. Darren Tu worked on both the back end and the front end, writing code for the python server and the implementation of the javascript frameworks. The frameworks and libraries that we used for this project included socketio, angularjs, jquery, flask, chartjs, Intuit Mint API, and Cue SDK.
