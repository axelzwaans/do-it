# Vanlife Blog

Vanlife blog is a simple and easy-to-use blogging application specifically designed for vanlifers. It's a straightforward and efficient way to document and share adventures, while also offering some interactivity features.

![responsive-design](../vanlife_blog/vanlife_blog/static/images-readme/responsive_design.png)

# UX

## User stories

Before starting this project, I thought about how this software application might provide value to a user. Using agile methodology, I identified a set of user stories and used GitHub projects to document them. I tagged them either as 'must have' (this is functionality which my app has) or 'could have' (functionality which my app doesn't have, but would be a good feature.)

![github-issues](../vanlife_blog/vanlife_blog/static/images-readme/github_issues.png)

### User Accounts

1. As a **user** I can **register for an account** so that **I can write a blog and view other blog posts**.
2. As a **user** I can **log in and out of my account** so that **I will be the only one with access to it**.
3. As a **user** I can **log in using my email address** so that **my login information is consistent**.
4. As a **user** I can **view my account details** including **date joined and number of blog posts**.
5. As a **user** I can **update my username** so that **I can change it whenever I feel like**.

### User Blog

1. As a **user** I can **easily start blogging** so that **I can focus on what I'm writing rather than how to get set up**.
2. As a **user** I can **view my blog posts on the same page as the blog entry page** so that **I have a clear overview of what's going on**.
3. As a **user** I can **see the date on which my blog posts were created** so that **I can keep track of them**.
4. As a **user** I can **view other users' account information and blog posts** so that **I get a good understanding of who else is using the app**.
5. As a **user** I can **comment on other users' blog posts** so that I can **easily interact with them**.
6. As a **user** I can **view comments other users have made on my blog posts**.
7. As a **user** I can **like and unlike other people's blog posts** so that **I can give feedback without having to leave a comment**.
8. As a **user** I can **edit my own blog posts** so that **I can make alterations or fix mistakes**.
9. As a **user** I can **delete my blog posts** so that **I don't need to worry about anything being permanent**.

### ADMIN

1. As a **site admin** I can **have a clear overview of all users registered to the site along with their account information**.
2. As a **site admin** I can **delete all users' blog posts**.
3. As a **site admin** I can **delete user accounts**.

## Design

### General, colour, font

This app has been built and customized using Bootstrap. The colour scheme was inspired by a cool image I found on google which matched the type of style I wanted for this project. I used this image as the main image on the landing page, and adjusted the colouring throughout the app accordingly. I kept the design very simple, focusing on functionality and user-friendliness. I used 'Oxygen' as the main font in the app because of its simple and elegant style. I chose 'Sans-Serif' as a backup in case the primary font is unable to load. 

### Wireframes

I created a low-fidelity wireframe using Balsamiq to help me design my app. I created a mock-up of each page;

**Home page**

![balsamiq-landing_page](../vanlife_blog/vanlife_blog/static/images-readme/landing_page_wireframe.png)

**Login/register page**

![balsamiq-login_page](../vanlife_blog/vanlife_blog/static/images-readme/login_wireframe.png)

**Blog page**

![balsamiq-blog_page](../vanlife_blog/vanlife_blog/static/images-readme/blog_page_wireframe.png)

**Dashboard page**

![balsamiq-dashboard](../vanlife_blog/vanlife_blog/static/images-readme/dashboard_wireframe.png)

## Entity Relationship Model

I added a graphical representation in the form of an entity-relationship model to depict the relationship between entities within my models. I used Lucidchart to design it.

![entity-relationship-model](../vanlife_blog/vanlife_blog/static/images-readme/er_diagram.png)

## Features

I set out to create a simple app that anyone can engage in, providing an easy way for people in the vanlife community to log their travels and stories. I wanted this app to be a little more than a simple blogging app so I included functionality which allows users to interact with each other on a basic level, similar to a social media app.

### Existing features

- **Nav bar** - My app has a responsive nav bar which allows the user to seamlesly navigate between pages. The nav bar will show appropriate navigation options depending on whether the user is authenticated. It also includes the name of the app, 'Vanlife Blog', which links the user back to the landing page from any page. Going by Bootstrap's 'mobile first' approach, the navbar menu automatically renders as collapsed on smaller screen sizes, and can be toggled by a hamburger button.

![navbar-big](../vanlife_blog/vanlife_blog/static/images-readme/navbar_big.png)

![navbar-small](../vanlife_blog/vanlife_blog/static/images-readme/navbar_small.png)

- **Landing page** - The landing page contains the image which inspired the colour scheme of my app. It also includes a brief description of the app's purpose followed by a button which generates the login/registration form, not taking the user away from the page.

![landing-page](../vanlife_blog/vanlife_blog/static/images-readme/landing_page.png)

- **Login / Registration** - The login/registration forms are presented on the landing page. A first-time user will be required to register before they can to use the app. To register, a user just needs to provide a username, email address, password and password confirmation. Once registered, they can then use their email address to log in. A user cannot log in or register if they leave a field empty or enter invalid data.

![login](../vanlife_blog/vanlife_blog/static/images-readme/login.png)

- **Blog page** - This is where the magic happens! Using Bootstrap forms, I created a simple section where users can input their blog posts. A basic text input field followed by a 'post' button allowed space for blog posts to be displayed on the same page. Using Bootstrap 'cards' as content containers, I was able to neatly display multiple blog posts on a single page. Within these cards, users can edit and delete their own blog posts. 2 features I thought were fun to implement were a **comment** feature with which registered users can comment on other users' blog posts. Once a post has a comment, a collapsable link will appear which can display/hide all comments. Both post and comment authors are authorised to delete the comment. A **'like'** feature allowing a registered user to click a 'thumb' icon to like a post and click it again to 'unlike' it was implemented using Javascript. The blog post cards include the following information:
    - Blog post author, which can be clicked to view all the author's posts.
    - Blog post comments, including the comment author and date created.
    - Comment text input field.
    - Date the blog post was created.
    - 'Like' icon with the number of likes.

![blog-page](../vanlife_blog/vanlife_blog/static/images-readme/blog_page.png)

- **Dashboard** - I created a simple dashboard page which displays registered users' information. It also has a button which links the user to a page where they can update their username. There are also links to log out or go to the blog page. If the user is also an admin, a table will be displayed underneath the user information card containing a list of all users currently registered to the app, along with their account information. Within this list, the admin can delete a user and click on the username to be redirected straight to that user's posts page.

![user-dashboard](../vanlife_blog/vanlife_blog/static/images-readme/user_dashboard.png)

![admin-dashboard](../vanlife_blog/vanlife_blog/static/images-readme/admin_dashboard.png)

- **Footer** - I added a simple footer to tie the page together and to put my name to the app. My name acts as a link to my email address and will open up the user's email editor should they want to contact me.

![footer](../vanlife_blog/vanlife_blog/static/images-readme/footer.png)

- **Alerts** - I implemented flexible alerts using the Bootstrap toolkit to provide contextual feedback to users whenever they perform an action for which feedback might be appreciated, or when an error occurs. For example, if a user logs in or creates/deletes a post, or when they try to log in with an empty form field. the appropriate notification will appear at the top of the page and may be dismissed with the click of a button.

![alert-success](../vanlife_blog/vanlife_blog/static/images-readme/alert_success.png)

![alert-danger](../vanlife_blog/vanlife_blog/static/images-readme/alert_danger.png)

### Features to implement

There are endless features I would like to add to this app, but I will only mention a few key ones below as I feel they would provide the most value. Unfortunately, I didn't have the time to implement them.

- Allow users to edit comments.
- Defensive programming - trigger modals to verify if a user wants to perform certain actions, such as deleting a comment.

## Testing

### Lighthouse testing

I ran Lighthouse tests on Chrome to check the performance, quality and correctness of this web app. I generated reports for mobile and desktop devices which gave the following results;

**Desktop**

![lighthouse-desktop](../vanlife_blog/vanlife_blog/static/images-readme/lighthouse_desktop.png)

**Mobile**

![lighthouse-mobile](../vanlife_blog/vanlife_blog/static/images-readme/lighthouse_mobile.png)

### HTML testing

I used the W3 HTML checker to check the markup validity of my app. After initially validating by URI, I got 2 errors and 1 warning;

![html-checker](../vanlife_blog/vanlife_blog/static/images-readme/html_checker_1.png)

A few tweaks in my HTML code sorted this out.

![html-checker-fixed](../vanlife_blog/vanlife_blog/static/images-readme/html_checker_2.png)

### CSS testing

I used the W3C CSS validation service to check for errors and warnings and received the following report;

![css-checker-errors](../vanlife_blog/vanlife_blog/static/images-readme/css_checker.png)

### JavaScript testing

I used JSHint to detect errors and potential problems in my JavaScript code. 

![js-checker-errors](../vanlife_blog/vanlife_blog/static/images-readme/js_tester_warnings.png)

After running my JS code through the validator, I got 8 warnings, which were all version related. I was able to resolve these errors by adding a small block of code to the top of the script.js file.

![js-checker](../vanlife_blog/vanlife_blog/static/images-readme/js_tester.png)

### Python testing

I used the CI Python Linter to analyse all python files for potential errors. 

**app.py**

![python-checker-app](../vanlife_blog/vanlife_blog/static/images-readme/python_tester_app.png)

**models.py**

![python-checker-models](../vanlife_blog/vanlife_blog/static/images-readme/python_tester_models.png)

**routes.py**

![python-checker-routes](../vanlife_blog/vanlife_blog/static/images-readme/python_tester_routes.png)

**auth.py**

![python-checker-auth](../vanlife_blog/vanlife_blog/static/images-readme/python_tester_auth.png)

All files came back without any errors, except for the init.py file.

**init.py**

![python-checker-init](../vanlife_blog/vanlife_blog/static/images-readme/python_tester_init.png)

I was able to ignore these errors as putting them at the top of the file would result in a circular import error.

### Manual testing

| Function| Test case | Result |                                                          
|---------|-----------|--------|
| Registration form | Form checks if email exists | Pass
| Registration form | Form checks if username exists | Pass
| Registration form | Form checks if email is valid | Pass
| Registration form | Form checks if username is valid | Pass
| Registration form | Form checks if password is valid | Pass
| Registration form | Form checks if both password fields match | Pass
| Registration form | User successfully registered | Pass
| Login form | Form checks if email exists | Pass
| Login form | Form checks if password is correct | Pass
| Login form | Form checks if password is correct | Pass
| Blog post | Form checks if text input is valid | Pass
| Blog post | Create blog post | Pass
| Blog post | Display blog post | Pass
| Blog post | Edit blog post | Pass
| Blog post | Delete blog post | Pass
| Comment | Create comment | Pass
| Comment | Display comment | Pass
| Comment | Delete comment | Pass
| Logout | User can logout | Pass
| Dashboard | User can edit username | Pass
| Dashboard | Admin can delete user | Pass

## Deployment

I deployed this app on Heroku, which is a cloud application platform for developers to build, run and operate their applications. As Heroku is no longer offering multiple free databases to their free tier users, I used a separate free database service called ElephantSQL to host my PostgreSQL database. First I created my ElephantSQL account;

1. Navigate to the ElephantSQL website and click 'Get a managed database today'.
2. Select 'Try now for FREE' in the TINY TURTLE database plan.
3. Select 'Log in with GitHub' and authorize ElephantSQL with my selected GitHub account
4. Create a new team. (I am the team!)

After setting up my account, I created the database;

1. In the top right-hand corner of my account dashboard, click 'Create New Instance'
2. Set up my plan.
3. Select region and data center.
4. Click 'Review'
5. Check details and click 'Create instance'
6. Return to the ElephantSQL dashboard and click on the database instance name for my project.
7. In the URL section, click the copy icon to copy the database URL to my clipboard.

After creating the database and configuring my Gitpod code for Heroku, I was ready to deploy my project. I already had a Heroku account from a previous project, so setting up for deployment was next;

1. Log into Heroku.com and select 'Create new app' on user dashboard.
2. Choose a name and closest region and click 'Create app'.
3. Go to the settings tab of my app.
4. Click 'Reveal Config Vars'.
5. Copy the database URL from ElephantSQL.
6. Add a Config Var called 'DATABASE_URL' and paste my ElephantSQL database URL in as the value, click 'Add'.
7. Add each of my other environment variables except DEVELOPMENT and DB_URL from the env.py file as a config var.

Ready for deployment;

1. Navigate to the “Deploy” tab of my app.
2. In the deployment method section, select 'Connect to GitHub'.
3. Search for my repo and click 'Connect'.
4. I enabled 'Automatic Deploys' so that every push to the main branch will deploy a new version of the app.
5. DEBUG mode set to 'False'.
6. Click 'Deploy branch' to start the build process.

Add tables to database;

1. On the Heroku app dashboard, click the 'More' button and select 'Run console'.
2. Type 'python3' into the console and click 'Run'.
3. Create the tables using the same commands I use in Gitpod.
4. Exit the Python terminal by typing 'exit()'.
5. Click 'Open app' and test CRUD functionality.

## Admin log in information

Please use the following log in details to access admin capabilities;

Email: admin@admin.com

Password: admin123

## Credits

### Content

- [Balsamiq](https://balsamiq.com) for wireframes.
- [This YouTube tutorial](https://www.youtube.com/watch?v=GQcM8wdduLI&t=870s) for app functionality.
- [Lucidchart](https://www.lucidchart.com) for entity relationship model.
- [StackOverflow](https://stackoverflow.com) for help with code-related issues.
- [Flask documentation](https://flask.palletsprojects.com/en/2.2.x/) for help with setting up a Flask app.
- [Bootstrap](https://getbootstrap.com) for app layout and components.
- [Heroku](https://dashboard.heroku.com/apps) for cloud platform.
- [ElephantSQL](https://www.elephantsql.com/) for hosting the database.
- [Code Institute](https://learn.codeinstitute.net/dashboard) for course material.

### Media

- [Vanlifer.com](https://vanlifer.com/products/van-vector) for the home page image.
- [Google Fonts](https://fonts.google.com/knowledge) for the 'Oxygen' font.
- [Font Awesome](https://fontawesome.com/) for the 'like' icon.