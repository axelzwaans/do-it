# Vanlife Blog

Vanlife blog is a simple and easy to use blogging application specifically designed for vanlifers. It's a straight forward and efficient way to document and share adventures, while also offering some interactivity features.

![responsive-design](../vanlife_blog/vanlife_blog/static/images-readme/responsive_design.png)

# UX

## User stories

Before starting this project, I thought about how this software application might provide value to a user. Using agile methodology, I identified a set of user stories and and used GitHub projects to document them. I tagged them either as 'must have' (this is functionality which my app has) and 'could have' (functionality which my app doesn't have, but would be a good feature.)

![github-issues](../vanlife_blog/vanlife_blog/static/images-readme/github_issues.png)

### User Accounts

1. As a **user** I can **register for an account** so that **I can write a blog and view other blog posts**.
2. As a **user** I can **log in and out of my account** so that **I will be the only one with access to it**.
3. As a **user** I can **log in using my email address** so that **my login information is consistent**.
4. As a **user** I can **view my account details** including **date joined and number of blog posts**.
5. As a **user** I can **update my username** so that **I can change it whenever I feel like**.

### User Blog

1. As a **user** I can **easily start blogging** so that **I can focus on what I'm writing rather than how to get set up**.
2. As a **user** i can **view my blog posts on the same page as the blog entry page** so that **I have a clear overview of what's going on**.
3. As a **user** I can **see the date on which my blog posts were created** so that **I can keep track of them**.
4. As a **user** I can **view other users' account information and blog posts** so that **I get a good understanding of who else is using the app**.
5. As a **user** I can **comment on other users' blog posts** so that I can **easily interact with them**.
6. As a **user** I can **view comments other users have made on my blog posts**.
7. As a **user** I can **like and unlike other people's blog posts** so that **I can give feedback without having to leave a comment**.
8. As a **user** I can **edit my own blog posts** so that **I can make alterations or fix mistakes**.
9. As a **user** I can **delete my own blog posts** so that **I don't need to worry about anything being permanent**.

### ADMIN

1. As a **site admin** I can **have a clear overview of all users registered to the site along with their account information**.
2. As a **site admin** I can **delete all users' blog posts**.
3. As a **site admin** I can **delete user accounts**.

## Design

### General, colour, font

This app has been built and customized using Bootstrap. The colour scheme was inspired by a cool image I found on google which matched the type of style I wanted for this project. I used this image as the main image on the landing page, and adjusted colouring throughout the app accordingly. I kept the design very simple, focusing on functionality and user-friendliness. I used 'Oxygen' as the main font in the app because of its simple and elegant style. I chose 'Sans-Serif' as a back up incase the primary font is unable to load. 

### Wireframes

I created a low-fidelity wireframe using Balsamiq to help me design my app. I created a mock up of each page;

Home page

![balsamiq-landing_page](../vanlife_blog/vanlife_blog/static/images-readme/landing_page_wireframe.png)

Login/register page

![balsamiq-login_page](../vanlife_blog/vanlife_blog/static/images-readme/login_wireframe.png)

Blog page

![balsamiq-blog_page](../vanlife_blog/vanlife_blog/static/images-readme/blog_page_wireframe.png)

Dashboard page

![balsamiq-dashboard](../vanlife_blog/vanlife_blog/static/images-readme/dashboard_wireframe.png)

## Entity Relationship Model

I added a graphical representation in the form of an entity relationship model to depict the relationship between entities within my models. I used Lucidchart to design it.

![entity-relationship-model](../vanlife_blog/vanlife_blog/static/images-readme/er_diagram.png)

## Features

I set out to create a simple app that anyone can engage in, providing an easy way for people in the vanlife community to log their travels and stories. I wanted this app to be a little more than a simple blogging app so I included functionality which allows users to interact with each other on a basic level, similar to a social media app.

### Existing features

- **Nav bar** - My app has a responsive nav bar which allows the user to seemlesly navigate between pages. The nav bar will show appropriate navigation options depending on whether the user is authenticated. It also includes the name of the app, 'Vanlife Blog', which links the user back to the landing page from any page. Going by Bootstrap's 'mobile first' approach, the navbar menu automatically renders as collapsed on smaller screen sizes, and can be toggled by a hamburger button.

![navbar-big](../vanlife_blog/vanlife_blog/static/images-readme/navbar_big.png)

![navbar-small](../vanlife_blog/vanlife_blog/static/images-readme/navbar_small.png)

- **Landing page** - The landing page contains the image which inspired the colour scheme of my app. It also includes a brief description of the app's purpose followed a button which generates the login/registration form, not taking the user away from the page.

![landing-page](../vanlife_blog/vanlife_blog/static/images-readme/landing_page.png)

- **Login / Registration** - The login / registration forms are presented on the landing page. A first time user will be required to register before they are able to use the app. To register, a user just needs to provide a username, email address, password and password confirmation. Once registered, they can then use their email address to log in. A user cannot login or register if they leave a field empty or enter invalid data.

![login](../vanlife_blog/vanlife_blog/static/images-readme/login.png)

- **Blog page** - This is where the magic happens! Using Bootstrap forms, I created a simple section where users can input their blog posts. A basic text input field followed by a 'post' button allowed space for blog posts to be displayed on the same page. Using Bootstrap 'cards' as content containers, I was able to neatly display multiple blog posts on a single page. Within these cards, users are able to edit and delete their own blog posts. 2 features I thought were fun to implement were a **comment** feature with which registered users can comment on other users' blog posts. Once a post has a comment, a collapsable link will appear which can display/hide all comments. Both post and comment authors are authorised to delete the comment. A **'like'** feature allowing a registered used to click a 'thumb' icon to like a post and click it again to 'unlike' it was implemented using Javascript. The blog post cards include the following information:
    - Blog post author, which can be clicked to view all the author's posts.
    - Blog post comments, including the comment author and date created.
    - Comment text input field.
    - Date the blog post was created.
    - 'Like' icon with number of likes.

![blog-page](../vanlife_blog/vanlife_blog/static/images-readme/blog_page.png)

- **Dashboard** - I created a simple dashboard page which displays registered users' information. It also has a button which links the user to a page where they can update their username. There are also links to logout or go to the blog page. If the user is also an admin, a table will be displayed underneath the user information card containing a list of all users currently registered to the app, along with their account information. Within this list, the admin has the capability to delete a user, and can click on the username to be redirected straight to that user's posts page.

![user-dashboard](../vanlife_blog/vanlife_blog/static/images-readme/user_dashboard.png)

![admin-dashboard](../vanlife_blog/vanlife_blog/static/images-readme/admin_dashboard.png)


- **Footer** - I added a simple footer to tie the page together and to put my name to the app. My name acts as a link to my email address and will open up the user's email editor should they want to contact me.

![footer](../vanlife_blog/vanlife_blog/static/images-readme/footer.png)

- **Alerts** - I implemented flexible alerts using the Bootstrap toolkit to provide contextual feedback to users whenever they perform an action for which feedback might be appreciated, or when an error occurs. For example, if a user logs in or creates/deletes a post, or when they try to log in with an empty form field. the appropriate notification will appear at the top of the page, and may be dismissed with the click of a button.

![alert-success](../vanlife_blog/vanlife_blog/static/images-readme/alert_success.png)

![alert-danger](../vanlife_blog/vanlife_blog/static/images-readme/alert_danger.png)

### Features to implement

There are endless features I would like to add to this app, but I will only mention a few key ones below as I feel they would provide the most value. Unfortunately I didn't have the time to implement them.

- Allow users to edit comments.
- Defensive programming - trigger modals to verify if a user wants to perform certain actions, such as deleting a comment.

## Testing

### Lighthouse testing

I ran Lighthouse tests on Chrome to check the performance, quality and correctness of this web app. I generated reports for mobile and desktop devices which gave the following results:

Desktop

![lighthouse-desktop](../vanlife_blog/vanlife_blog/static/images-readme/lighthouse_desktop.png)

Mobile

![lighthouse-mobile](../vanlife_blog/vanlife_blog/static/images-readme/lighthouse_mobile.png)