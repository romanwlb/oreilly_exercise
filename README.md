# Hello, team!
Thank you for finding the time to look at my humble solution! In order to run it locally, please use the following commands:

    docker run --rm -p 5432:5432 --name ormdb -e POSTGRES_PASSWORD=hunter2 -e POSTGRES_USER=oreilly -d registry.hub.docker.com/caedus41/oreilly-cloud-engineer-postgres
    
    docker run --rm -p 5051:5051 --name oreilly-api -d registry.hub.docker.com/romansage/oreilly_take_home

You should be able to access the search API in your web browser at http://127.0.0.1:5051/

## NB:

Since I was using my macbook to work on the task, I ran into an issue with using the docker network.

Per https://docs.docker.com/network/host/:

> "The host networking driver only works on Linux hosts, and is not supported on Docker Desktop for Mac, Docker Desktop for Windows, or Docker EE for Windows Server."

See more: https://github.com/docker/for-mac/issues/6185

Having said that, I had to hardcode the docker virtual network address here instead of using the host network to make it work:

https://github.com/romanwlb/oreilly_exercise/blob/main/oreilly_api/take_home.py#L5

My solution should work on OS X but let me know if you are using Linux and I will look into making it work.

## Application Design considerations.

In order to spend no more than 3-4 hours on a basic working solution for a proof of concept I had to take a few shortcuts, let's just say it's a very dev version of the app that is aspiring to go to a QA environment some day ;)

In order to make it production ready we would need to:

-Use a dedicated WSGI server, since we are runnng our code in our own k8s cluster we need to use one of the self hosted solutions: https://flask.palletsprojects.com/en/2.2.x/deploying/#self-hosted-options
-Postgres password should be a k8s secret passed to the app as an env variable
-Some of the books are missing ISBNs, we need to contact our sales department and add them to the database
-Consider checking the length of our searches before their execution (e.g. if a search string is shorter than 3 symbols - return an error)
-Consider some caching solutions for the db requests

Infrastructure considerations:
-Use a hosted k8s solution such as GKE or AKS
-Put the search API app behind a load balancer
-Use SSL
-If we want to run postgres in k8s we should deploy it as a stateful set with persistent volumes in order to make sure we don't lose the data

## How to use:
Our API currently supports the following GET requests (we do not needs other kinds of HTTP requests for this task):

/orapi/_all - fetch all of the books in our catalog
/orapi/search/_isbn/$ISBN - search by isbn
/orapi/search/_authors/$AUTHOR - search by author (not case sensitive)
/orapi/search/_books/$KEYWORD - search by a keyword in a books's title (not case sensitive)

