Application Design considerations.

In order to spend no more than 3-4 hours on a basic working solution for a proof of concept I had to take a few shortcuts, let's just say it's a very dev version of the app that is aspiring to go to a QA environment some day ;)
In order to make it production ready we would need to:

-Use a dedicated WSGI server, since we are runnng our code in our own k8s cluster we need to use one of the self hosted solutions: https://flask.palletsprojects.com/en/2.2.x/deploying/#self-hosted-options
-Postgres password should be a k8s secret passed to the app as an env variable
-Some of the books are missing ISBNs, we need to contact our sales department and add them to the database
-Put the app behind a load balancer
-Use SSL
-Consider creating a Helm chart
-Configure a deployment pipeline 
-Consider checking the length of our searches before their execution (e.g. if a search string is shorter than 3 symbols - return an error)
-Consider some caching solutions for the db requests

Infrastructure considerations:
-Use a hosted k8s solution such as GKE or AKS

How to use:
Our API currently supports the following GET requests (we do not needs other kinds of HTTP requests for this task):

![Alt text](/screenshots/docker.jpeg?raw=true "Docker")