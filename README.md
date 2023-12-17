# Plus Resources: Django Project Starter

Starter code for the Plus Django project.

# Sandra Lopez - She Codes News Project

## About This Project
This is a News story webiste created using Django as a project for the She Codes Plus Program. 
The theme of my website was inspired by the TV shows I was watching while learning Django.

## How To Run This Code

1. Clone repo - Make sure you clone the repo into the right place
2. Create and activate your Virtual environment (venv)
3. Migrate the database `python manage.py migrate`
4. Open the repo from your terminal and run the server using `python manage.py runserver`
5. Create a user account or log in and enjoy using {Coders} News
6. User Account details provided below

## Database Schema
![ERD](<she_codes_news/img/erd.png>)

## Project Features
- [x] Order stories by date
    ![Stories ordered newest to oldest](<she_codes_news/img/Screen Shot 2023-12-17 at 11.03.09 pm.png>)

- [ ] Styled "new story" form

- [x] Story images
    ![Individual story page with image](<she_codes_news/img/Screen Shot 2023-12-17 at 11.04.28 pm.png>)

- [x] Log-in/log-out
    ![Log out button only visible when loged in](<she_codes_news/img/Screen Shot 2023-12-17 at 11.07.09 pm.png>)

- [x] "Account view" page
    ![View your own account and list of all your stories](<she_codes_news/img/Screen Shot 2023-12-17 at 11.07.09 pm.png>)

- [x] "Create Account" page
    ![Create account only accessible when logged out](<she_codes_news/img/Screen Shot 2023-12-17 at 11.11.31 pm.png>)

- [x] View stories by author
    ![View your anothers account and list of all their stories](<she_codes_news/img/Screen Shot 2023-12-17 at 11.07.45 pm.png>)

- [x] "Log-in" button only visible when no user is logged in/"Log-out" button
        only visible when a user *is* logged in
        ![Log in only available when logged out](<she_codes_news/img/Screen Shot 2023-12-17 at 11.11.17 pm.png>)

- [x] "Create Story" functionality only available when user is logged in 
![Create a story form](<she_codes_news/img/Screen Shot 2023-12-17 at 11.06.32 pm.png>)

## Additional Features:
- [ ] Add categories to the stories and allow the user to search for stories by
        category.

- [x] Add the ability to update and delete stories (consider permissions - who
        should be allowed to update or and/or delete stories).
    ![Update and selete stories](<she_codes_news/img/Screen Shot 2023-12-17 at 11.08.46 pm.png>)

- [ ] Add the ability to “favourite” stories and see a page with your favourite
        stories.

- [ ] Our form for creating stories requires you to add the publication date,
        update this to automatically save the publication date as the day the
        story was first published (maybe you could then add a field to show
        when the story was updated).
         

Test accounts 1
username: test_test - password: hellotest

username: Ted Mosby - password: robinsparkles

username: aimz_99 - password: coolcoolcoolcool

username: chef_geller - password: minttreasures

username: schmidtyy - password: nickismyfave

username: dwight_rules - password: beetsbearsbattle