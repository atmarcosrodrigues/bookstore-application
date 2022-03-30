# BookStore Application Web Server

Web service application developed with AngularJS hosted in Google App Engine cloud structure.
### Used libraries, resources and plataforms:

- Google App Engine
- Google Cloud
- Python webapp2
- Python 2 NDB Client Library
- ReactJS



#### Google App Engine
pp Engine is a simple way to deploy applications that will automatically scale up and down according to load, collect logs, etc. https://cloud.google.com/appengine/

#### Python 2 NDB Client
The Google Datastore NDB Client Library allows App Engine Python apps to connect to Datastore. The NDB client library builds on the older DB Datastore library adding the following data store features:
The StructuredProperty class, which allows entities to have nested structure.
Integrated automatic caching, which typically gives fast and inexpensive reads via an in-context cache and Memcache.
Supports both asynchronous APIs for concurrent actions in addition to synchronous APIs.

## Application Details
## - Server
#### Api REST



| Rest | Service |
| ------ | ------ |
| / | Provides the user with the initial web interface of the application |
| /api | Provides the Documentation interface explaining in detail the use of the REST API |
 | /inserirLivro | Provides the POST functionality to insert books into the API server
 | /getLivros | Provides the GET functionality that returns the books registered in the API serer
 | /getLivro | Provides GET functionality that returns a specific book from an identifying key
 | /deleteLivro | Provides DELETE functionality to remove a book on the API server |
 | /updateLivro | Provides PUT functionality to update book attributes on API server |
 | /deleteLivros | Provides DELETE functionality to remove books on API server |
 | /postComentario | Provides POST functionality to post comments to API server |
 | /getCommentario | Provides the GET functionality that returns the comments registered in the API serer |
 | /postUsuario | Provides POST functionality to insert a new user into the API server |
 | /getUsuario | Provides the GET functionality that returns the data of a user registered in the serer through the identifying key |
 | /resetaSistema | Provides support and maintenance option to restart and clear server data |
  

## -Client
Web Application UI to use funcionalitys from REST API and bookstore manegment.



