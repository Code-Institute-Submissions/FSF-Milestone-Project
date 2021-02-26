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

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

### Credits

Test book image - [pixabay](https://pixabay.com/vectors/book-paper-text-textbook-tome-2026267/)
placeholder for missing images - [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Placeholder-image.png)
Solution to crispy forms image saving - [Stackoverflow](https://stackoverflow.com/questions/3702465/how-to-copy-inmemoryuploadedfile-object-to-disk/30195605)