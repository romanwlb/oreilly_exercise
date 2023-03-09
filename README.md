Hello!
Thank you for finding the time to look at my humble solution! In order to run it locally, please use the following commands:

docker run --rm -p 5432:5432 --name ormdb -e POSTGRES_PASSWORD=hunter2 -e POSTGRES_USER=oreilly -d registry.hub.docker.com/caedus41/oreilly-cloud-engineer-postgres

docker run --rm -p 5051:5051 --name oreilly-api -d registry.hub.docker.com/romansage/oreilly_take_home

You should be able to access the search API in your web browser at http://127.0.0.1:5051/


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

/orapi/_all - fetch all of the books in our catalog
/orapi/search/_isbn/ - search by isbn
/orapi/search/_authors/ - search by author
/orapi/search/_books/ - search by a keyword in a books's title
https://github.com/docker/for-mac/issues/6185