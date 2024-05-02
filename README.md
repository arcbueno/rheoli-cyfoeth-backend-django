# Rheoli Cyfoeth

This project is a simple implementation of a REST API made in Django for the purpose of learning the framework and following the Model-View-Controller (MVC) design pattern. 

The Django framework is very tricky to understand because it has a lot of "under the hood" features that I am not used to. My objective is understand its features and use it as I want. 
> It is expected that some views, controllers and other classes will not be following a pattern, this project is a document for myself to use in future projects to understand why or how.

#### About Django and MVC

Django is a powerful web framework written in Python that follows the MVC architectural pattern. It provides a convenient way to build web applications by abstracting away common tasks, such as database management, URL routing, and form handling.

The Model-View-Controller pattern separates the application logic into three interconnected components:

- **Model**: Represents the data and business logic of the application. It interacts with the database and performs operations such as data retrieval, manipulation, and validation.

- **View**: Handles the presentation logic and renders the data to the user. It receives user input and communicates with the model to retrieve the necessary data.

- **Controller**: Acts as the intermediary between the model and the view. It receives user input from the view, processes it, and updates the model or view accordingly.

Of course, as a study project, it means that at final moment I can affirm that the MVC pattern is not useful for developing a Django application, but I want to simulate what is a big django project in a company. 

The project name itself means "Wealth Management" in Gaelic, pretty not creative I admit.

#### My conclusions
- The Django Rest Framework (DRF) has a lot of functionalities and many ways to implement the same thing. The ViewSet classes help a lot when creating a simple CRUD, so it's easy to implement something fast and simple (like the ItemView), but it's not so intuitive when we need to implement some rules, like limiting the actions (like I did on the MovingHistoryView) or adding a layer of validation (like in the User flows, that I used the Controller as a business logic layer). 
- Although it sounds like it's a negative point, it's not. It's really good that DRF is flexible enough to implement all the CRUD endpoints without having to worry about each route at the same time it has ways to implement logic "by hand", it's different than when I worked in a REST API in C#, but still a way that works.
- (Before this project, I did some courses to understand it, but none showed me more complex things about the framework so I invested some time reading the documentation.)
- About the MVC, I tried to use it without creating unnecessary classes, that's why the ItemView does not have an ItemController. The pattern is not a waste but it is still hard to not use the shortcuts that the DRF allows. I created the Controller classes to help with validation and to not write so much code in the View classes. 
- If this system turns bigger, I would create External models and Repository classes. The external models I would use when the data is on the View layer and the repository classes would be useful when saving the data on the database (with a converter from external models to domain models as well).
- Continuing on design patterns, I used the Result pattern, similar to the [Either](https://www.thoughtworks.com/insights/blog/either-data-type-alternative-throwing-exceptions), using the package [returns](https://pypi.org/project/returns/), while getting the result from the Controller. Probably there's a better way to code it, but I am a bit new to the Python universe.
- My conclusion is: that I have to learn more. I really liked Django and how fast I can create things with it if I have experience. A downside is that all that I wanted to do I had to search on its documentation, the classes and code don't explain much. Would still use it on a project? Yes, but on an MVP. The next target is Flask.

Thank you