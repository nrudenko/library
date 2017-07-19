# library
Sample of python API project implementation 

## Database documentation

![Datagram](https://github.com/nrudenko/library/blob/master/docs/library-diagram.png)

## API documentation
[Library swagger referrence](https://app.swaggerhub.com/apis/nrudenko/library/1.0.0)


## Short description

The application contains two part:
*  admin_panel `http://host/admin/` - for adding test data (users, books, rents)
*  books get endpoint `http://host/api?name=John` - endpoint for getting books with same price as second rented book by user

  
## Usage
You can start project locally:
$ `docker-composer up`
In this case parts are available:
* http://localhost/admin
* http://localhost/api/book?name=John

Or use already deployed to Google Cloud instance:

* http://104.154.193.227/admin
* http://104.154.193.227/api/book?name=John
