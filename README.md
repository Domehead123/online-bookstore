# Online Book Store

An online book store where people can buy books, in the form of a download, or upload their books in document format for sale.

# UX

The site is for buyers and sellers, catering for all tastes in fiction. It would be another way for aspiring authors to get their works sales and attention.

Buyers visiting the site can browse the different book, sorting them by genre if they want. On the home page they will see the title, author, a brief description, the genre, price and an opening excerpt from the book. They see more of this excerpt if they click Read More, taking them to the Book Details page. Here they can buy the book or leave a comment on the book – but only if they log in. Payment is via Stripe. Once they have paid, they will be taken to a Downloads page, where they can download the book in a document format.

Sellers, if logged in, can upload a new book via a form, edit or delete it.

People can be both buyers and sellers, but people can’t edit/delete other people’s books. And sellers won’t see a link to buy their own book.

## Features.

### Existing Features

* Register/Log-in/see profile – via Accounts app
* Add, edit, delete or view details of books - via Books app and delete.js
* Filter books by genre via genre.js
* Search by book title via search app
* Add books to cart via cart app
* Purchase books via checkout app and stripe,js
* Download books via download app
* Comment on books via comment app

### Features Left to Implement
Better search facility so not just title search.

## Technologies Used

* [Python](https://www.python.org/download/releases/3.0/) - The is an app largely using Python3
* [Django](https://www.djangoproject.com/) - The app uses the Django framework – version 1.11
* [Javascript](https://www.javascript.com/)  - Used for DOM manipulation
* [JQuery](https://jquery.com/) - Used for DOM manipulation
* [Bootstrap](https://getbootstrap.com/) - The app uses the Bootstrap framework to hep create responsiveness.

## Testing
 
The testing has been manual, logging in as several users to make sure books can be added, edited and deleted, but only by the person who has uploaded them. All the other functionality such as registration, logging in, payment and downloading books has also been tested manually.

Payment testing was carried out using the 4242424242424242 Strip testing code.

Also tested on different browsers and devices using responsinator.com

## Deployment

The app uses os environment variables stored in the env.py file, which has not been added to GitHub or Heroku.

* os.environ.setdefault('STRIPE_PUBLISHABLE',’xxxxxxxxxxxxxxx’)
* os.environ.setdefault('STRIPE_SECRET', 'xxxxxxxxxxxxxx')
* os.environ.setdefault('DATABASE_URL', 'xxxxxxxxxxxx’)
* os.environ.setdefault('SECRET_KEY', 'xxxxxxxxxxxxxx ')
* os.environ.setdefault('AWS_ACCESS_KEY_ID','xxxxxxxxxxx')
* os.environ.setdefault('AWS_SECRET_ACCESS_KEY', 'xxxxxxxxxxxxxx’)
* os.environ.setdefault('EMAIL_ADDRESS','xxxxxxxxxxx')
* os.environ.setdefault('EMAIL_PASSWORD','xxxxxxxxxx')

To run in an IDE, use run or python3 manage.py runserver $IP:$C9_PORT", substituting the relevant port details.

## Credits

### Apps

The checkout, cart and search apps were copied over from the Code Institute course lessons and then changed as appropriate.

