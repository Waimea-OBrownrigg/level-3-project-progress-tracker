# Sprint 4 - Developing a Refined and Complete System


## Sprint Goals

Develop the system until it is fully featured, with a refined UI and it satisfies the requirements. The system will be fully tested at this point.

### Specific Goals

**Edit these goals as needed**

- Refine the design and UI of the website
- Refine the user experience (UX) of the system
- Perform final, full-system testing


## Adding colours

To make my site more visually appealing I added a blue/grey colour palette.

![First coloured home page](screenshots/homepagecss1.png)

### Changes / Improvements

A lot of the contrast was bad, and also the main text wasn't coloured, so I fixed that.

![Second coloured home page](screenshots/homepagecss1.5.png)


## Formatting

To continue making my site more readable, I added padding and moved around different assets on my pages

![Image showcasing a fully formatted home page](screenshots/homepagecss2.png)

### Changes / Improvements

None


## Testing unauthorized  access

There are some pages on my website that should only be accessed when you are logged in to the right account, but at the moment you can bypass tis by typing the url of the page into the search bar, as shown in the GIF below.

![Logged out user accessing the edit page for a project](screenshots/securityissue.gif)

### Changes / Improvements

Added functions to check if A: You're logged in. B: If applicable, your account owns the project you're trying to edit/delete. 

![Logged out user unable to access the edit page for a project](screenshots/unauthorizedaccess.gif)

![Non owners unable to edit other people's project](screenshots/unauthorizedaccess2.gif)


## Testing entering add milestone page for a project that doesn't exist.

The add milestone page is intended to come directly after the create project page, so when it doesn't it causes issues

![Accessing the add milestone page directly causes a crash](screenshots/milestonecrash.gif)

### Changes / Improvements

I just needed to add a simple check and now it simply redirects to project creation.

![Logged out user accessing the edit page for a project](screenshots/milestoneredirects.gif)



## Sprint Review

With this sprint done my project is finally complete,my website now has css, and is as far as I can tell, bug free.

