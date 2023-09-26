# datasci_4_web_viz
HHA 507 assignment 4

# R's Shiny Visualization:

deployed shinyapps link: <https://joyc3lin.shinyapps.io/project/>

# Reflections:

**Challenges:** 

**_shiny_r:_** 

+ ran into error messages when deploying app from posit to shinyapps with: <code>rsconnect::deployApp('/cloud/project/cdc.R')</code> that was given by shinyapps. It ran with <code>rsconnect::deployApp( server = 'shinyapps.io')</code>. 

+ Running <code>shiny::runApp()</code> returned _App dir must contain either app.R or server.R._. It worked once the file name was changed to app.R. 

**_shiny_python:_** 

+ ran into an issue with pushing changes onto repo because I made a change to the README.md file on github. Solved it with git pull repo-link. 

**Insights:** 

The basic format of the codes for all three were similar, it was mainly the syntax that made them different from each other. 
