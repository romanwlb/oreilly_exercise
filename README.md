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

Having said that, I had to hardcode the docker virtual network address here instead of using the host network in order to make the API app be able to connect to PSQL and remain to be accessible at localhost:5051 at the same time:

https://github.com/romanwlb/oreilly_exercise/blob/main/oreilly_api/take_home.py#L5

My solution should work on OS X with default docker network configuration but let me know if you are using Linux and I will look into making it work.

## Application Design considerations.

To spend no more than 3-4 hours on a basic working solution for a proof of concept I had to take a few shortcuts, let's just say it's a very dev version of the app that is aspiring to go to a QA environment some day ;)

### In order to make it production ready we would need to:

-Use a dedicated WSGI server, since we are runnng our code in our own k8s cluster we need to use one of the self hosted solutions: https://flask.palletsprojects.com/en/2.2.x/deploying/#self-hosted-options

-Postgres password should be a k8s secret passed to the app as an env variable

-Some of the books are missing ISBNs, we need to contact our sales department and add them to the database

-Consider checking the length of our searches before their execution (e.g. if a search string is shorter than 3 symbols - return an error)

-Consider some caching solutions for the db requests


## Infrastructure considerations:

-Use a hosted k8s solution such as GKE or AKS

-Put the search API app behind a load balancer

-Use SSL

-If we want to run postgres in k8s we should deploy it as a stateful set with persistent volumes in order to make sure we don't lose the data

-Create k8s resource yamls and a deployment pipeline

## How to use:
Our API currently supports the following GET requests (we do not needs other kinds of HTTP requests for this task):

/orapi/_all - fetch all of the books in our catalog

/orapi/search/_isbn/$ISBN - search by isbn

/orapi/search/_authors/$AUTHOR - search by author (not case sensitive)

/orapi/search/_books/$KEYWORD - search by a keyword in a books's title (not case sensitive)

Example:

    curl http://127.0.0.1:5051/orapi/search/_authors/percival

    [[55,"The Complete Python and PostgreSQL Developer Course","Jose Salvatierra; Rob Percival","","<span><p>Build 9 projects and master two essential and modern technologies: Python and PostgreSQL</p><p><b>About This Video</b></p><ul><li>Gain comprehensive understanding of software and programming with Python</li><li>Create basic beginner-level applications to advanced engaging applications using Python</li></ul><p><b>In Detail</b></p><p>Ever wanted to learn one of the most popular programming languages on the planet? Why not learn two of the most popular at the same time?</p><p>Python and SQL are widely used by small to large technology companies thanks to their powerful, yet extremely flexible features. While Python is used in the industry for embedded software, web development, desktop applications, and mobile apps, PostgreSQL allows your applications to become even more powerful by storing, retrieving, and filtering through large datasets easily. This course is your one-stop-shop for everything Python and PostgreSQL. You'll advance from an absolute Python and PostgreSQL beginner to an experienced software developer.</p><p>Get ready to transform your world and become a super-confident app developer!</p><p><b>Who this book is for</b></p><p>If you\u2019re a complete beginner to programming and Python, this course will provides concise explanations with hands-on projects. Intermediate programmers will be able to fly through the first couple of sections and quickly learn about PostgreSQL and advanced Python concepts. This course is likely not for advanced programmers, although it has a lot of useful information that will serve as a reference!</p></span>"],[71,"The Complete Machine Learning Course with Python","Anthony NG; Rob Percival","","<span><p>Build a Portfolio of 12 Machine Learning Projects with Python, SVM, Regression, Unsupervised Machine Learning &amp; More!</p><p><b>About This Video</b></p><ul><li>Solve any problem in your business or job with powerful Machine Learning models</li><li>Go from zero to hero in Python, Seaborn, Matplotlib, Scikit-Learn, SVM, and unsupervised Machine Learning etc.</li></ul><p><b>In Detail</b></p><p>Do you ever want to be a data scientist and build Machine Learning projects that can solve real-life problems? If yes, then this course is perfect for you.</p><p>You will train machine learning algorithms to classify flowers, predict house price, identify handwritings or digits, identify staff that is most likely to leave prematurely, detect cancer cells and much more!</p><p>Inside the course, you'll learn how to:</p><ul><li>Set up a Python development environment correctly</li><li>Gain complete machine learning toolsets to tackle most real-world problems</li><li>Understand the various regression, classification and other ml algorithms performance metrics such as R-squared, MSE, accuracy, confusion matrix, prevision, recall, etc. and when to use them.</li><li>Combine multiple models with by bagging, boosting or stacking</li><li>Make use to unsupervised Machine Learning (ML) algorithms such as Hierarchical clustering, k-means clustering etc. to understand your data</li><li>Develop in Jupyter (IPython) notebook, Spyder and various IDE</li><li>Communicate visually and effectively with Matplotlib and Seaborn</li><li>Engineer new features to improve algorithm predictions</li><li>Make use of train/test, K-fold and Stratified K-fold cross-validation to select the correct model and predict model perform with unseen data</li><li>Use SVM for handwriting recognition, and classification problems in general</li><li>Use decision trees to predict staff attrition</li><li>Apply the association rule to retail shopping datasets</li><li>And much more!</li></ul><p>By the end of this course, you will have a Portfolio of 12 Machine Learning projects that will help you land your dream job or enable you to solve real-life problems in your business, job or personal life with Machine Learning algorithms.</p></span>"]]


