# Web-dash
Browser-based dashboard that dynamically reloads content via web requests

## TODO list
[ ] build basic ui
[ ] build api to handle link requests
[ ] figure out how to get server to force client refresh
[ ] think about auth potential (local, so low priority)
[ ] setup redis for persistence
[ ] dockerize app

## Main dashboard
The vision that sparked this project is a local web server that displays
multiple third-party assets neatly on a sinlge page.

### Example use case
You're tracking several stocks during a crisis (COVID-19), and you want a HUD
that contains all of the real-time tickers. Pull the URLs for each individual
ticker and push them to the web-dash update API endpoint. The home page now
displays all the charts in a single dashboard.

## Alternative dashboards
1. ToDo list/goals page
  - Several user stories here, short term goals (organize work day tasks) or
longer term goals (reading list, graduation requirements, etc.)
