## Project Summary

# Design
The goal of this project is to create a digital marketplace & auctioneering site, where users can browse,  purchase, and review products.

More specifically, the design for this site revolves around a combination digital marketplace and auction house, which will serve as another piece of interactive fiction, as per my first milestone project.
The reason for this is fairly simple, it adds additional familiarity to the setting to allow for more naturalistic roleplaying, 
can potentially serve as an extension of gameplay for tabletop RPGs using the setting, and finally could potentially provide story hooks for future plot events in the setting.

To accomplish this, the site need to have a believable format, and the best way to accomplish this is to put a high-quality and professional-looking front on the site,
along side responsive design elements to give a higher-budget feel to the site design.

#### Similar Sites/Competitors
During the research portion of the design, I looked into sites for the same niche, so auctioneering sites. I have compiled a shortlist of three such sites, 
in order to acertain the common design elements to each of these sites and make sure to implement them into the finished project.

[Ebay](https://www.ebay.co.uk/)

[The Sale Room](https://www.the-saleroom.com/en-gb)

[John Pye Auctions](https://www.johnpye.co.uk/)

In addition to these three sites, I have looked into digital marketplaces where set goods are sold, or where small businesses or sole traders can sell their products.
Once again, I have looked for common design elements in these sites:

[Etsy](https://www.etsy.com/)

[Amazon](https://www.amazon.co.uk/)

---
#### Scope

In order for this project to be considered complete it must implement full CRUD functionality via front-end input & use the Stripe payment system to sell goods or services.
It must do this as a multi-app django project featuring full use of javascript, python, html, css, and a relational database of some kind. Additionally, it must implement a user authentication
 system of some sort, allowing users to log in and out, and have a good reason to allow this.

#### User Stories
After the previous research stages, a set of user stories have been created. This was done in a spreadsheet not only to provide an easy viewing experience, but also to ease testing later down the line.

[User Story Spreadsheet](designs/fsf_userstories_v1.xlsx)

---

### Skeleton
From the above user stories, some prototype visual designs have been created to provide structure to future development and inform the layout of the DOM tree.

![Wireframe - Home Page](designs/wireframes/templates/Home.png)
![Wireframe - Account Settings Page](designs/wireframes/templates/AccountSettings.png)
![Wireframe - Account Orders Page](designs/wireframes/templates/AccountPage.png)
![Wireframe - Item Page](designs/wireframes/templates/Item.png)
![Wireframe - Products List Page](designs/wireframes/templates/Products.png)
![Wireframe - Basket Page](designs/wireframes/templates/Basket.png)
![Wireframe - Create Account Page](designs/wireframes/templates/CreateAccount.png)
![Wireframe - Create Review Page](designs/wireframes/templates/CreateReview.png)
![Wireframe - Checkout Page](designs/wireframes/templates/Checkout.png)
![Wireframe - Acknowledge Page](designs/wireframes/templates/Acknowledgement.png)

### Database Diagram
![Database Diagram](designs/wireframes/database/db_er_diagram_v2.png)

--- 

### Surface
#### Colour Palette and Design Philosophy For Site
The main design philosophy for this site's visuals is to merge elements of the more modern minimalistic style of site design with the older content-heavy methods, in order to create a easily readable and clean style that shows as much content as possible without overloading the user and causing content to become visual noise.
To that end, a higher-contrast colour palette has been chosen, in order to make the elements distinct.

![Color Palette Swatch](designs/fsfpalette.png)

## Features
 
### Existing Features

- Users can create an account and verify their email address
- User profile avatar uploading
- Item browsing, filtering and searching
- Items can be added to cart, taken to checkout, and purchased
- User can view their Orders
- User can post reviews of items they have purchased.
- Items show these reviews on their respective pages, along with an aggregated average score.

### Features Left to Implement
Due to time & knowledge constraints, I was forced to cut a few features. 

First amoungst these was the auction feature, as it would have dramatically increased development time due to the number of email calls and time-based methods it would require.

Secondly The styling had to be cut back due to time, as I lost a great deal due to stress-related issues.

Finally, The website looks awful on mobile and does not work well. Sadly, I was not able to get mobile styling done in time for this, for the same reason as before.

## Technologies Used

- [Django](https://www.djangoproject.com/)
    - The project uses **Django** to simplify website creation and development.
- [Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap** to provide styling and layout to pages.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Fontawesome](https://fontawesome.com/)
    - The project uses **Fontawesome** to provide icons.
- [GoogleFonts](https://fonts.google.com/)
    - The project uses **GoogleFonts** to provide different text fonts.
- [Stripe](https://stripe.com/)
    - The project uses **Stripe** for financial services and checkout.

## Testing

As little time as I have had, I still took it upon myself to ensure functionality. To that end I have tested against the User stories still relevant to project, taking in to account cuts that had been made during development.

With this in mind, here are my assessments of the user stories and their various states of completion.

[User Story Spreadsheet](designs/fsf_userstories_v1-implementation.xlsx)

So, while the vast majority of user stories have been implemented, this does not mean the website is entirely feature complete.

The mobile scaling is virtually non-existant, as the time for that was lost during aforementioned stress-related issues.
Additionally, the visuals as a whole could do with several more passes as the entire site is somewhat bland and lacks any real distinction.
Finally, The pages rarely live up to the design works, and could do with additonal work to bring them more in line with those and each other.

All in all, I'm a little surprised I managed to get even this submitted, given the difficulties I had during development. Despite that, I am not entirely satisfied with the current state of the site, but it is what it is.

#### Known Bugs

Aside from the previously talked-about mobile scaling issues, one persistent odd issue cropped up during development.

In the account page, when setting a new avatar, the image file for it will update, but the stripe forms for this will not.
As far as i can tell, this has something to do with stripe reading the model data before the image has finished uploading. This could possibly be fixed by altering the view, adding an additional page in the interim so that the user is not returned to the page before the image is finished uploading.

## Deployment

In order to deploy this to heroku, I had to set up amazon web service stuff, specifically a server for the static & media files to exist on.
This was quite a process. It needed me to setup an AWS account, setup the bucket, get the s3 stuff sorted, then finally add the env variables, and call it with Boto3 & gunicorn to ensure that it could be called properly for storing files.

Then, I needed to setup the gmail app connection, which was far simpler. though in my fatigued and stressed-out state I made more than a few typos in entering it all.

Finally, I simply needed to point heroku at this git repository, add the remaining environment variables and set up automatic deployment.

There was one persistent issue, that I have no idea if I can even fix. Heroku seems set on using the variable name 'EMAIL_HOST_USERNAME', one of the previous typos, instead of 'EMAIL_HOST_USER', which is actually what settings.py shows.
I hope to have this finished in this final deployment, but I honestly couldn't figure out what was causing it.

### Credits

Test book image - [pixabay](https://pixabay.com/vectors/book-paper-text-textbook-tome-2026267/)
placeholder for missing images - [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Placeholder-image.png)
Solution to crispy forms image saving - [Stackoverflow](https://stackoverflow.com/questions/3702465/how-to-copy-inmemoryuploadedfile-object-to-disk/30195605)